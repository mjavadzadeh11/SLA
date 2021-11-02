# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:17:34 2021

@author: Javadzadeh
"""

def sheet_info(df):
    for index in range(len(df)):
        if df.iloc[index , 0]== "Total":
            final_index=index
    
    Date=df.iloc[2:final_index , 0]
    Day=Date.str.slice(start=-2)
            
    
    Dw=df.iloc[2:final_index , 1:3]
    Duration=df.iloc[2:final_index , 3]
    Disrupt=df.iloc[2:final_index , 5]
    
    unique=set(Day)
    unique_day=list(unique)
    unique_day.sort()
    
    

    
    return  Date , Day , Dw , Duration , Disrupt , unique_day , final_index

def empty_sheets(df,Day):
    
    if len(Day)==0:
        return True
    else:
        return False
    
    
    