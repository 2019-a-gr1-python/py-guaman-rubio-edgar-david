# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:18:43 2019

@author: Edgar
"""

print("Hola mundo")
edad = 24
nombre="Edgar"
print(nombre)

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

numero_serie = pd.Series(lista_numeros)
numero_serie_uno = pd.Series(tupla_numeros)
numero_serie_dos = pd.Series(np_numeros)

numero_serie_tres = pd.Series([True,False, 12, 123.34,"ABCD",None, (),[],{"nombre":"Edgar"}])

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]
serie_ciudades = pd.Series(lista_ciudades,index=["A","B","C","D"])
print(serie_ciudades["A"])
serie_ciudades[0]
type(serie_ciudades)
valores_ciudad = {"Ibarra":9500,"Guayaquil":8500,"Quito":3400,"Loja":2300}
serie_valor_ciudad = pd.Series(valores_ciudad)
serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[0]

ciudades_menores_5000 = serie_valor_ciudad < 5000

serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad *1.1

serie_valor_ciudad["Quito"] = 4750

print("Lima" in serie_valor_ciudad) #False

print("Loja" in serie_valor_ciudad)  #True

ciudades_uno = pd.Series({"Quito":1500,"Loja":4000})
ciudades_dos = pd.Series({"Loja":300,"Cuenca":1000,"Quito":2000})

print(ciudades_uno * ciudades_dos)

randomico = np.random.rand(3)

series_tres_rand = pd.Series(randomico)

ciudades_unidas = pd.concat([ciudades_uno,ciudades_dos])
print(ciudades_unidas)

ciudades_tres = pd.Series({"Chone":5500,"Puyo":2000})
ciudades_añadidas = ciudades_unidas.add(ciudades_tres)
print(ciudades_añadidas)

#Calculando valores de probabilidad
ciudades_unidas.max()

ciudades_unidas.std()

ciudades_unidas.median()

#Primeros 2 valores
ciudades_añadidas.head(2)

#Ultimos 2 valores
ciudades_añadidas.tail(2)

#Condicionales dentro de una serie

def calculo(valor):
    if(valor<=1000):
        return valor * 1.05
    if(valor>1000 and valor<=3000):
        return valor * 1.10
    if(valor > 3000):
        return valor * 1.15

ciudades_añadidas.map(calculo)









