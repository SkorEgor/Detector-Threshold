<!---------------------------------------------------------------------------------->
<div align="left">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" height=24> 
<img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" height=24>
<img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" height=24>
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" height=24>
<img src="https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=Qt&logoColor=white" height=24>
</div>

<h1 align="center">Detector Threshold / Детектор по пороговому значению</h1>

Программа одного из методов дипломной работы бакалавриата, на тему *"Развитие метода автоматизации обработки спектроскопических данных, полученных с использованием спектрометра с фазовой манипуляцией воздействующего на газ излучения"*

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> Содержание </h2>

1. [ Описание задачи и демонстрация работы ](https://github.com/SkorEgor/Detector-Threshold#-1-описание-задачи-и-демонстрация-работы-)
2. [ Входные и выходные данные ](https://github.com/SkorEgor/Detector-Threshold#-2-входные-и-выходные-данные-)
3. [ Описание логической структуры - Алгоритм программы ](https://github.com/SkorEgor/Detector-Threshold#-3-описание-логической-структуры---алгоритм-программы-)
4. [ Описание программной структуры - Используемые методы ](https://github.com/SkorEgor/Detector-Threshold#-4-описание-программной-структуры---используемые-методы-)
   1. [ Метод нахождения разницы ](https://github.com/SkorEgor/Detector-Threshold#-41-метод-нахождения-разницы---data_difference-)
   2. [ Метод возврата все данные данных, в виде (bool) - выше порога ](https://github.com/SkorEgor/Detector-Threshold#-42-метод-возврата-все-данные-данных-в-видеbool---выше-порога---compare_difference_and_threshold-)
   3. [ Метод возврата данных выше порога (фильтр) ](https://github.com/SkorEgor/Detector-Threshold#-43-метод-возврата-данных-выше-порога-фильтр---find_intervals_after_difference-)
   4. [ Метод возвращающий точки / координаты линий поглощения (ИНТЕРЕСНАЯ РАЛИЗАЦИЯ) ](https://github.com/SkorEgor/Detector-Threshold#-441-метод-возвращающий-точки-координаты-линий-поглощения---find_point-интересная-рализация-)
5. [ Описание пользовательского интерфейса ](https://github.com/SkorEgor/Detector-Threshold#-5-описание-пользовательского-интерфейса-)
6. [ Структура программы - Классы и их описание](https://github.com/SkorEgor/Detector-Threshold#-6-структура-программы---классы-и-их-описание-)

<br><br>
<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 1. Описание задачи и демонстрация работы </h2>
Программа для нахождения особых точек (линий поглощения) в сигнале/данных с шумом, полученных со спектрометра.
<br><br>
<div align="center">
<!--- 1.PictureControl.png -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/1_full_time.gif" >
</div>

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 2. Входные и выходные данные </h2>

**Входные данные** - Два набора точек спектра, по ~40000 штук.
1.	Набор данные без исследуемого вещества в камере. Получаем константы спектра для каждой частоты
Пример 2 точке спектра (формат файла .csv):
2. Набор данных с исследуемым веществом в камере. Сигнал получается путем сложения сигнала от вещества с константой и шумом.
Выводные данные: точки (координаты) линий поглощения вещества из спектрометра

_Пример входных данных_
```C
Index:	FREQUENCY:	AMPLITUDE:	BIAS:	GAMMA:	Pressure:	TimeMark:
000000001	022000.000	001.346120	-0.306155	7.365150e-07	0.0e+00	00:00:00.000
000000002	022000.075	001.336400	-0.303900	7.293964e-07	0.0e+00	00:00:00.156
***********************************************************
Finish
```
**Выходные данные** - точки (координаты) линий поглощения вещества из спектрометра

_Пример выходных данных_
```C
FREQUENCY:	GAMMA:
22340.650	1.0814830E-06
***********************************************************
```

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 3. Описание логической структуры - Алгоритм программы </h2>

1. Получение положительной разности, между спектрами с газом и без газа (_Получение синего графика_)
2. Вычисление и построение порогового значения, как процент от максимальной разницы (_Получение красного графика_)
<div align="center">
<!--- (2) Картинка исходных данных и разницы -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/2_picture_source_data_and_differences.jpg" >
</div>

3. Находим координаты линий поглощения
   1. Интервалы выше порога считаем участками с линией поглощения (График 1. Участок зеленый)
   2. Находим максимальное значение на участках -> ему соответствует координата линии поглощения

<div align="center">
<!--- (3) Картинка таблицы - -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/3_table_picture.jpg" >
</div>

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 4. Описание программной структуры - Используемые методы </h2>

<h3 align="left"> 4.0. Формат данных </h3>

Создаем DataFrame данных из библиотеки **Pandas**, для хранения данных из этапов обработки
```C
        self.names_data = [
            "frequency",  # Частота (ось x)
            "without_gas",  # Без шума (ось y)
            "with_gas",  # Сигнал (ось y)
        ]
        self.names_processing = [
            "difference",  # Разница
            "difference_above_threshold",  # Логический массив, где разница выше порога
            "intervals_after_difference"  # Интервалы выше порога, со значением данных с веществом
        ]
        self.data = pd.DataFrame(columns=self.names_data + self.names_processing)
```
   *Пример начальных данных*
```C
     frequency   without_gas      with_gas    difference  
...
431  22340.350  7.556487e-07  9.598057e-07         NaN  
432  22340.425  8.124049e-07  9.939411e-07         NaN  
...   
```

<h3 align="left"> 4.1. Метод нахождения разницы - data_difference </h3>

Считаем разницу значений между столбцами "with_gas" и "without_gas". Зануляя отрицательные элементы *.clip(lower=0)*

```C
        self.data["difference"] = (self.data["with_gas"] - self.data["without_gas"]).clip(lower=0)
```
   *Пример полученных данных*
```C
     frequency   without_gas      with_gas    difference  
...
49   22311.700 -2.143019e-07 -3.229686e-07  0.000000e+00   
50   22311.775 -3.437667e-07 -3.773847e-07  0.000000e+00   
...
431  22340.350  7.556487e-07  9.598057e-07  2.041570e-07   
432  22340.425  8.124049e-07  9.939411e-07  1.815362e-07   
...   
```

<h3 align="left"> 4.2. Метод возврата все данные данных, в виде(bool) - выше порога - compare_difference_and_threshold </h3>

```C
self.data["difference_above_threshold"] = self.data["difference"] >= self.difference_threshold
```
   *Пример полученных данных, для порогового значения: 2.3733604999999997e-07*
```C
     frequency   without_gas      with_gas    difference  
...
432  22340.425  8.124049e-07  9.939411e-07  1.815362e-07   
433  22340.500  7.721221e-07  1.010640e-06  2.385179e-07    
437  22340.800  7.682840e-07  1.014819e-06  2.465350e-07   
438  22340.875  7.934789e-07  9.887647e-07  1.952858e-07   
...   

     difference_above_threshold  intervals_after_difference  
432                       False                         NaN  
433                        True                         NaN    
437                        True                         NaN 
438                       False                         NaN  
   
```
<h3 align="left"> 4.3. Метод возврата данных выше порога (фильтр) - find_intervals_after_difference </h3>

Получение интервалов с предполагаемой линией поглощения. Нужно только для визуализации, таким образом закрашиваются интервалы выше порога
- self.data["difference_above_threshold"] - логический массив, первый параметр *.loc[...]*. Служит условием
- "intervals_after_difference" - Наименование нового столбца для записи. 
- self.data["with_gas"] - значение которое нужно подставить, если условие верно
```C
# Все что выше порога, приобретает значение данных с веществом, остальное None
self.data.loc[
    self.data["difference_above_threshold"], "intervals_after_difference"] = self.data["with_gas"]
```
*Пример полученных данных*
```C
     difference_above_threshold  intervals_after_difference  
432                       False                         NaN  
433                        True                1.010640e-06    
437                        True                1.014819e-06  
438                       False                         NaN  
```
<h3 align="left"> 4.4. Поиск точек (координат линий поглощения) - find_point_after_difference </h3>

- Цель получить Frame, индексов точек и их величин
```C
self.point_absorption_after_difference = pd.DataFrame()

            gamma
61   8.517156e-07
435  1.081483e-06
```
<h4 align="left"> 4.4.1. Метод возвращающий точки (координаты линий поглощения) - find_point (ИНТЕРЕСНАЯ РАЛИЗАЦИЯ) </h4>
Будем использовать метод *find_point()*, на вход которой подаем только элементы выше порога:

```C
self.data["with_gas"][  # В качестве значений - гамма с веществом
                    self.data["difference_above_threshold"]  # Оставляем элементы выше порога
...
60     7.544945e-07
61     8.517156e-07
433    1.010640e-06
434    1.054282e-06
...
```

_*_ Имеем подряд идущие интервалы выше порога, в которых нужно найти максимальное значение с индексом. Samples - вход из предыдущего примера
```C
xx = samples.groupby((samples.index != samples.index.to_series().shift() + 1)
                     .cumsum()).apply(lambda grp: (DataAndProcessing.max_index_val(grp)))
return pd.Series(xx.str[1].values, index=xx.str[0].values)
```
**Разложим на составные элементы**

* Логический массив. Значение True - если с этого индекса начинается новый интервал / предыдущий и настоящий индекс не подряд идущие. Вначале всегда True
```C
samples.index != samples.index.to_series().shift() + 1
```
Пример
```C
60     7.544945e-07
61     8.517156e-07
433    1.010640e-06
434    1.054282e-06
435    1.081483e-06

[ True False  True False False]
```
* *.cumsum([True False  True False False])* - сумма элементов вдоль заданной оси.
```C
[ True False True False False ] -> [1 1 2 2 2]
```
* samples.groupby([1 1 2 2 2]) - Сгруппирует фрейм данных (samples) сопоставляя переданный аргумент. Для применения к каждой группе метод

    Пример (*apply* - для применения функции к каждой группе; *grp* - группа):
```C
samples.groupby([1 1 2 2 2]).apply(lambda grp: print(grp))

60    7.544945e-07
61    8.517156e-07
Name: 1, dtype: float64
433    0.000001
434    0.000001
435    0.000001
Name: 2, dtype: float64
```
* Находим максимум и его индекс в каждой группе
```C
 xx = samples.groupby([1 1 2 2 2]).apply(lambda grp: (DataAndProcessing.max_index_val(grp)))
 
 1     (61, 8.517156e-07)
 2    (435, 1.081483e-06)
```
* Коллекцию записываем в виде массива Series для удобства
```C
return pd.Series(xx.str[1].values, index=xx.str[0].values)

61     8.517156e-07
435    1.081483e-06
dtype: float64
```

<br><br>
<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 5. Описание пользовательского интерфейса </h2>

<div align="center">
<!--- (4) Картинка интерфейса - -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/4_interface_picture.jpg" >
</div>

Интерфейс делится на 3 функциональные зоны:

1. меню в левой части программы для ввода данных и управления работой программы;
2. область графиков для отображения входных и расчётных данных;
3. вкладка с таблицей полученных линий поглощения и кнопкой сохранения результирующих данных.


<!---------------------------------------------------------------------------------->
<h2 align="left"> 5.1. Меню </h2>
<h3 align="left"> 5.1.1. Меню - Заголовок </h3>

Представляет собой название программы и переключатель цветовой темы

<div align="center">
<!--- (5) gif переключения цветовой схемы.jpg -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/5_color_theme_switch.png" >
</div>

Приложение поддерживает две цветовые темы: темная и светлая.

<div align="center">
<!--- (5) gif переключения цветовой схемы.gif - -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/5_color_theme_switch.gif" >
</div>

<h3 align="left"> 5.1.2. Меню - Вкладки для входных данных и параметров обработки </h3>

Вкладки для входных данных и параметров обработки располагаются под названием приложения. Имеется две вкладки: «Данные» и «Разница».
Скрыть и раскрыть каждую можно по нажатию на заголовок. Если вкладки не умещаются, появляется ползунок

<div align="center">
<!--- (6) gif скрыть и раскрыть вкладку -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/6_hide_and_reveal_tab.gif" >
</div>

<h3 align="left"> 5.1.3. Меню - Загрузка файла данных со спектрометра </h3>

<div align="center">
<!--- (7) загрузка данных и выбор диапазона -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/7_loading_data_and_selecting_range.gif" >
</div>

1. Первостепенно загружаются данные со спектрометра, для этого необходимо нажать кнопки загрузки во кладке «Данные» в полях «Без ис-следуемого вещества» и «С исследуемым веществом».
2. После нажатия появится диалоговое окно «Выбрать файл без вещества» или «Выбрать файл с веществом». В диалоге реализована фильтрация по расширению названия файлов (*.csv)
3. В случае успешной загрузки данных отобразится график и изменится иконка статуса данных справа от загрузки. В случае, если данные не загрузятся, статус не поменяется и останется красным
4. Предварительно или после загрузки данных можно выбрать диапазон отображаемых данных.
   1. все данные
   <div align="center">
   <!--- (8) все данные -->
   <img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/8_all_data.jpg" >
   </div>   <br>

   2. данные в конкретном диапазоне частот, при этом необходимо указать начало и конец загружаемого диапазона частот
   <div align="center">
   <!--- (8) диапазона данных -->
   <img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/8_data_range.jpg" >
   </div>
   <br>

<h3 align="left"> 5.1.4. Меню - Ввод параметров </h3>

Ввод параметров обработки осуществляется в соответствии с описанным раннее алгоритмом работы.

В случае неверного ввода параметра (введена буква вместо цифры, введено положительное число вместо отрицательного, введено дробное число вместо целого и т.д.), программа сообщит об ошибке через соответствующий индикатор справа.

<div align="center">
<!--- (9) индикации ошибки -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/9_error_indications.png" >
</div>

Если ошибка не устранена и идет запуск вычисления, программа остановится и появится окно ошибки 

<div align="center">
<!--- (10) Окно ошибки -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/10_windows_error.jpg" >
</div>

Последовательная обработка всех ошибок

<div align="center">
<!--- (11) Последовательная обработка всех ошибок -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/11_sequential_processing_all_errors.gif" >
</div>

<h3 align="left"> 5.1.5. Кнопки управления в нижней части меню  </h3>

В нижней части меню расположены две кнопки: «Таблица» и «Вычислить».

<div align="center">
<!--- (12) кнопки_таблица_и_вычислить -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/12_buttons_table_and_calculate.jpg" >
</div>

- Кнопка «Таблица» скрывает и раскрывает боковую панель с таблицей линий поглощения 

<div align="center">
<!--- 13_раскрытие_и_сворачивание_таблицы -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/13_expanding_and_collapse_table.gif" >
</div>

- Кнопка «Вычислить» проверяет правильность введенных данных и проводит вычисление. Обязательной является предварительная загрузка данных со спектрометра. 

<div align="center">
<!--- 14_раскрытие_и_сворачивание_таблицы -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/14_button_calculate.gif" >
</div>

<br><br>
<!---------------------------------------------------------------------------------->
<h2 align="left"> 5.2. Область графиков  </h2>
<h3 align="left"> 5.2.1. Режимы области построения графиков </h3>

Область построения графиков предназначена для графического отображения данных, загруженных в программу или полученных в ходе вычислений. Одновременно на экране программы показываются один график или два графика.

<div align="center">
<!--- 15_one_or_two_graphics -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/15_one_or_two_graphics.gif" >
</div>

Сворачивание нижнего графика происходит по левой кнопке (стрелки вниз), нижней панели инструментов
<h3 align="left"> 5.2.2. Инструменты для работы с графиком - toolbar  </h3>
Каждый график имеет стандартный toolbar matplotlib, с кнопками
- Кнопки начальное, предыдущее и следующее положение границ окна просмотра или области приближения
- Кнопка панорамирования или масштабирования 
- Кнопка масштабирование в прямоугольную область (лупа)
- Кнопка настройки параметров отображения
- Кнопка сохранения в файл (флоппи-диск)

<div align="center">
<!--- 16_toolbar -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/16_toolbar.gif" >
</div>

<!---------------------------------------------------------------------------------->
<h2 align="left"> 5.3. Вкладка полученных линий поглощения   </h2>
<h3 align="left"> 5.3.1. Таблица </h3>

Информация результатов обработки представлена в таблице. 

Каждая строка — это точка линии поглощения, указаны: частота, гамма (максимум), статус.

Статус имеет два значения: крест и галочка (Введен для удобства):

- линии полученные в результате обработки получают статус «крест»;
- предполагается, что линии проверенные вручную являющиеся правильными для них следует устанавливать статус «галочка», вручную;
- линии поглощения со статусом «галочка» будут сохранены в файл.

<h3 align="left"> 5.3.2. Выбор отображаемых данных в таблице </h3>

При работе с большими массивами данных алгоритм может находить 800 линий и только 80 из них будут иметь статус «галочка». Для удобства просмотра конкретной категории над таблицей есть поле «Отображаемые данные», в котором можно выбрать, какие данные отображать в таблице:

I.все, оранжевый прочерк;

II.только «галочка»;

III.только «крест»;

<h3 align="left"> 5.3.3. Масштабирование графика по выбранной линии поглощения </h3>

Программа поддерживает отображение конкретного участка линии поглощения из таблицы. При нажатии строки

<h3 align="left"> 5.3.4. Кнопка «Сохранить в файл» </h3>

При нажатии вызывает диалоговое окно для выбора пути и имени файла с данными, записываются линии со статусом «галочка». 

<h3 align="left"> 5.3.5. Демонстрация работы со вкладкой таблица </h3>

<div align="center">
<!--- 17_work_with_table -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/Detector-Difference/17_work_with_table.gif" >
</div>

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 6. Структура программы - Классы и их описание </h2>

1. main.py - Запускает окно программы класса GuiProgram
2. gui_logic - class GuiProgram(Ui_Dialog) - контроллер интерфейса - обрабатывает нажатия и ошибки, вызывает функции обработки
   1. Содержит объект интерфейса, наследник Ui_Dialog
   2. Содержит два объекта графики Graph
   3. Содержит объект данных и их обработки DataAndProcessing
3. gui.ui -> gui.py - class Ui_Dialog(object) - класс диалога и объектов на нем. Автоматически сгенерирован Qt Designer
4. res.qrc -> res_rc.py - ресурсы проекта, картинки, иконки, значки
5. graph.py - class Graph - На объектах ui (widget и его layout) создает объекты matplotlib (axis, figure, canvas, toolbar) для отображения данных через методы класса  Drawer
6. drawer.py - class Drawer - На объектах Graph, строит графики через статичные методы. Имея метода - определяет вид графика; Переданный объект Graph - место отрисовки; Переданный объект DataAndProcessing - данные для отрисовки; 