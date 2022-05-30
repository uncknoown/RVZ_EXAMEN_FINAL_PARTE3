# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:17:30 2022

@author: CARLOS
"""
# Dado el Subtotal, calcular el IGV y el total
import financieros
subtotal = 847.87
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2f}")
