# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:21:40 2020

@author: User
"""

import random
pf=0


for i in range (0,5):
   i=random.randint(0,1)
   if(i==0):
      print("State: Dirty")
      
      j=random.randint(0,1)
      if(j==1):
         print("Successfully cleaned ")
         pf=pf+1
      else:
         print("failure to clean")
         
      
         
      
      
      
   else:
      print("It is already Clean")
      pf=pf+0

print("Performance Score:",pf)