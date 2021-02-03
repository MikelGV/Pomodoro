import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        #  pomodoro has 4 blocks of work in each block there are different stages
        #  aKa pomodoro(Working time == 25 min) short_break(short time rest == 5) long_break(long time rest == 15)
        super(MainWindow, self).__init__(*args, **kwargs)

        self.pomodoroCount = 0
        self.count = 0  # Seconds

        self.start = False  # Boolean to control if the timer is on or of

        self.setWindowTitle("Pomodoro App")

        widget = QWidget()
        layout = QGridLayout()
        # ui components
        pomodoro_button = QPushButton('pomodoro')
        short_break = QPushButton('Short Break')
        long_break = QPushButton('Long break')
        self.placeHolder = QLabel('Place Holder')
        self.placeHolder.setStyleSheet('border: 6px solid black')
        self.placeHolder.setFont(QFont('Aerial', 7))
        self.placeHolder.setAlignment(Qt.AlignCenter)
        self.placeHolder.setFixedSize(QSize(200, 100))
        startBtn = QPushButton('Start')
        settingsBtn = QPushButton('Settings')
        # Adding the widgets
        layout.addWidget(pomodoro_button, 0, 0)
        layout.addWidget(short_break, 0, 1)
        layout.addWidget(long_break, 0, 2)
        layout.addWidget(self.placeHolder, 1, 1)
        layout.addWidget(startBtn, 2, 1)
        layout.addWidget(settingsBtn, 3, 1)
        # button functionality
        pomodoro_button.clicked.connect(self.pomodoro)
        short_break.clicked.connect(self.shortBreak)
        long_break.clicked.connect(self.longBreak)
        startBtn.clicked.connect(self.startPomodoro)
        settingsBtn.clicked.connect(self.setting)
        #  timer
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(100)

        self.show()
        # Setting the layout and the widget
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def pomodoro(self):
        self.count = 1500  # default time in pomodoro
    def shortBreak(self):
        self.count = 300
    def longBreak(self):
        self.count = 900
    def startPomodoro(self):
        self.start = True
        print(self.start)

    def setting(self):
        pass

    def show_time(self):
        mins, secs = divmod(self.count, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        if self.start:
            self.count -= 1
            time.sleep(1)
            if self.count == 0:
                self.start = False
        self.placeHolder.setText(time_format)
app = QApplication(sys.argv)

window = MainWindow()
# window.show()

app.exec()