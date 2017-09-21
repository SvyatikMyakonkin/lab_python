import sys
# -*- coding: utf-8 -*-
weight = input('Weight: ')
height = input('Height: ')

indexBody = float(weight) / (height*height)
print('Your Weight index' + ' ' + str(indexBody))


