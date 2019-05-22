# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:59 2019

@author: Edgar
"""

import pandas as pd
import json
import os

path = 'C:\\Users\\Edgar\\Documents\\GitHub\\py-guaman-rubio-edgar-david\\03_pandas\\data\\artwork'

archivo = '/a/000/a00001-1035.json'

path_archivo = path+archivo

llaves = ['id','all_artists','title','medium','dateText','acquisitionYear','height','width','units']

registro = []

with open(path_archivo) as texto_json:
    contenido_json=json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)
    registro_df = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df.append(valor)
    serie = tuple(registro_df)
print(serie)
df_chiquito=pd.DataFrame([registro_df])
df_chiquito_t=pd.DataFrame([serie])
