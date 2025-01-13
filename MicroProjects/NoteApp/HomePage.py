# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        # Set window to fullscreen
        MainWindow.showMaximized()
        MainWindow.setWindowTitle("CloudAlgoSim")
        MainWindow.setWindowIcon(QtGui.QIcon("../download.jpg"))  # Replace with your icon file
        
        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a vertical layout
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        # Image/Logo
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setPixmap(QtGui.QPixmap("../download.jpg"))  # Replace with your image
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.layout.addWidget(self.label)
        
        # Application name
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText("Cloud Algo Simulator")
        self.label_2.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.layout.addWidget(self.label_2)
        
        # Progress bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setValue(0)  # Start at 0
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.layout.addWidget(self.progressBar)
        
        # Set the central widget layout
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        
        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        
        # Menus
        self.menuMenu = QtWidgets.QMenu("File", self.menubar)
        self.menuSimulation = QtWidgets.QMenu("Simulation", self.menubar)
        self.menuView = QtWidgets.QMenu("View", self.menubar)
        self.menuSettings = QtWidgets.QMenu("Settings", self.menubar)
        self.menuHelp = QtWidgets.QMenu("Help", self.menubar)
        
        self.menubar.addMenu(self.menuMenu)
        self.menubar.addMenu(self.menuSimulation)
        self.menubar.addMenu(self.menuView)
        self.menubar.addMenu(self.menuSettings)
        self.menubar.addMenu(self.menuHelp)
        
        # Actions
        self.actionOpen = QtWidgets.QAction("Open", MainWindow)
        self.actionSave = QtWidgets.QAction("Save", MainWindow)
        self.actionExit = QtWidgets.QAction("Exit", MainWindow)
        self.actionStart = QtWidgets.QAction("Start", MainWindow)
        self.actionStop = QtWidgets.QAction("Stop", MainWindow)
        self.actionResume = QtWidgets.QAction("Resume", MainWindow)
        
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionExit)
        self.menuSimulation.addAction(self.actionStart)
        self.menuSimulation.addAction(self.actionStop)
        self.menuSimulation.addAction(self.actionResume)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Create main window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # Update progress bar example
    for i in range(101):
        QtCore.QThread.msleep(100)
        ui.progressBar.setValue(i)
        app.processEvents()
    
    sys.exit(app.exec_())
