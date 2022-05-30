# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:43:46 2022

@author: CARLOS
"""

archivo = open("archivo de prueba.txt","wt")
contenido = "Linea1 hola amigos como están\nLinea2 Bienvenido a la UNTELS"
archivo.write(contenido)
archivo.close()