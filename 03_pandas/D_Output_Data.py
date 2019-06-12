# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:23:19 2019

@author: Edgar
"""
import pandas as pd
import numpy as np
import os
import sqlite3

path = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\csv\\artwork_data.csv'

df = pd.read_csv(path,nrows=5,usecols=['id','artist'], index_col='id')

columnas_a_usar=['id','artist','title','medium','year','acquisitionYear','height','width','units']

df_completo = pd.read_csv(path,usecols=columnas_a_usar,index_col='id')

path_guardado = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\csv\\artwork_data.pickle'
df_completo.to_pickle(path_guardado)
df_completo_pickle = pd.read_pickle(path_guardado)
df = df_completo_pickle.iloc[49980:50019,:].copy()

#Tipos de archivos que se pueden exportar los dataframes
# JSON
# SQL
# EXCEL

### Exportar a Excel ####
df.to_excel('ejemplo_basico.xlsx')

df.to_excel('ejemplo_basico_sin_indices.xlsx',index=False)

columnas = ['artist','title','year']

df.to_excel('columnas.xlsx',columns=columnas)

#### Multiples hojas de trabajo (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',engine='xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')

df.to_excel(writer, sheet_name = 'Preview_dos', index=False)

df.to_excel(writer, sheet_name = 'Preview_tres', columns=columnas)

writer.save()

## Formateo condicional ##

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine='xlsxwriter')

artistas_contados.to_excel(writer, sheet_name='Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index)+1)

formato = {'type':'2_color_scale',
           'min_value':'10',
           'min_type':'percentile',
           'max_value':'99',
           'max_type':'percentile'}

hoja_artistas.conditional_format(rango_celdas,formato)

writer.save()

############## SQL ############

with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('tabla',conexion)
    
## with sqlite3.connect('mysql://user:password@ip:puerto/bd') as conexion
    
############## JSON ############
    
df.to_json('artistas.json')
df.to_json('artistas_orientados_tabla.json',orient='table')

##### Ejercicios con formatos condicionales #####

conteo_artistas = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('traffic_lights.xlsx', engine='xlsxwriter')

conteo_artistas.to_excel(writer, sheet_name='conteo_artistas')

hoja_artistas = writer.sheets['conteo_artistas']

rango_celdas = 'B2:B{}'.format(len(conteo_artistas.index)+1)

formato = {'type': 'icon_set',
           'icon_style': '3_traffic_lights'}

hoja_artistas.conditional_format(rango_celdas,formato)

writer.save()


##### Ejercicios con formatos condicionales #####

conteo_artistas = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('Signs.xlsx', engine='xlsxwriter')

conteo_artistas.to_excel(writer, sheet_name='conteo_artistas')

hoja_artistas = writer.sheets['conteo_artistas']

rango_celdas = 'B2:B{}'.format(len(conteo_artistas.index)+1)

formato = {'type': 'icon_set',
           'icon_style': '3_signs'}

hoja_artistas.conditional_format(rango_celdas,formato)

writer.save()




















