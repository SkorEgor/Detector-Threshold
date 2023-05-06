from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Dialog


class GuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)              # Initialize Window
        self.setupUi(dialog)                  # Set up the UI

