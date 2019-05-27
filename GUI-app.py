#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
import PyQt5.QtWidgets as qw
import requests
from PyQt5.QtCore import pyqtSlot


class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 400)
        self.move(70, 70)
        self.setWindowTitle('This is my GUI app')

        self.dnpBtn = qw.QPushButton("Don't push", self)
        self.dnpBtn.move(125, 75)
        self.dnpBtn.clicked.connect(self.dnt_push)

        self.sadBtn = qw.QPushButton("I'm sad.", self)
        self.sadBtn.move(125, 150)
        self.sadBtn.clicked.connect(self.sad)

        self.goNetBtn = qw.QPushButton('Download AU', self)
        self.goNetBtn.move(125, 225)
        self.goNetBtn.clicked.connect(self.spbau)

        self.quitBtn = qw.QPushButton('Close', self)
        self.quitBtn.move(125, 300)
        self.quitBtn.clicked.connect(self.close)

    @pyqtSlot(bool)
    def dnt_push(self, evt):
        print('OMG, you pushed it! NO!')
        time.sleep(3)
        print("Hm, hothing bad happened. That's cool =)")
        

    @pyqtSlot(bool)
    def spbau(self, evt):
        site = requests.get('https://spbau.ru/')
        print('Page https://spbau.ru/', 'with', len(site.content), 'bytes was downloaded from the Internet')


    @pyqtSlot(bool)
    def sad(self, evt):
        print("don't be sad! you are a good guy! \U0001F609 everything'll be OK.")


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
