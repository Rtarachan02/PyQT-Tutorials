import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QLabel,QWidget,QPushButton,QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Some major classes")
        # create a label
        label=QLabel("Hello PyQt")

        # create a push button
        button=QPushButton("Click Me")
        button.clicked.connect(self.onButtonClick)

        # create a vertical layout
        layout=QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        # create a central widget and set the layout
        central_widget=QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def onButtonClick(self):
        print("Button Clicked..")



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())