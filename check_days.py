# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:47:55 2021

@author: Javadzadeh
"""

def check_days(day,Day):
    ind={}
    
    
    for i in range(len(day)):
        
        for j in range(len(Day)):
            
            if day.iloc[i]==Day.iloc[j]:
                ind.setdefault(j,[])
                ind[j]+=[i]
                
    
    return ind 
    


            
                 
                 
                
    
    
    
    