# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:23:45 2022

@author: CARLOS
"""
# Dado el total, calcular el IGV y el subtotal
import financieros
total = 1000.49
print(f"Sutotal; {financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")