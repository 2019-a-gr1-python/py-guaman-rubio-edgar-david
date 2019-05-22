# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:36:57 2019

@author: Edgar
"""

import numpy as np
import pandas as pd

arr_rand = np.random.randint(0,10,6).reshape(2,3)
df = pd.DataFrame(arr_rand,columns=['Estatura(cm)','Peso(kg)','Edad(años)'],index=['Edgar','David'])
df2 = pd.DataFrame(arr_rand)
df2.columns = ['Estatura(cm)','Peso(kg)','Edad(años)']
df2.index = ['Andres','Jorge']
df3 = pd.DataFrame(arr_rand)
df3[0]
df2['Estatura(cm)']
type(df2['Estatura(cm)'])

df['Estatura(cm)']['Edgar']
df['Peso(kg)']['Edgar']
df['Edad(años)']['Edgar']





