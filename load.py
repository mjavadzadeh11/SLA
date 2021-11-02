# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:43:29 2021

@author: Javadzadeh
"""
import pandas as pd

def load(filename):
    
    
    file=pd.ExcelFile(filename)
    res = len(file.sheet_names)
    sheets=[]
    
    #load all sheets in excel file:
    for i in range(res):
        sheets.append(pd.read_excel(filename,sheet_name= i))
    
    return [res,sheets]