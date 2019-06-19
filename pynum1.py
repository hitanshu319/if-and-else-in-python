#!/usr/bin/python3


import numpy as np
import subprocess

for i in range(2) :
   r=int(input("enter no. of rows...>>"))
   c=int(input("enter no. of columns....>>")) 
   q=np.random.randint(low=1,high=10,size=(r,c))
   print(q)
   n=input("enter the name of file..")
   np.savetxt(n,q)
   np.loadtxt(n)


