# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:05:40 2021

@author: Javadzadeh
"""
class Time_F():
    
    import datetime
    
    Timez1=datetime.time   (0,0,0)    
    Timez2=datetime.time   (7,0,0)
    Timez3=datetime.time  (11,0,0)
    Timez4=datetime.time  (18,0,0)
    Timez5=datetime.time(23,59,59)
    def __init__(self,Time):
        self.Time=Time
        
    def time_diff(self,other):
        Total1=self.hour * 3600 + self.minute * 60 + self.second
        Total2=other.hour * 3600 + other.minute *60 + other.second
        M=(Total2-Total1)/60 
        return M
    
    def time_comp(self,other):
        Total1=self.hour * 3600 + self.minute * 60 + self.second
        Total2=other.hour * 3600 + other.minute *60 + other.second
        if Total1 > Total2 :
            return True
        elif Total1 <= Total2 :
            return False
        
    def time_within(self,other1,other2):
        Total1 = (self.hour*3600 + self.minute *60 + self.second) 
        Total2 = other1.hour * 3600 + other1.minute *60 + other1.second
        Total3 = other2.hour * 3600 + other2.minute *60 + other2.second 
        
        if Total2>=Total1 and Total2<=Total3:
            return True
        else:
            return False
        
    def 
        
