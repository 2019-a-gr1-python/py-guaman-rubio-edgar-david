# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:54:00 2019

@author: Edgar
"""

#Pandas permite leer archivos de 3 lugares distintos
#Archivos de texto = JSON, CSV, HTML, XML, etc
#Archivos Binarios = asdadad
#Base de datos relacionales
import pandas as pd
import os
path = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\csv\\artwork_data.csv'

df = pd.read_csv(path,nrows=5,usecols=['id','artist'], index_col='id')

columnas_a_usar=['id','artist','title','medium','year','acquisitionYear','height','width','units']

df_completo = pd.read_csv(path,usecols=columnas_a_usar,index_col='id')

path_guardado = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\csv\\artwork_data.pickle'
df_completo.to_pickle(path_guardado)
df_completo_pickle = pd.read_pickle(path_guardado)



