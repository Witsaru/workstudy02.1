import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("ui")

import main_ui

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