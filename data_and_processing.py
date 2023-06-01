import numpy as np
import pandas as pd


# Класс хранения данных сигналов с шумом и без, разницы, списки частот поглощения
# Методов обработки и получения данных
class DataAndProcessing:
    def __init__(self):
        self.names_data = [
            "frequency",  # Без шума
            "without_gas",  # Без шума
            "with_gas",  # Сигнал
        ]
        self.names_processing = [
            "difference",  # Разница
            "difference_above_threshold",  # Логический массив, где разница выше порога
            "intervals_after_difference"  # Интервалы выше порога, со значением данных с веществом
        ]
        self.data = pd.DataFrame(columns=self.names_data + self.names_processing)

        # Пороговое значение для корреляции
        self.difference_threshold = None

        # Точки линий поглощения, от разницы (строчки: индекс и гамма)
        self.point_absorption_after_difference = pd.DataFrame()

    # (*) Чистит данные процесса обработки
    def clear_data_processing(self):
        self.data[self.names_processing] = np.nan
        self.difference_threshold = None
        self.point_absorption_after_difference = pd.DataFrame()

    # (*) Чистит все данные (альтернатива:  self.data = self.data.head(0))
    def clear_data(self):
        self.data = self.data.head(0)
        self.difference_threshold = None
        self.point_absorption_after_difference = pd.DataFrame()

    # ОБЩИЙ АЛГОРИТМ
    def all_processing(
            self,
            difference_threshold: float
    ):
        # Нет данных
        if (self.data["frequency"].empty and
                self.data["without_gas"].empty and
                self.data["with_gas"].empty):
            return

        # Чистим от прошлых данных
        self.clear_data_processing()

        # (1) Разница
        self.data_difference(difference_threshold)  # Считаем разницу между данными и порог
        self.compare_difference_and_threshold()  # логический массив данных из разницы выше порога

        # Находим
        self.find_intervals_after_difference()  # Интервалы линий поглощения (для 1 графика)
        self.find_point_after_difference()  # Точки линий поглощения

    # ОБРАБОТКА (1.1): Считаем разницу между данными
    def data_difference(self, threshold_percentage):
        # Нет данных - сброс
        if self.data["without_gas"].isnull().values.all() or self.data["with_gas"].isnull().values.all():
            return

        # Считаем разницу
        self.data["difference"] = (self.data["with_gas"] - self.data["without_gas"]).clip(lower=0)

        # Задаем порог
        self.difference_threshold = \
            self.data["difference"].max() * (threshold_percentage/100)

    # ОБРАБОТКА (1.2): Возвращаем серию "порогового значения разницы" для построения
    def data_difference_threshold(self):
        # Данных нет - сброс
        if self.difference_threshold is None:
            return

        return pd.Series([self.difference_threshold] * 2,
                         index=[self.data["frequency"].iloc[0],
                                self.data["frequency"].iloc[-1]])

    # ОБРАБОТКА (1.3): логический массив данных из разницы выше порога
    def compare_difference_and_threshold(self):
        # Данных нет - сброс
        if (self.difference_threshold is None) or self.data["without_gas"].empty:
            return

        # Логический массив, где разница выше порога
        self.data["difference_above_threshold"] = self.data["difference"] >= self.difference_threshold

    # ОБРАБОТКА (*): ИНТЕРВАЛЫ И ТОЧКИ ЛИНИЙ ПОГЛОЩЕНИЯ
    # (1) # Интервалы линий поглощения, выше порога, со значением данных с веществом (для 1 графика)
    def find_intervals_after_difference(self):
        # нет данных - сброс
        if self.difference_threshold is None:
            return

        # Все что выше порога, приобретает значение данных с веществом, остальное None
        self.data.loc[
            self.data["difference_above_threshold"], "intervals_after_difference"] = self.data["with_gas"]

    # (2) Точки линий поглощения, от корреляции (строчки: индекс и гамма)
    def find_point_after_difference(self):
        self.point_absorption_after_difference = pd.DataFrame({
            "gamma": DataAndProcessing.find_point(
                self.data["with_gas"][  # В качестве значений - гамма с веществом
                    self.data["difference_above_threshold"]  # Оставляем элементы выше порога
                ]
            )})
        self.point_absorption_after_difference["frequency"] = \
            self.data["frequency"][self.point_absorption_after_difference.index]
        self.point_absorption_after_difference["status"] = False

    # ************************************************************************************
    #                                       ОБЩИЕ МЕТОДЫ
    # ОБРАБОТКА (*): ИНТЕРВАЛЫ И ТОЧКИ ЛИНИЙ ПОГЛОЩЕНИЯ
    # (1) ИНТЕРВАЛА ПОГЛОЩЕНИЯ
    # Поиск участков выше порога -> получение индексов начала и конца интервала
    # ---------------------------------------------------------------------
    # В формате индекс: начало интервала; значение: конец интервала. Пример, при пороге 4:
    # ind: 0 1 2 3 4 5 6 7 8 9 10-> ind: 1 5 9 -> (пары: с 1 по 2; с 5-6; с 9 по 9)
    # val: 1 5 8 1 3 9 8 1 0 8 0 -> val: 2 6 9
    @staticmethod
    def find_intervals_borders(samples, threshold):
        bool_samples = samples[samples >= threshold]
        xx = bool_samples.groupby((bool_samples.index != bool_samples.index.to_series().shift() + 1)
                                  .cumsum()).apply(lambda grp: (grp.index[0], grp.index[-1]))
        return pd.Series(xx.str[1].values, index=xx.str[0])

    # (2) ТОЧКИ ПОГЛОЩЕНИЯ
    # (2.1) Поиск участков выше порога -> на участке применяем функцию поиск ТОЧКИ ПОГЛОЩЕНИЯ
    # ---------------------------------------------------------------------
    # В формате индекс: начало интервала; значение: конец интервала. Пример, при пороге 4:
    # ind: 0 1 2 3 4 5 6 7 8 9 10-> ind: 2 5 9 -> (в интервале от 1-2: 1 мах 8;...)
    # val: 1 5 8 1 3 9 8 1 0 8 0 -> val: 8 9 8
    # Пример samples: bool_samples = samples[samples >= threshold] - массив индексов и значений
    # без пар индексов не подходящих под условие
    @staticmethod
    def find_point(samples):
        xx = samples.groupby((samples.index != samples.index.to_series().shift() + 1)
                             .cumsum()).apply(lambda grp: (DataAndProcessing.max_index_val(grp)))
        return pd.Series(xx.str[1].values, index=xx.str[0].values)

    # (2.2) Метод поиска линии поглощения на участке
    @staticmethod
    def max_index_val(mass):
        index = mass.idxmax()
        val = mass[index]
        return index, val
