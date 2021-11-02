# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:14:33 2021

@author: Javadzadeh
"""



import load
import sheet_info as info
import sum_daily
import time_f
import check_days
import pandas as pd

#res : number of sheets in loaded excel
#sheet : contain all sheets seperatly in a list
filename='CFS.xlsx'
[res,sheets]=load.load(filename)

main=sheets[0]
#return the index of Total in excels:
[Date , Day , Dw , Duration , Disrupt , final_index , _ ]=info.sheet_info(main)




for i in range(1,7):
    
    sub=sheets[i]
    sub1=sub.copy()
    
    [date , day , dw , duration , disrupt , unique_day , final_index]\
        =info.sheet_info(sub)
    

        
    time_f.time_fact(sub, day, dw , duration)
    time_f.time_fact(sub1, day, dw , duration)
    time_f.time_fact(main,Day,Dw , Duration)        
    unique_df = sum_daily.sum_daily(day, unique_day, duration)
    
    ind = check_days.check_days(day, Day)
    
    for i , m in ind.items():
        for j in m:
            
            duration.iloc[j] = time_f.inside_duration(dw.iloc[j,0], dw.iloc[j,1],\
                               Dw.iloc[i,0],  Dw.iloc[i,1], Disrupt.iloc[i],duration,j)
                
                
        
   
    
    time_f.under_limit(day, Day, unique_df, duration)
                
    for i in range (2,final_index+1):
        
        # sub1.iloc[i,6] : Multiplication of duration , distrupt and timefact
        # sub.iloc[i,3]  : Durations which under limit of day and common with service are eliminate
        # sub1.iloc[i,4] : Timefact
        # sub1.iloc[i,5] : Disrupt
        sub1.iloc[i,6] = sub.iloc[i,3] * sub1.iloc[i,4] * sub1.iloc[i,5]
        
    
    sub1.to_csv(r'E:\sla\python\edited' ,index=False)
                
                
    
                
        
            
            
            
                
            
            
            
                
    
    
        
        
                
        
                    
    

    
            
              
                 
    
    

            
                
        
        

        
        
       
            
           
            
            
                
                
                
        
                
    
            
        
        
        
            
            
                
            
        
    


    
    
    
    
        
    
        
 
            
        
   
    

            
                    
                            
                            
                 

                            
                        
                        
            

                    
                    
                 
        
        
        
            
            
            
                
                
        
        
        
        
        
        
        
        
   
       
            
    
        
    
    
    




 
    

     
               
   
        
            
           
                
                
            
            
    
    
    
    
        
        
        
        
        
        
    
    
    
    
            
            



