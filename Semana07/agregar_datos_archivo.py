# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:47:14 2022

@author: CARLOS
"""

archivo = open("noticia.txt","at")
#\ n es para agregar el contenido en un línea al final
contenido="\nfuente:RPP"

archivo.write(contenido)
archivo.close()