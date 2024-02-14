#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:54:02 2024

@author: mauricio
"""

import os
import pathlib
import platform

myfolder = pathlib.Path.cwd()
print(myfolder)
myfile = myfolder/'files'/'example.txt'
print(myfile)
if platform.system() == "Windows":
    os.system(f"explorer {myfile}") 
elif platform.system() == "Darwin":
    os.system(f"open {myfile}") 
else:
    os.system(f"xdg-open {myfile}")