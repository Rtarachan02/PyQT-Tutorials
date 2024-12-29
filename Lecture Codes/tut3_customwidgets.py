import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QWidget,QLabel

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Widgets Learning")

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=CustomWidget()
    window.show()
    sys.exit(app.exec())
