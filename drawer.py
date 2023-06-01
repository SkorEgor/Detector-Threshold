from graph import Graph
from data_and_processing import DataAndProcessing


# ШАБЛОНЫ ОТРИСОВКИ ГРАФИКОВ
# Очистка и подпись графика (вызывается в начале)
def cleaning_and_chart_graph(graph: Graph, x_label, y_label, title):
    graph.toolbar.home()  # Возвращаем зум в домашнюю позицию
    graph.toolbar.update()  # Очищаем стек осей (от старых x, y lim)
    # Очищаем график
    graph.axis.clear()
    # Задаем название осей
    graph.axis.set_xlabel(x_label)
    graph.axis.set_ylabel(y_label)
    # Задаем название графика
    graph.axis.set_title(title)


# Отрисовка (вызывается в конце)
def draw_graph(graph: Graph, chart_caption: bool = True):
    # Рисуем сетку
    graph.axis.grid()
    # Инициирует отображение наименований графиков (label plot)
    if chart_caption:
        graph.axis.legend()
    # Убеждаемся, что все помещается внутри холста
    graph.figure.tight_layout()
    # Показываем новую фигуру в интерфейсе
    graph.canvas.draw()


# Отрисовка при отсутствии данных
def no_data(graph: Graph):
    graph.axis.text(0.5, 0.5, "Нет данных",
                    fontsize=14,
                    horizontalalignment='center',
                    verticalalignment='center')
    # Отрисовка, без подписи данных графиков
    draw_graph(graph, chart_caption=False)


# Класс художник. Имя холст (graph), рисует на нем данные (data_and_processing)
class Drawer:
    # ПАРАМЕТРЫ ГРАФИКОВ
    # График №1 Данные
    title_data = "График №1. Данные с исследуемым веществом и без вещества"
    horizontal_axis_name_data = "Частота [МГц]"
    vertical_axis_name_data = "Гамма [усл.ед.]"

    name_without_gas = "Без вещества"
    color_without_gas = "#515151"
    name_with_gas = "C веществом"
    color_with_gas = "#DC7C02"
    list_absorbing = "Участок с линией поглощения"
    color_absorbing = "#36F62D"

    # График №2 Разница
    title_difference = "График №2. Положительная разница между данными."
    horizontal_axis_name_difference = "Частота [МГц]"
    vertical_axis_name_difference = "Отклонение"

    name_difference = "Разница"
    color_difference = "#310DEC"
    list_threshold = "Порог"
    color_threshold = "#EE2816"

    # ОТРИСОВКИ
    # (1) Без данных и с данными
    @staticmethod
    def updating_gas_graph(
            graph: Graph,
            data_signals: DataAndProcessing,
    ):
        # Очистка, подпись графика и осей (вызывается в начале)
        cleaning_and_chart_graph(
            # Объект графика
            graph=graph,
            # Название графика
            title=Drawer.title_data,
            # Подпись осей
            x_label=Drawer.horizontal_axis_name_data, y_label=Drawer.vertical_axis_name_data
        )

        # Данных нет
        if data_signals.data["without_gas"].empty and data_signals.data["with_gas"].empty:
            no_data(graph)
            return

        # Если есть данные без газа, строим график
        if not data_signals.data["without_gas"].empty:
            graph.axis.plot(
                data_signals.data["frequency"],
                data_signals.data["without_gas"],
                color=Drawer.color_without_gas, label=Drawer.name_without_gas)
        # Если есть данные с газом, строим график
        if not data_signals.data["with_gas"].empty:
            graph.axis.plot(
                data_signals.data["frequency"],
                data_signals.data["with_gas"],
                color=Drawer.color_with_gas, label=Drawer.name_with_gas)
        # Если интервалы корреляции найдены, строим график
        if not data_signals.data["intervals_after_difference"].isnull().values.all():
            graph.axis.plot(
                data_signals.data["frequency"],
                data_signals.data["intervals_after_difference"],
                color=Drawer.color_absorbing, label=Drawer.list_absorbing)

        # Отрисовка (вызывается в конце)
        draw_graph(graph)

    # (2) График корреляции
    @staticmethod
    def updating_deviation_graph(
            graph: Graph,
            data_signals: DataAndProcessing
    ):
        # Очистка, подпись графика и осей (вызывается в начале)
        cleaning_and_chart_graph(
            # Объекты графика
            graph=graph,
            # Название графика
            title=Drawer.title_difference,
            # Подпись осей
            x_label=Drawer.horizontal_axis_name_difference, y_label=Drawer.vertical_axis_name_difference
        )

        # Данных нет
        if data_signals.data["difference"].isnull().values.all():
            no_data(graph)
            return

        # Если есть данные корреляции, строим график
        if not data_signals.data["difference"].isnull().values.all():
            graph.axis.plot(
                data_signals.data["frequency"],
                data_signals.data["difference"],
                color=Drawer.color_difference, label=Drawer.name_difference)
        # Если есть порог, строим график
        if data_signals.difference_threshold is not None:
            # Высчитываем порог
            threshold_data = data_signals.data_difference_threshold()
            graph.axis.plot(
                threshold_data.index,
                threshold_data.values,
                color=Drawer.color_threshold, label=Drawer.list_threshold)

        # Отрисовка (вызывается в конце)
        draw_graph(graph)
