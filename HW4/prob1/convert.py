from math import *
# This code converts the angle of declination and right ascension to radians
class Radian:
    def __init__(self,value1:float, value2:float, value3:float):
        self.value1=value1
        self.value2=value2
        self.value3=value3
    def RA2rad(self): # computes the right ascension angle in radians
        deg=(self.value1*15)+(self.value2*(15/60))+(self.value3*(15/3600))
        if deg > 180.0:  return radians(deg-360.0) # ensures that the angle lies between -180 and +180
        return radians(deg)
    def DEC2rad(self): # computes the declination angle in radians
        deg=self.value1 + (self.value2*(1/60))+ (self.value3*(1/3600))
        return radians(deg)
