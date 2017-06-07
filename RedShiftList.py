#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np

RedList = range(20, 0)
RedList.reverse()
print RedList


"""
print "Redshift con que iniciará la simulación"
z_ini = float(raw_input('RedShift de Inicio == z : '))
a_ini = float(1 / (1 + z_ini)) 
print 'TimeBegin: ', a_ini, '\n\n\n'

 
print "Conversion de TimeMax a Redshift Final de la simulación"
a_fin = float(raw_input('TimeMax de Gadget-2 == a : '))
z_fin = (1 - a_fin)/a_fin
print 'RedShift Final == z : ', z_fin, '\n\n\n'


print "Redshift final de la simulación"
z_fn = float(raw_input('RedShift del Final == z : '))
a_fn = float(1 / (1 + z_fn)) 
print 'TimeMax: ', a_fn, '\n\n\n'
"""

RedList2 = []
for ind in RedList:
        p = float(ind/2.0)
        RedList2.append(p)
print RedList2



Olist2 = open('OutputListRedShift.txt', 'w')
Olist2.close


for unid in RedList2:
        z_new = float(1 / (1 + float(unid)))
        de__0 = str(z_new).strip()

        OutputList = open('OutputListRedShift.txt', 'a')
        OutputList.write(de__0 + '\n')
        OutputList.close
        print z_new
