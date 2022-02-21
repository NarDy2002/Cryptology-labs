
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt,QSize

from frequency import WordsDict

frequency_dict = WordsDict()
frequency_dict.fill_from_file("words.txt")


class FrequencyTable(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()

        self._data = frequency_dict.items()
        self._order = Qt.SortOrder.DescendingOrder

        self.setColumnCount(2)
        self.setRowCount(len(self._data))

        self.setHorizontalHeaderLabels(["Letter","Frequency"])
        self.set_items()
        self.resizeColumnsToContents()
    

    def set_items(self):
        for i,(letter,frequency) in enumerate(self._data):
            self.setItem(i,0,QTableWidgetItem(letter))
            self.setItem(i,1,QTableWidgetItem(str(frequency)))

   
    def change_order_of_sorting(self):
        if self._order == Qt.SortOrder.DescendingOrder:
            self._order = Qt.SortOrder.AscendingOrder
        else:
            self._order = Qt.SortOrder.DescendingOrder

    def sortByLetter(self):
        self.change_order_of_sorting()
        self.sortByColumn(0,self._order)
        self.change_order_of_sorting()

    def sortByFrequency(self):
        self.sortByColumn(1,self._order)
           

    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Frequency Analysis")
        self.setFixedSize(QSize(460,200))

        main_layout = QtWidgets.QHBoxLayout()

        buttons_layout = QtWidgets.QVBoxLayout()

        self._open_file = QtWidgets.QPushButton("Open file")
        self._about = QtWidgets.QPushButton("About")
        self._order = QtWidgets.QCheckBox("Sort in descending order")
        self._sort_by_letter = QtWidgets.QPushButton("Sort by alphabet")
        self._sort_by_frequency = QtWidgets.QPushButton("Sort by frequency")
        
        self._table = FrequencyTable()

        self._sort_by_frequency.setCheckable(True)
        self._sort_by_letter.setCheckable(True)

        self._sort_by_frequency.clicked.connect(self.frequency_button_pressed)
        self._sort_by_letter.clicked.connect(self.letter_button_pressed)
        


        self._order.setCheckable(True)
        self._order.setCheckState(Qt.CheckState.Checked)
        self._order.stateChanged.connect(self._table.change_order_of_sorting)
        


        buttons_layout.addWidget(self._open_file)
        buttons_layout.addWidget(self._about)
        buttons_layout.addWidget(self._order)
        buttons_layout.addWidget(self._sort_by_letter)
        buttons_layout.addWidget(self._sort_by_frequency)


        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self._table)


        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)



    def letter_button_pressed(self):
        self._table.sortByLetter()
        self._sort_by_letter.setChecked(False)
    

    def frequency_button_pressed(self):
        self._table.sortByFrequency()
        self._sort_by_frequency.setChecked(False)

    





def main():
    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()  

if __name__ == "__main__":
    main()

