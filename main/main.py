import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui import main_ui

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main_ui.Ui_MainWindow()
    # plot_ui = ppt.Ui_Plot_process_time()
    # plot_ui.activatePlotprocess()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()