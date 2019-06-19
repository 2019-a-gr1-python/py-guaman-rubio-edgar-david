# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 00:21:50 2019

@author: Edgar
"""

import pandas as pd

path = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\employee_compensation\\employee-compensation.csv'

columnas_a_usar=['Year Type','Year','Department','Job','Salaries','Overtime','Other Salaries','Total Salary']

df_completo = pd.read_csv(path,usecols=columnas_a_usar,index_col='Job')

path_guardado = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\employee_compensation\\employee-compensation.pickle'
df_completo.to_pickle(path_guardado)
df_completo_pickle = pd.read_pickle(path_guardado)
df_reducido = df_completo_pickle.iloc[100:1100,:].copy()

##### Formato condicional 1 #####

writer = pd.ExcelWriter('luces_semaforo.xlsx', engine='xlsxwriter')

df_reducido.to_excel(writer, sheet_name='salarios')

salarios = writer.sheets['salarios']

rango_celdas = 'E2:E{}'.format(len(df_reducido.index)+1)

formato = {'type': 'icon_set',
           'icon_style': '3_traffic_lights'}

salarios.conditional_format(rango_celdas,formato)

writer.save()

##### Formato condicional 2 #####

writer = pd.ExcelWriter('dos_colores.xlsx', engine='xlsxwriter')

df_reducido.to_excel(writer, sheet_name='salarios')

salarios1 = writer.sheets['salarios']

rango_celdas = 'F2:F{}'.format(len(df_reducido.index)+1)

formato = {'type': '2_color_scale',
           'min_value':10000}

salarios1.conditional_format(rango_celdas, formato)

writer.save()

##### Formato condicional 3 #####

writer = pd.ExcelWriter('data_bars.xlsx', engine='xlsxwriter')

df_reducido.to_excel(writer, sheet_name='salarios')

salarios1 = writer.sheets['salarios']

rango_celdas = 'G2:G{}'.format(len(df_reducido.index)+1)

formato = {'type': 'data_bar',
           'min_value':'10000'}

salarios1.conditional_format(rango_celdas, formato)

writer.save()

##### Formato condicional 4 #####

writer = pd.ExcelWriter('ratings.xlsx', engine='xlsxwriter')

df_reducido.to_excel(writer, sheet_name='salarios')

salarios1 = writer.sheets['salarios']

rango_celdas = 'H2:H{}'.format(len(df_reducido.index)+1)

formato = {'type': 'icon_set',
           'icon_style': '4_ratings',
           'min_value':'50000'}

salarios1.conditional_format(rango_celdas, formato)

writer.save()