# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:03:34 2022

@author: CARLOS
"""
# Importamos la libreria
import camelcase

nombre = "carlos alberto ruiz montero"
print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase...")

# Imprimimos el nombre en formato titulo
# tilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los arguentos
# 'carlos' y 'ruiz'

cam2=camelcase.CamelCase('carlos','ruiz')
print(cam2.hump(nombre))