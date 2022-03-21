import sys
import os

from PyQt6.QtWidgets import (
    QWidget,QLabel,
    QVBoxLayout,QHBoxLayout,
    QTableWidget,QTextEdit,
    QTableWidgetItem,QPushButton,QCheckBox,QComboBox,
    QFileDialog,
)

from PyQt6.QtCore import (
    Qt
)
from PyQt6.QtGui import(
    QAction
)
from matplotlib.pyplot import text

import lab2_simple_replacement.interface



class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Encryptor

        self._encrypter = lab2_simple_replacement.interface.SimpleReplacementEncrypter()

        # Widgets

        self._left_field = QTextEdit("Message here...")
        self._right_field = QTextEdit("Encrypted message here ...")
        self._key_holder = QTextEdit("Key place")

        # Buttons

        self._read_text_button = QPushButton("Open text")
        self._read_key_button = QPushButton("Open key")
        self._generate_key_button = QPushButton("Generate key")
        self._refresh_button = QPushButton("Refresh")
        self._load_to_file_button = QPushButton("Load to file")

        # Operation option

        self._option = QComboBox()
        self._option.addItems(["Encrypt","Decrypt"])
        
        # Triggers

        self._read_text_button.clicked.connect(self.onReadTextButtonClicked)
        self._read_key_button.clicked.connect(self.onReadKeyButtonClicked)
        self._generate_key_button.clicked.connect(self.onGenerateKeyButtonClicked)

        self._load_to_file_button.clicked.connect(self.onLoadToFileButtonClicked)
        
        # ----

        self._key_holder.textChanged.connect(self.refreshKeyFromHolder)
        self._refresh_button.clicked.connect(self.onRefreshButtonClicked)
        
        # Setup layouts

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        key_layout = QHBoxLayout() 
        text_layout = QHBoxLayout()
        key_buttons_layout = QVBoxLayout()
        key_fields_layout = QHBoxLayout()
        text_buttons_layout = QVBoxLayout()
        text_fields_layout = QHBoxLayout()
        key_labels_layout = QVBoxLayout()
        key_holders_layout = QVBoxLayout()


        main_layout.addLayout(key_layout)
        main_layout.addLayout(text_layout)

        key_layout.addLayout(key_buttons_layout)
        key_layout.addLayout(key_fields_layout)

        key_buttons_layout.addWidget(self._read_key_button)
        key_buttons_layout.addWidget(self._generate_key_button)


        key_fields_layout.addLayout(key_labels_layout)
        key_fields_layout.addLayout(key_holders_layout)
        
        key_labels_layout.addWidget(QLabel("Alphabet:"))
        key_labels_layout.addWidget(QLabel("Key:"))
       
        key_holders_layout.addWidget(QLabel(self._encrypter.alphabet))
        key_holders_layout.addWidget(self._key_holder)
        
        self._key_holder.setFixedHeight(26)



        text_layout.addLayout(text_buttons_layout)
        text_layout.addLayout(text_fields_layout)
        text_buttons_layout.addWidget(self._read_text_button)        
        text_buttons_layout.addWidget(self._refresh_button)
        text_buttons_layout.addWidget(self._load_to_file_button)
        text_buttons_layout.addWidget(self._option)
        text_fields_layout.addWidget(self._left_field)
        text_fields_layout.addWidget(self._right_field)


    def onReadTextButtonClicked(self):
        path = QFileDialog.getOpenFileName(self,"Open file",'',"Text Files (*.txt)")

        if path != ("",""):
            with open(path[0], 'r',encoding="utf-8") as f:
                text = f.read()
                self._left_field.clear()
                self._left_field.setText(text)

        self._read_text_button.setChecked(False)


    def onReadKeyButtonClicked(self):
        path = QFileDialog.getOpenFileName(self,"Open file",'',"Text Files (*.txt)")

        if path != ("",""):
            with open(path[0], 'r',encoding="utf-8") as f:
                key = f.read()
                self._key_holder.clear()
                self._key_holder.setText(key)
                self._encrypter.key = key
        
        self._read_key_button.setChecked(False)



    def onGenerateKeyButtonClicked(self):
        self._encrypter.generate_key()
        self._key_holder.clear()
        self._key_holder.setText(self._encrypter.key)

        self._generate_key_button.setChecked(False)


    def onLoadToFileButtonClicked(self):
        path = QFileDialog.getOpenFileName(self,"Open file",'',"Text Files (*.txt)")

        if path != ("",""):
            with open(path[0], 'w',encoding="utf-8") as f:
                text = self._right_field.document().toRawText()
                f.write(text)

        self._load_to_file_button.setChecked(False)


    def refreshKeyFromHolder(self):
        self._encrypter.key = self._key_holder.document().toRawText()


    def onRefreshButtonClicked(self):
        text_for_right_field = str()
        if self._option.currentText() == "Encrypt":
            text_for_right_field = self._encrypter.encrypt(self._left_field.document().toRawText())
        elif self._option.currentText() == "Decrypt":
            text_for_right_field = self._encrypter.decrypt(self._left_field.document().toRawText())
        else:
            raise ValueError("Bad option to refresh")

        self._right_field.clear()
        self._right_field.setText(text_for_right_field)

    
        