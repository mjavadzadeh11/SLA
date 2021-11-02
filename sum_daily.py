# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:33:53 2021

@author: Javadzadeh
"""
import pandas as pd
def sum_daily(day,unique_day,duration):
    dict_unique={}
    dict_unique1={}
    
    for days in unique_day:
        
        for i in range(len(day)):
            
            if days==day.iloc[i]:
                 dict_unique.setdefault(days , 0)
                 dict_unique[days]+=duration.iloc[i]
                 
    for i in dict_unique.keys():
        if dict_unique[i]>5:
            dict_unique1[i]=[dict_unique[i] , True]
        else:
            dict_unique1[i]=[dict_unique[i], False]
            
    
        
            
             
    
        

            
            
                
  
            
            
                
                
    return dict_unique1 