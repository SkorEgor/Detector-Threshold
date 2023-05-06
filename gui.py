# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(713, 573)
        Dialog.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.layout_dialog = QtWidgets.QHBoxLayout(Dialog)
        self.layout_dialog.setContentsMargins(0, 0, 0, 0)
        self.layout_dialog.setSpacing(0)
        self.layout_dialog.setObjectName("layout_dialog")
        self.widget_menu = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_menu.setStyleSheet("")
        self.widget_menu.setObjectName("widget_menu")
        self.layout_menu = QtWidgets.QVBoxLayout(self.widget_menu)
        self.layout_menu.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout_menu.setContentsMargins(0, 0, 0, 0)
        self.layout_menu.setSpacing(0)
        self.layout_menu.setObjectName("layout_menu")
        self.widget_menu_title = QtWidgets.QWidget(self.widget_menu)
        self.widget_menu_title.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_menu_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_menu_title.setStyleSheet("background-color: rgb(91, 107, 153);")
        self.widget_menu_title.setObjectName("widget_menu_title")
        self.layout_menu.addWidget(self.widget_menu_title)
        self.widget_menu_body = QtWidgets.QWidget(self.widget_menu)
        self.widget_menu_body.setStyleSheet("background-color: rgb(98, 114, 165);")
        self.widget_menu_body.setObjectName("widget_menu_body")
        self.layout_menu_body = QtWidgets.QVBoxLayout(self.widget_menu_body)
        self.layout_menu_body.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layout_menu_body.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_body.setSpacing(0)
        self.layout_menu_body.setObjectName("layout_menu_body")
        self.scrollArea_menu_body = QtWidgets.QScrollArea(self.widget_menu_body)
        self.scrollArea_menu_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_menu_body.setLineWidth(1)
        self.scrollArea_menu_body.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_menu_body.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_menu_body.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_menu_body.setWidgetResizable(True)
        self.scrollArea_menu_body.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_menu_body.setObjectName("scrollArea_menu_body")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 200, 523))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Layout_scroll_menu = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.Layout_scroll_menu.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Layout_scroll_menu.setContentsMargins(0, 0, 0, 0)
        self.Layout_scroll_menu.setSpacing(0)
        self.Layout_scroll_menu.setObjectName("Layout_scroll_menu")
        self.widget_data = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_data.sizePolicy().hasHeightForWidth())
        self.widget_data.setSizePolicy(sizePolicy)
        self.widget_data.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_data.setObjectName("widget_data")
        self.layout_menu_data = QtWidgets.QVBoxLayout(self.widget_data)
        self.layout_menu_data.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_menu_data.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_data.setSpacing(0)
        self.layout_menu_data.setObjectName("layout_menu_data")
        self.widget_data_header = QtWidgets.QWidget(self.widget_data)
        self.widget_data_header.setStyleSheet("")
        self.widget_data_header.setObjectName("widget_data_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_data_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_data_header = QtWidgets.QPushButton(self.widget_data_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_data_header.sizePolicy().hasHeightForWidth())
        self.pushButton_data_header.setSizePolicy(sizePolicy)
        self.pushButton_data_header.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_data_header.setFont(font)
        self.pushButton_data_header.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_data_header.setAccessibleDescription("")
        self.pushButton_data_header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_data_header.setAutoFillBackground(False)
        self.pushButton_data_header.setStyleSheet("/*Стандартное состояние для кнопки*/\n"
"QPushButton {\n"
"    background-color: rgb(98, 114, 165);/* задает цвет фона */\n"
"    display: inline-block;                            /* пределяет, будет ли элемент обрабатываться как блочный или встроенный элемент */\n"
"    border: 1px solid rgb(52, 59, 72);        /* задает границу элемента */\n"
"\n"
"\n"
"    /* задает иконку */\n"
"    background-image: url(:/menu_titles/resource/menu_titles/menu_data_white_36dp.svg);\n"
"    background-position: left center;                            /* выравнивание иконки */\n"
"    background-repeat: no-repeat;                                /* повторять иконку */\n"
"} \n"
"\n"
"/* срабатывает, когда пользователь наводит на элемент мышью */\n"
"QPushButton:hover {\n"
"    background-color: rgb(86, 98, 138);            /* задаем цвет фона */\n"
"    border: none;                                                /* без границ */\n"
"    border-left:4px solid rgb(171, 125, 171);    /* С правой красной раницей */\n"
"}\n"
"\n"
"\n"
"/* срабатывает, при нажатии*/\n"
"QPushButton:pressed      {\n"
"    background-color: rgb(189, 146, 251);        /* задаем цвет фона */\n"
"    border: none;                                                /* без границ */\n"
"}")
        self.pushButton_data_header.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_data_header.setCheckable(True)
        self.pushButton_data_header.setChecked(False)
        self.pushButton_data_header.setAutoRepeat(False)
        self.pushButton_data_header.setAutoExclusive(False)
        self.pushButton_data_header.setDefault(False)
        self.pushButton_data_header.setFlat(False)
        self.pushButton_data_header.setObjectName("pushButton_data_header")
        self.horizontalLayout.addWidget(self.pushButton_data_header)
        self.layout_menu_data.addWidget(self.widget_data_header)
        self.widget_data_body = QtWidgets.QWidget(self.widget_data)
        self.widget_data_body.setStyleSheet("background-color: rgb(92, 105, 150);")
        self.widget_data_body.setObjectName("widget_data_body")
        self.layout_data_body = QtWidgets.QVBoxLayout(self.widget_data_body)
        self.layout_data_body.setContentsMargins(5, 0, 5, 10)
        self.layout_data_body.setSpacing(0)
        self.layout_data_body.setObjectName("layout_data_body")
        self.groupBox_no_gas = QtWidgets.QGroupBox(self.widget_data_body)
        self.groupBox_no_gas.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_no_gas.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_no_gas.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_no_gas.setFont(font)
        self.groupBox_no_gas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_no_gas.setMouseTracking(False)
        self.groupBox_no_gas.setTabletTracking(False)
        self.groupBox_no_gas.setStyleSheet("QGroupBox{\n"
"    color:rgb(215, 132, 191);    /* задает цвет шрифта */\n"
"    font-size:10pt;                    /* задает размер шрифта */\n"
"}")
        self.groupBox_no_gas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_no_gas.setFlat(True)
        self.groupBox_no_gas.setCheckable(False)
        self.groupBox_no_gas.setObjectName("groupBox_no_gas")
        self.layout_no_gas = QtWidgets.QHBoxLayout(self.groupBox_no_gas)
        self.layout_no_gas.setContentsMargins(5, 0, 5, 0)
        self.layout_no_gas.setSpacing(0)
        self.layout_no_gas.setObjectName("layout_no_gas")
        self.label_file_name_no_gas = QtWidgets.QLabel(self.groupBox_no_gas)
        self.label_file_name_no_gas.setTextFormat(QtCore.Qt.AutoText)
        self.label_file_name_no_gas.setScaledContents(False)
        self.label_file_name_no_gas.setObjectName("label_file_name_no_gas")
        self.layout_no_gas.addWidget(self.label_file_name_no_gas)
        self.pushButton_reading_file_no_gas = QtWidgets.QPushButton(self.groupBox_no_gas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reading_file_no_gas.sizePolicy().hasHeightForWidth())
        self.pushButton_reading_file_no_gas.setSizePolicy(sizePolicy)
        self.pushButton_reading_file_no_gas.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_reading_file_no_gas.setStyleSheet("/*Стандартное состояние для кнопки*/\n"
"QPushButton {\n"
"    background-color: rgb(98, 114, 165);    /* задает цвет фона */\n"
"    border: none;                                            /* без границ */\n"
"\n"
"        /* задает иконку */\n"
"    background-image: url(:/shared/resource/file_download_white_24dp.svg);\n"
"    background-position: center;                                                            /* выравнивание иконки */\n"
"    background-repeat: no-repeat;                                                        /* повторять иконку */\n"
"} \n"
"\n"
"/* срабатывает, когда пользователь наводит на элемент мышью */\n"
"QPushButton:hover {\n"
"    background-color: rgb(86, 98, 138);        /* задает цвет фона */\n"
"}\n"
"\n"
"/* срабатывает, при нажатии*/\n"
"QPushButton:pressed      {\n"
"    background-color: rgb(215, 132, 191);    /* задает цвет фона */\n"
"}\n"
"\n"
"")
        self.pushButton_reading_file_no_gas.setText("")
        self.pushButton_reading_file_no_gas.setObjectName("pushButton_reading_file_no_gas")
        self.layout_no_gas.addWidget(self.pushButton_reading_file_no_gas)
        self.checkBox_download_no_gas = QtWidgets.QCheckBox(self.groupBox_no_gas)
        self.checkBox_download_no_gas.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_download_no_gas.sizePolicy().hasHeightForWidth())
        self.checkBox_download_no_gas.setSizePolicy(sizePolicy)
        self.checkBox_download_no_gas.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_download_no_gas.setStyleSheet("/* Стандартное состояние*/\n"
"QCheckBox{\n"
"    padding-left: 8px;        /* Отступ слева */\n"
"    padding-right: -8px;    /* Отступ справа */\n"
"}\n"
"\n"
"/* Состояние - не выбран*/\n"
"QCheckBox::indicator:unchecked {\n"
"    /* Выбор картинки*/\n"
"    image: url(:/checkbox_status_success/resource/checkbox_status_success/check_error_purple_24dp.svg);\n"
"}\n"
"\n"
"/* Состояние -  выбран*/\n"
"QCheckBox::indicator:checked {\n"
"    /* Выбор картинки*/\n"
"    \n"
"    image: url(:/checkbox_status_success/resource/checkbox_status_success/check_ok_grean_24dp.svg);\n"
"}")
        self.checkBox_download_no_gas.setText("")
        self.checkBox_download_no_gas.setChecked(False)
        self.checkBox_download_no_gas.setTristate(False)
        self.checkBox_download_no_gas.setObjectName("checkBox_download_no_gas")
        self.layout_no_gas.addWidget(self.checkBox_download_no_gas)
        self.label_status_no_gas = QtWidgets.QLabel(self.groupBox_no_gas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status_no_gas.sizePolicy().hasHeightForWidth())
        self.label_status_no_gas.setSizePolicy(sizePolicy)
        self.label_status_no_gas.setText("")
        self.label_status_no_gas.setObjectName("label_status_no_gas")
        self.layout_no_gas.addWidget(self.label_status_no_gas)
        self.layout_data_body.addWidget(self.groupBox_no_gas)
        self.groupBox_with_gas = QtWidgets.QGroupBox(self.widget_data_body)
        self.groupBox_with_gas.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_with_gas.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_with_gas.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_with_gas.setFont(font)
        self.groupBox_with_gas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_with_gas.setMouseTracking(False)
        self.groupBox_with_gas.setTabletTracking(False)
        self.groupBox_with_gas.setStyleSheet("QGroupBox{\n"
"    color:rgb(215, 132, 191);    /* задает цвет шрифта */\n"
"    font-size:10pt;                    /* задает размер шрифта */\n"
"}")
        self.groupBox_with_gas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_with_gas.setFlat(True)
        self.groupBox_with_gas.setCheckable(False)
        self.groupBox_with_gas.setObjectName("groupBox_with_gas")
        self.layout_with_gas = QtWidgets.QHBoxLayout(self.groupBox_with_gas)
        self.layout_with_gas.setContentsMargins(5, 0, 5, 0)
        self.layout_with_gas.setSpacing(0)
        self.layout_with_gas.setObjectName("layout_with_gas")
        self.label_file_name_with_gas = QtWidgets.QLabel(self.groupBox_with_gas)
        self.label_file_name_with_gas.setTextFormat(QtCore.Qt.AutoText)
        self.label_file_name_with_gas.setScaledContents(False)
        self.label_file_name_with_gas.setObjectName("label_file_name_with_gas")
        self.layout_with_gas.addWidget(self.label_file_name_with_gas)
        self.pushButton_reading_file_with_gas = QtWidgets.QPushButton(self.groupBox_with_gas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reading_file_with_gas.sizePolicy().hasHeightForWidth())
        self.pushButton_reading_file_with_gas.setSizePolicy(sizePolicy)
        self.pushButton_reading_file_with_gas.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_reading_file_with_gas.setStyleSheet("/*Стандартное состояние для кнопки*/\n"
"QPushButton {\n"
"    background-color: rgb(98, 114, 165);    /* задает цвет фона */\n"
"    border: none;                                            /* без границ */\n"
"\n"
"        /* задает иконку */\n"
"    background-image: url(:/shared/resource/file_download_white_24dp.svg);\n"
"    background-position: center;                                                            /* выравнивание иконки */\n"
"    background-repeat: no-repeat;                                                        /* повторять иконку */\n"
"} \n"
"\n"
"/* срабатывает, когда пользователь наводит на элемент мышью */\n"
"QPushButton:hover {\n"
"    background-color: rgb(86, 98, 138);        /* задает цвет фона */\n"
"}\n"
"\n"
"/* срабатывает, при нажатии*/\n"
"QPushButton:pressed      {\n"
"    background-color: rgb(215, 132, 191);    /* задает цвет фона */\n"
"}\n"
"\n"
"")
        self.pushButton_reading_file_with_gas.setText("")
        self.pushButton_reading_file_with_gas.setObjectName("pushButton_reading_file_with_gas")
        self.layout_with_gas.addWidget(self.pushButton_reading_file_with_gas)
        self.checkBox_download_with_gas = QtWidgets.QCheckBox(self.groupBox_with_gas)
        self.checkBox_download_with_gas.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_download_with_gas.sizePolicy().hasHeightForWidth())
        self.checkBox_download_with_gas.setSizePolicy(sizePolicy)
        self.checkBox_download_with_gas.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_download_with_gas.setStyleSheet("/* Стандартное состояние*/\n"
"QCheckBox{\n"
"    padding-left: 8px;        /* Отступ слева */\n"
"    padding-right: -8px;    /* Отступ справа */\n"
"}\n"
"\n"
"/* Состояние - не выбран*/\n"
"QCheckBox::indicator:unchecked {\n"
"    /* Выбор картинки*/\n"
"    image: url(:/checkbox_status_success/resource/checkbox_status_success/check_error_purple_24dp.svg);\n"
"}\n"
"\n"
"/* Состояние -  выбран*/\n"
"QCheckBox::indicator:checked {\n"
"    /* Выбор картинки*/\n"
"    \n"
"    image: url(:/checkbox_status_success/resource/checkbox_status_success/check_ok_grean_24dp.svg);\n"
"}")
        self.checkBox_download_with_gas.setText("")
        self.checkBox_download_with_gas.setChecked(False)
        self.checkBox_download_with_gas.setTristate(False)
        self.checkBox_download_with_gas.setObjectName("checkBox_download_with_gas")
        self.layout_with_gas.addWidget(self.checkBox_download_with_gas)
        self.label_status_witth_gas = QtWidgets.QLabel(self.groupBox_with_gas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status_witth_gas.sizePolicy().hasHeightForWidth())
        self.label_status_witth_gas.setSizePolicy(sizePolicy)
        self.label_status_witth_gas.setText("")
        self.label_status_witth_gas.setObjectName("label_status_witth_gas")
        self.layout_with_gas.addWidget(self.label_status_witth_gas)
        self.layout_data_body.addWidget(self.groupBox_with_gas)
        self.layout_menu_data.addWidget(self.widget_data_body)
        self.Layout_scroll_menu.addWidget(self.widget_data)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Layout_scroll_menu.addItem(spacerItem)
        self.scrollArea_menu_body.setWidget(self.scrollAreaWidgetContents)
        self.layout_menu_body.addWidget(self.scrollArea_menu_body)
        self.layout_menu.addWidget(self.widget_menu_body)
        self.layout_dialog.addWidget(self.widget_menu)
        self.widget_main = QtWidgets.QWidget(Dialog)
        self.widget_main.setStyleSheet("")
        self.widget_main.setObjectName("widget_main")
        self.layout_main = QtWidgets.QVBoxLayout(self.widget_main)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(0)
        self.layout_main.setObjectName("layout_main")
        self.widget_main_header = QtWidgets.QWidget(self.widget_main)
        self.widget_main_header.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_main_header.setStyleSheet("background-color:rgb(98, 114, 165);")
        self.widget_main_header.setObjectName("widget_main_header")
        self.layout_main.addWidget(self.widget_main_header)
        self.widget_main_body = QtWidgets.QWidget(self.widget_main)
        self.widget_main_body.setObjectName("widget_main_body")
        self.layout_main_body = QtWidgets.QVBoxLayout(self.widget_main_body)
        self.layout_main_body.setContentsMargins(0, 0, 0, 0)
        self.layout_main_body.setSpacing(0)
        self.layout_main_body.setObjectName("layout_main_body")
        self.widget_plotting = QtWidgets.QWidget(self.widget_main_body)
        self.widget_plotting.setObjectName("widget_plotting")
        self.plotLayout = QtWidgets.QVBoxLayout(self.widget_plotting)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setSpacing(0)
        self.plotLayout.setObjectName("plotLayout")
        self.layout_main_body.addWidget(self.widget_plotting)
        self.layout_main.addWidget(self.widget_main_body)
        self.layout_dialog.addWidget(self.widget_main)

        self.retranslateUi(Dialog)
        self.pushButton_data_header.clicked['bool'].connect(self.widget_data_body.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_data_header.setText(_translate("Dialog", "Данные"))
        self.groupBox_no_gas.setTitle(_translate("Dialog", "Без исследуемого вещества"))
        self.label_file_name_no_gas.setText(_translate("Dialog", "Нет файла"))
        self.groupBox_with_gas.setTitle(_translate("Dialog", "С исследуемым веществом"))
        self.label_file_name_with_gas.setText(_translate("Dialog", "Нет файла"))
import res_rc
