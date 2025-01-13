import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("My Portofolio")
        widget=QPushButton("Click Me")
        widget.clicked.connect(lambda:[  print(x) for x in range(10)])

if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec())