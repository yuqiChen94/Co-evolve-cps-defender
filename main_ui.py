import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import testui

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = testui.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())