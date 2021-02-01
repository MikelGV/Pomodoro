import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("enter your text")

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)
    def return_pressed(self):
        print('return pressed')
        self.centralWidget().setText("boom")
    def selection_changed(self):
        print("selection changed")
        print(self.centralWidget().selectedText)

    def text_edited(self, s):
        print("text edited")
        print(s)
    def text_changed(self, s):
        print("Text changed")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()





''''''''''''''''
        layout = QVBoxLayout()
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit
                   ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        '''''''''''''''''''''''''''''''''''
