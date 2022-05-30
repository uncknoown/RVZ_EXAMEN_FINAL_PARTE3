# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:33:20 2022

@author: CARLOS
"""

noticia = open("noticia.txt","rt", encoding=('utf-8'))
datos_noticia = noticia.read()
print(datos_noticia)