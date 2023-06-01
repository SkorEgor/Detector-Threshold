# Класс темной и светлой темы приложения
class ColorTheme:
    light_style_sheet = """
   QWidget{
	background-color: rgb(230, 230, 230);
	color:rgb(33, 37, 43);
	font-size: 10pt;
}
/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
 QScrollBar {
border: none;												/* без границ */
	border-right:5px solid rgb(211, 211, 211);	/* С правой красной раницей */

 }
 QScrollBar:vertical {
	border: none;
    background:rgb(230, 230, 230);
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
 }

/* Ползунок */
 QScrollBar::handle:vertical {	
	background:rgb(255, 255, 255);
    min-height: 25px;
	border-radius: 4px
 }
/*Нижняя стрелка*/
 QScrollBar::add-line:vertical {
     border: none;
     height: 20px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }
/*Верхняя стрелка*/
 QScrollBar::sub-line:vertical {
	border: none;
     height: 20px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }
/* Цвета нижних и верхних стрелок */
 QScrollBar::up-arrow:vertical{
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     background: rgb(255, 255, 255);
 }
QScrollBar::down-arrow:vertical{
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     background: rgb(255, 255, 255);
}

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
 }
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
RadioButton */
QRadioButton::indicator {
    border: 3px solid rgb(179, 179, 179);
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: rgb(255, 255, 255);
}
QRadioButton::indicator:hover {
    border: 3px solid rgb(179, 179, 179);
}
QRadioButton::indicator:checked {
    background: 3px solid rgb(140, 140, 140);
    border: 3px solid  rgb(179, 179, 179);
}
/* срабатывает, когда пользователь наводит на элемент мышью */
QRadioButton:hover {
	background-color:rgb(212, 212, 212);			/* задаем цвет фона */
}
/* срабатывает, при нажатии*/
QRadioButton:pressed      {
	background-color:rgb(130, 130, 130);		/* задаем цвет фона */
	color:  rgb(0, 0, 0);
	border: none;												/* без границ */
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QCheckBox */
/* Стандартное состояние*/
QCheckBox{
	padding-left: 8px;		/* Отступ слева */
	padding-right: -8px;	/* Отступ справа */
}

/* Состояние - не выбран*/
QCheckBox::indicator:unchecked {
	/* Выбор картинки*/
	image: url(:/checkbox_status_success/resource/checkbox_status_success/check_error_red_24dp.svg)
}

/* Состояние -  выбран*/
QCheckBox::indicator:checked {
	/* Выбор картинки*/
	image: url(:/checkbox_status_success/resource/checkbox_status_success/check_ok_grean_24dp.svg);
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QPushButton */
/*Стандартное состояние для кнопки*/
QPushButton {
	font-size: 12pt;
	background-color:rgb(212, 212, 212);/* задает цвет фона */
	display: inline-block;							/* пределяет, будет ли элемент обрабатываться как блочный или встроенный элемент */
	border: none;

	/* задает иконку */
	background-position: left center;							/* выравнивание иконки */
	background-repeat: no-repeat;								/* повторять иконку */
} 

/* срабатывает, когда пользователь наводит на элемент мышью */
QPushButton:hover {
	background-color:rgb(212, 212, 212);			/* задаем цвет фона */
	border: none;												/* без границ */
	border-left:4px solid rgb(189, 189, 189);	/* С правой красной раницей */
}


/* срабатывает, при нажатии*/
QPushButton:pressed      {
	background-color:rgb(130, 130, 130);		/* задаем цвет фона */
	color: rgb(255, 255, 255);
	border: none;												/* без границ */
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QLineEdit */
/* Стиль по умолчанию */
QLineEdit:enabled{
	background-color:rgb(230, 230, 230); /* Устанавливаем цвет заливки */
	border: 1px solid rgb(255, 255, 255); 
}

/* Если поле отключено */
QLineEdit:disabled {
	background-color:  rgb(212, 212, 212); /* Устанавливаем цвет заливки */
	border: 1px solid rgb(255, 255, 255); 
	color: rgb(167, 167, 167);
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QGroupBox */
QGroupBox{
	color:rgb(70, 70, 70);	/* задает цвет шрифта */
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QTableWidget */
QTableWidget {	
	gridline-color: rgb(160, 160, 160);
	border-top: 2px solid rgb(212, 212, 212);
	border-bottom: 2px solid  rgb(212, 212, 212);
}
QTableWidget::item:selected{
	background-color: rgb(72, 81, 94);
	background-color: rgb(182, 182, 182);
}
QHeaderView { qproperty-defaultAlignment: AlignCenter; }
/*Цвет верхнего и левого поля*/
QHeaderView::section{
background-color: rgb(212, 212, 212);
    border-style: none;
border: 1px solid rgb(160, 160, 160);
}
/*Кнопка в верхнем левом углу*/
QTableCornerButton::section {background-color:rgb(212, 212, 212); }

/* ///////////////////////////////////////////////////////////////////////////////////////////////// */

"""
    dark_style_sheet = """
   QWidget{
	background-color: rgb(33, 37, 43);
	color: rgb(208, 208, 208);
	font-size: 10pt;
}
/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
 QScrollBar {
border: none;												/* без границ */
	border-right:5px solid rgb(211, 211, 211);;	/* С правой красной раницей */
 }
 QScrollBar:vertical {
	border: none;
    background: rgb(52, 59, 72);
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
 }

/* Ползунок */
 QScrollBar::handle:vertical {	
	background:rgb(255, 255, 255);
    min-height: 25px;
	border-radius: 4px
 }
/*Нижняя стрелка*/
 QScrollBar::add-line:vertical {
     border: none;
    background: rgb(55, 63, 77);
     height: 20px;

     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }
/*Верхняя стрелка*/
 QScrollBar::sub-line:vertical {
	border: none;
    background: rgb(55, 63, 77);
     height: 20px;

     subcontrol-position: top;
     subcontrol-origin: margin;
 }
/* Цвета нижних и верхних стрелок */
 QScrollBar::up-arrow:vertical{
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     background: rgb(255, 255, 255);
 }
QScrollBar::down-arrow:vertical{
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     background: rgb(255, 255, 255);
}

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
 }
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
RadioButton */
QRadioButton::indicator {
    border: 3px solid rgb(52, 59, 72);
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: rgb(44, 49, 60);
}
QRadioButton::indicator:hover {
    border: 3px solid rgb(58, 66, 81);
}
QRadioButton::indicator:checked {
    background: 3px solid rgb(255, 255, 255);
	border: 3px solid rgb(52, 59, 72);	
}
/* срабатывает, когда пользователь наводит на элемент мышью */
QRadioButton:hover {
	background-color:rgb(40, 44, 52);			/* задаем цвет фона */
}
/* срабатывает, при нажатии*/
QRadioButton:pressed      {
	background-color:rgb(170, 170, 170);		/* задаем цвет фона */
	color:  rgb(0, 0, 0);
	border: none;												/* без границ */
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QCheckBox */
/* Стандартное состояние*/
QCheckBox{
	padding-left: 8px;		/* Отступ слева */
	padding-right: -8px;	/* Отступ справа */
}

/* Состояние - не выбран*/
QCheckBox::indicator:unchecked {
	/* Выбор картинки*/
	image: url(:/checkbox_status_success/resource/checkbox_status_success/check_error_red_24dp.svg)
}

/* Состояние -  выбран*/
QCheckBox::indicator:checked {
	/* Выбор картинки*/
	image: url(:/checkbox_status_success/resource/checkbox_status_success/check_ok_grean_24dp.svg);
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QPushButton */
/*Стандартное состояние для кнопки*/
QPushButton {
	font-size: 12pt;
	background-color:rgb(37, 41, 48);/* задает цвет фона */
	display: inline-block;							/* пределяет, будет ли элемент обрабатываться как блочный или встроенный элемент */
	border: 1px solid rgb(52, 59, 72);		/* задает границу элемента */

	/* задает иконку */
	background-position: left center;							/* выравнивание иконки */
	background-repeat: no-repeat;								/* повторять иконку */
} 

/* срабатывает, когда пользователь наводит на элемент мышью */
QPushButton:hover {
	background-color:rgb(40, 44, 52);			/* задаем цвет фона */
	border: none;												/* без границ */
	border-left:4px solid rgb(208, 208, 208);	/* С правой красной раницей */
}


/* срабатывает, при нажатии*/
QPushButton:pressed      {
	background-color:rgb(170, 170, 170);		/* задаем цвет фона */
	color: rgb(181, 181, 181);
	border: none;												/* без границ */
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QLineEdit */
/* Стиль по умолчанию */
QLineEdit:enabled{
	background-color:rgb(44, 49, 58); /* Устанавливаем цвет заливки */
	border: 1px solid rgb(255, 255, 255); 
}

/* Если поле отключено */
QLineEdit:disabled {
	background-color:  rgba(67, 74, 88, 0); /* Устанавливаем цвет заливки */
	border: 1px solid rgb(255, 255, 255); 
	color: rgb(67, 74, 88);
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QGroupBox */
QGroupBox{
	color:rgb(255, 255, 255);	/* задает цвет шрифта */
}
/* ///////////////////////////////////////////////////////////////////////////////////////////////// */
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QTableWidget */

QTableWidget {	
	gridline-color: rgb(136, 136, 136);
	border-top: 1px solid rgb(54, 60, 74);
	border-bottom: 1px solid  rgb(54, 60, 74);
}
QTableWidget::item:selected{
	background-color: rgb(72, 81, 94);
}
QHeaderView { qproperty-defaultAlignment: AlignCenter; }
/*Цвет верхнего и левого поля*/
QHeaderView::section{
	background-color:rgb(37, 41, 48);
    border-style: none;
border: 1px solid rgb(136, 136, 136);
}
/*Кнопка в верхнем левом углу*/
QTableCornerButton::section {background-color:rgb(33, 37, 43); }

"""