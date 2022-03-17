
import sys
import os

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,QHBoxLayout,
    QTableWidget,QTextEdit,
    QTableWidgetItem,QPushButton,QCheckBox,QComboBox,
    QFileDialog,
)

from PyQt6.QtCore import (
    Qt,
)

from lab1_frequency_analysis.interface import WordsDict



class FrequencyTable(QTableWidget):

    def __init__(self):
        super().__init__()

        self._dict = WordsDict() 
        self._order = Qt.SortOrder.DescendingOrder

        self.setColumnCount(2)


    def load_data(self, text:str) -> None:
        self._dict.fill_from_str(text)


    def refresh_table(self) -> None:

        self.setRowCount(len(self._dict.items()))
        
        self.setHorizontalHeaderLabels(["Letter","Frequency"])
        self.set_items()
        self.resizeColumnsToContents()


    def set_items(self):
        for i,(letter,frequency) in enumerate(self._dict.items()):
            self.setItem(i,0,QTableWidgetItem(letter))
            self.setItem(i,1,QTableWidgetItem(str(frequency)))
   

    def change_order_of_sorting(self):
        if self._order == Qt.SortOrder.DescendingOrder:
            self._order = Qt.SortOrder.AscendingOrder
        else:
            self._order = Qt.SortOrder.DescendingOrder


    def sort_by_letter(self):
        self.change_order_of_sorting()
        self.sortByColumn(0,self._order)
        self.change_order_of_sorting()


    def sort_by_frequency(self):
        self.sortByColumn(1,self._order)
           


class MainWidget(QWidget):
    
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout()

        buttons_layout = QVBoxLayout()


        # Widgets

        self._open_file_button = QPushButton("Open file")
        self._order = QCheckBox("Sort in descending order")
        self._sort_option = QComboBox()
        self._sort_button = QPushButton("sort")
        self._text_field = QTextEdit("Here should be your text!")
        self._table = FrequencyTable()
        

        self._sort_option.addItems(["By letter", "By frequency"])
    
        self._sort_button.setCheckable(True)
        self._open_file_button.setCheckable(True)
    
        self._text_field.textChanged.connect(self.onTextChanged)
        self._open_file_button.clicked.connect(self.onOpenFileButtonClicked)
        self._sort_button.clicked.connect(self.onSortButtonClicked)

        self._order.setCheckable(True)
        self._order.setCheckState(Qt.CheckState.Checked)
        self._order.stateChanged.connect(self._table.change_order_of_sorting)
        


        buttons_layout.addWidget(self._open_file_button)
        buttons_layout.addWidget(self._order)
        buttons_layout.addWidget(self._sort_option)
        buttons_layout.addWidget(self._sort_button)

        data_view_layout = QVBoxLayout()

        data_view_layout.addWidget(self._text_field)
        data_view_layout.addWidget(self._table)
        
        

        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(data_view_layout)

        self.setLayout(main_layout)



    def onOpenFileButtonClicked(self):

        path = QFileDialog.getOpenFileName(self,"Open File","","Text File (*.txt)")

        if path != ('',''):
            with open(path[0]) as f:
                self._text_field.setText(f.read())
            
        self._open_file_button.setChecked(False)


    def onTextChanged(self):
        self._table.load_data(self._text_field.document().toRawText())
        self._table.refresh_table()

    def onSortButtonClicked(self):
        
        if self._sort_option.currentIndex() == 0:
            self._table.sort_by_letter()
        elif self._sort_option.currentIndex() == 1:
            self._table.sort_by_frequency()

        self._sort_button.setChecked(False)
