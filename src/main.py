import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.Ui()
    def Ui(self, *args, **kwargs):
        #  pomodoro has 4 blocks of work in each block there are different stages
        #  pomodoro(Working time == 25 min) short_break(short time rest == 5) long_break(long time rest == 15)
        self.pomodoroCount = 0
        self.count = 0  # Seconds

        self.start = False  # Boolean to control if the timer is ON or OFF

        self.setWindowTitle("Pomodoro App")

        widget = QWidget()
        layout = QGridLayout()
        # ui components
        pomodoro_button = QPushButton('pomodoro')
        short_break = QPushButton('Short Break')
        long_break = QPushButton('Long break')
        self.placeHolder = QLabel('Place Holder')
        self.placeHolder.setFont(QFont('Aerial', 7))
        self.placeHolder.setAlignment(Qt.AlignCenter)
        self.placeHolder.setFixedSize(QSize(200, 100))
        startBtn = QPushButton('Start')
        settings = QPushButton('Settings')
        # Adding the widgets

        layout.addWidget(pomodoro_button, 0, 0)
        layout.addWidget(short_break, 0, 1)
        layout.addWidget(long_break, 0, 2)
        layout.addWidget(self.placeHolder, 1, 1)
        layout.addWidget(startBtn, 2, 1)
        layout.addWidget(settings, 3, 1)

        # button functionality
        pomodoro_button.clicked.connect(self.pomodoro)
        short_break.clicked.connect(self.shortBreak)
        long_break.clicked.connect(self.longBreak)
        startBtn.clicked.connect(self.startPomodoro)
        settings.clicked.connect(self.setting)
        #  timer
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(100)

        self.show()  # Showing the widgets
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

    def setting(self):  # Adding a task
        pass

    def show_time(self):
        mins, secs = divmod(self.count, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # Printing the text of the count
        if self.start:  # Checking if is True or False
            self.count -= 1  # Incrementing the count
            time.sleep(1)
            if self.count == 0:
                self.start = False
        self.placeHolder.setText(time_format)

# One QApplication needed
# Pass in sys.argv to allow command line arguments for the app.
# QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()

# Starting the event loop.
app.exec()
# The app will not reach this part until you close the app and the event loop has finished