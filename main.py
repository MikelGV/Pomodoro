import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Pomodoro App")
        widget = QWidget()
        layout = QGridLayout()
        # ui components
        pomodoro_button = QAction('pomodoro', self)
        short_break = QAction('Short Break', self)
        long_break = QAction('Long break', self)
        self.placeHolder = QLabel('Place Holder')
        self.placeHolder.setStyleSheet('border: 6px solid black')
        self.placeHolder.setFont(QFont('Aerial', 7))
        self.placeHolder.setAlignment(Qt.AlignCenter)
        self.placeHolder.setFixedSize(QSize(200, 100))
        startBtn = QPushButton('Start')
        settingsBtn = QPushButton('Settings')
        # Adding the widgets
        layout.addWidget(self.placeHolder, 1, 1)
        layout.addWidget(startBtn, 2, 1)
        layout.addWidget(settingsBtn, 3, 1)
        # toolbar settings
        toolbar = QToolBar('Toolbar')
        self.addToolBar(toolbar)
        toolbar.addAction(pomodoro_button)
        toolbar.addAction(short_break)
        toolbar.addAction(long_break)
        # button functionality
        pomodoro_button.clicked.connect(self.pomodoro)
        short_break.clicked.connect(self.short_break)
        long_break.clicked.connect(self.long_break)
        startBtn.clicked.connect(self.start)
        settingsBtn.clicked.connect(self.settings)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def pomodoro(self):
        pass
    def short_break(self):
        pass
    def long_break(self):
        pass
    def start(self):
        pass
    def setting(self):
        pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()