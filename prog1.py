#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # подключаем библиотеку math (математические операции)
import numpy # подключаем библиотеку numpy (для работы с массивами)
import matplotlib.pyplot as mpp # подключаем библиотеку matplotlib (для построения графиков)


if __name__=='__main__': # проверка, на то, что файл запущен как основная программа
    arguments = numpy.r_[0:200:0.1] # задаём область
    mpp.plot( # строим график
        arguments, # используем заданную область как область функции
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # задаём правило функии
    ) # )
    mpp.show() # показываем график