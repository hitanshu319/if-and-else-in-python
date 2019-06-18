#!/usr/bin/python3

import subprocess
n=input("enter ...")
subprocess.call(["qrencode" ,"-s" ,"16*16", "-o" ,"a.png",n])
print(n)
