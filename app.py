
import sys
import os

from PyQt6.QtWidgets import (
    QApplication,QMainWindow, QWidget,
    QStackedLayout,QVBoxLayout,QHBoxLayout,
    QTableWidget,QLabel,QTextEdit,
)

from PyQt6.QtCore import (
    QSize
)

from PyQt6.QtGui import (
    QAction
)


import lab1_frequency_analysis.widget
import lab2_simple_replacement.widget


class FirstEncryptionWidget(QWidget):
    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()
 
        label = QLabel("Insert Encyption widget")
        
        message_field = QTextEdit()
        message_field.setText("This is example of message text....")

        encrypted_field = QTextEdit()
        encrypted_field.setText("This is example of an encrypted text....")

        layout.addWidget(label)
        layout.addWidget(message_field)
        layout.addWidget(encrypted_field)
        
        self.setLayout(layout)


class MainWindow(QMainWindow):
    """
    Main window
    Contains stacked layout widget with menu bar

    """
    def __init__(self) -> None:
        super().__init__()

        self._widgets = dict()
        
        self.setWindowTitle("Cryptology laboratory")

        self.layout = QStackedLayout()
        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

        # Widgets

        self.initWidgets()
        self.setupLayout()

        # Menu Bar
        menu = self.menuBar()

        # Actions
        freq_analysis_action = QAction("Frequency analysis",self)
        first_encryption_action = QAction("Simple encryption",self)

        encryption_menu = menu.addMenu("Encrypt")
        encryption_menu.addAction(first_encryption_action)
        menu.addAction(freq_analysis_action)

        # Triggers for layouts
        freq_analysis_action.triggered.connect(self.activateFreqAnalysis)
        first_encryption_action.triggered.connect(self.activateFirstEncryption)


    def initWidgets(self):
        self._widgets["Frequency analysis"] = lab1_frequency_analysis.widget.MainWidget()
        self._widgets["Insertion encryption"] = lab2_simple_replacement.widget.MainWidget()
    
    def setupLayout(self):
        for widget_name in self._widgets.keys():
            self.layout.addWidget(self._widgets[widget_name])


    def activateFreqAnalysis(self):
        self.layout.setCurrentIndex(0)


    def activateFirstEncryption(self):
        self.layout.setCurrentIndex(1)





def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()  

if __name__ == "__main__":
    main()

