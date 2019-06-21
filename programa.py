#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:30:20 2019

@author: rodolfopardo
"""

# Vamos a declarar los animales que intervienen en la granja

perros = int(input("¿Cuántos perros tiene la granja? = "))
gatos = int(input("¿Cuántos gatos tiene la granja? = "))
conejos = int(input("¿Cuántos conejos tiene la granja? = "))


total_animales = perros + gatos + conejos
promedio = total_animales / 3

print("El total de animales de la granja es de", total_animales)

print("El promedio de animales es de", promedio)


