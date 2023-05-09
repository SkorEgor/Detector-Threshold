import sys
from PyQt5 import QtWidgets
import ctypes

from gui_logic import GuiProgram

if __name__ == '__main__':
    # Вызов Windows из Python, чтобы явно указать Windows, какой правильный AppUserModelID
    # используется для этого процесса - отображает иконку в панели задач.
    my_app_id = 'company.my-product.subproject.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    program = GuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())
