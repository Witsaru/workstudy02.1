import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.addButton = QPushButton('เพิ่ม Line Edit')
        self.addButton.clicked.connect(self.addLineEdit)

        self.removeButton = QPushButton('ลบ Line Edit ล่าสุด')
        self.removeButton.clicked.connect(self.removeLineEdit)

        self.confirmButton = QPushButton('ตกลง')
        self.confirmButton.clicked.connect(self.confirmData)

        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.removeButton)
        self.layout.addWidget(self.confirmButton)

        self.setLayout(self.layout)

        self.lineEdits = []

    def addLineEdit(self):
        lineEdit = QLineEdit()
        self.lineEdits.append(lineEdit)
        self.layout.addWidget(lineEdit)

    def removeLineEdit(self):
        if self.lineEdits:
            lineEdit = self.lineEdits.pop()
            lineEdit.deleteLater()
            self.adjustSize()

    def confirmData(self):
        data = []
        for lineEdit in self.lineEdits:
            text = lineEdit.text()
            data.append(text)
        df = pd.DataFrame(data)
        print(df)  # แสดง DataFrame ใน Output ของ Python เพื่อตรวจสอบ

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())