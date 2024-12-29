import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # initialize the UIelements
        self.setWindowTitle("Python Major Classes Demo")
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
        
