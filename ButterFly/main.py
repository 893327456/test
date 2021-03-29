import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = test.Ui_MainWindow(myMainWindow)
    myMainWindow.show()
    sys.exit(app.exec_())
