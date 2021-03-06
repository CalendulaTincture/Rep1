#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # ���������� ���������� math (�������������� ��������)
import numpy # ���������� ���������� numpy (��� ������ � ���������)
import matplotlib.pyplot as mpp # ���������� ���������� matplotlib (��� ���������� ��������)


if __name__=='__main__': # ��������, �� ��, ��� ���� ������� ��� �������� ���������
    arguments = numpy.r_[0:200:0.1] # ����� �������
    mpp.plot( # ������ ������
        arguments, # ���������� �������� ������� ��� ������� �������
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # ����� ������� ������
    ) # )
    mpp.show() # ���������� ������