# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:16:26 2021

@author: Javadzadeh
"""
import datetime

Timez1=datetime.time   (0,0,0)    
Timez2=datetime.time   (7,0,0)
Timez3=datetime.time  (11,0,0)
Timez4=datetime.time  (18,0,0)
Timez5=datetime.time(23,59,59)

def time_diff(Time1,Time2):
    Total1= Time1.hour *3600 + Time1.minute * 60 + Time1.second
    Total2 = Time2.hour *3600 + Time2.minute * 60 + Time2.second
    
    M=(Total1 - Total2)/60
    return M
    



        
        
    
def time_comp(Time1,Time2):
    
    Total1 = Time1.hour*3600 + Time1.minute *60 + Time1.second
    
    Total2 = Time2.hour*3600 + Time2.minute *60 + Time2.second
    
    if Total1 >= Total2 :
        return True
    elif Total1 <= Total2 :
        return False
    
def time_within(Time1,Time2,Time3):
    Total1 = (Time1.hour*3600 + Time1.minute *60 + Time1.second) 
    Total2 = Time2.hour*3600 + Time2.minute *60 + Time2.second
    Total3 = (Time3.hour*3600 + Time3.minute *60 + Time3.second) 
    
    if Total2>=Total1 and Total2<=Total3:
        return True
    else:
        return False
    

   
def inside_duration(Time1,Time2,Time3,Time4,Disrupt, duration , j):
    
    Total1 = (Time1.hour*3600 + Time1.minute *60 + Time1.second) 
    Total2 = (Time2.hour*3600 + Time2.minute *60 + Time2.second)
    Total3 = (Time3.hour*3600 + Time3.minute *60 + Time3.second)
    Total4 = (Time4.hour*3600 + Time4.minute *60 + Time4.second)
    
    if Total1 >= (Total3 -300) and Total2<=(Total4+300) and Disrupt == 1.0:
         return 0
    elif Total1>= (Total3) and Total1 < Total4 and Total2 > Total4 and Disrupt == 1.0:
        #duzero=time_diff(Time4, Time1)
        duf=time_diff(Time4,Time2)
        
        return duf
    
    elif Total1 < Total3 and Total2 > Total3 and Total2 < Total4 and Disrupt == 1.0:
        duf=time_diff(Time2,Time3)
        
        return duf
    elif Total1 < Total3 and Total2> Total4 and Disrupt == 1.0 :
        duf= time_diff(Time3, Time1) + time_diff(Time2, Time4)
        
        return duf

    else:
        if  duration.iloc[j]>5:
            return duration.iloc[j]
        else:
            return 0 
       

            
        
        
        
        # if  duration.iloc[j]>5:
        #     return duration.iloc[j]
        # else:
        #     return 0       
        
        
        
        
        
    
    
    
    
    
    
    
  
def time_edge(Time1,Time2):
    Total1 = Time1.hour*3600 + Time1.minute *60 + Time1.second
    Total2 = (Time2.hour*3600 + Time2.minute *60 + Time2.second) -300
    Total3 = (Time2.hour*3600 + Time2.minute *60 + Time2.second) +300
    if Total1<=Total3 and Total1>=Total2:
        return True
    else:
        return False
    
    
    

            

def time_fact(df,Day,Dw,Duration):
    Timez1=datetime.time   (0,0,0)    
    Timez2=datetime.time   (7,0,0)
    Timez3=datetime.time  (11,0,0)
    Timez4=datetime.time  (18,0,0)
    Timez5=datetime.time(23,59,59)
    
    for i in range(len(Day)):
        
        if time_comp(Dw.iloc[i,0], Timez1) and time_comp(Timez2,Dw.iloc[i,1]):
            
            df.iloc[i+2,4]=1
            
        elif time_comp(Dw.iloc[i,0], Timez2) and time_comp(Timez3,Dw.iloc[i,1]):
            
            df.iloc[i+2,4]=4
            
        elif time_comp(Dw.iloc[i,0], Timez3) and time_comp(Timez4,Dw.iloc[i,1]):
            
            df.iloc[i+2,4]=3
        elif time_comp(Dw.iloc[i,0], Timez4) and time_comp(Timez5,Dw.iloc[i,1]):
            
            df.iloc[i+2,4]=2
            
        elif time_within(Timez1, Dw.iloc[i,0], Timez2) \
        and time_within(Timez2, Dw.iloc[i,1], Timez3):  
            
            du1= time_diff(Timez2,Dw.iloc[i,0])
            
            du2= time_diff(Dw.iloc[i,1], Timez2) 
            
            df.iloc[i+2,4] = (du1*1 / Duration.iloc[i] )  + (du2*4 / Duration.iloc[i] )
            
            
        elif  time_within(Timez2, Dw.iloc[i,0], Timez3) \
        and time_within(Timez3, Dw.iloc[i,1], Timez4): 
            
            du2 = time_diff(Timez3, Dw.iloc[i,0])
            
            du3= time_diff(Dw.iloc[i,1], Timez3)
            
            df.iloc[i+2,4] = (du2*4 / Duration.iloc[i] )  + (du3*3 / Duration.iloc[i] )
             
            
        elif time_within(Timez3, Dw.iloc[i,0], Timez4) \
        and time_within(Timez4, Dw.iloc[i,1], Timez5):
            
            du3= time_diff(Timez4, Dw.iloc[i,0])
            du4= time_diff(Dw.iloc[i,1], Timez4)
            
            df.iloc[i+2,4] =(du3*3 / Duration.iloc[i] )  + (du4*2 / Duration.iloc[i] )
            
            
        elif time_within(Timez1, Dw.iloc[i,0], Timez2) \
        and time_within(Timez3, Dw.iloc[i,1], Timez4):
            
            du1 = time_diff(Timez2,Dw.iloc[i,0]) 
            du2 = time_diff(Timez3,Timez2)
            du3 = time_diff(Dw.iloc[i,1],Timez3)
            
            df.iloc[i+2,4] =  (du3*3 / Duration.iloc[i+2] ) + (du2*4 / Duration.iloc[i] ) + \
                (du1*1 / Duration.iloc[i] )
            
                
        elif time_within(Timez2, Dw.iloc[i,0], Timez3) \
        and time_within(Timez4, Dw.iloc[i,1], Timez5):
            
            du2 = time_diff(Timez3, Dw.iloc[i,0])
            du3 = time_diff(Timez4, Timez3)
            du4 = time_diff(Dw.iloc[i,1], Timez4)
            df.iloc[i+2,4] = (du3*3 / Duration.iloc[i] ) + (du2*4 / Duration.iloc[i] ) + \
                (du4*2 / Duration.iloc[i] )
             
                
        else:
            
            du1 = time_diff(Timez2, Dw.iloc[i,0])
            du2 = time_diff(Timez3, Timez2)
            du3 = time_diff(Timez4, Timez3)
            du4 = time_diff(Dw.iloc[i,1], Timez4)
            
            df.iloc[i+2,4] = (du1*1 / Duration.iloc[i] )  + (du3*3 / Duration.iloc[i] )  \
                  + (du2*4 / Duration.iloc[i] ) + (du4*2 / Duration.iloc[i] )
             
            
            
    return df
    
def under_limit(day,Day,unique_df,duration):
    """ elimanates the durations which is lower than daily limit of 5 mins"""
    x=set(day)
    y=set(Day)
    z=list(x-y)
    z.sort()
    mlist=[]
    
    
    for i in z:
        
        if unique_df[i][1]==False:
            mlist.append(i)
    for i in range(len(day)):
        for j in mlist:
            if day.iloc[i] == j:
                duration.iloc[i]=0
     