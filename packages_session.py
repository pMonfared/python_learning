# Built_in Packages
# This kind of packages will install at the same time with Python installation
import math
import os

# p number (عدد پی)
print(math.pi)

# جذر
print(math.sqrt(16)) 

path = "C:/MyProjectFolder"
filename= "image.jpg"

print(os.path.join(path, filename))

# Not Built_in Packages
# This kind of packages must install as Third-party package in command line(powershell) by this command:
# pip install <package-name>
# pip show <package-name>
# pip uninstall <package-name>
# install a specific package version
# pip install <package-name>==<version-number>
# sometimes maybe watch a permission error, in this case, just try install it by Run as administator without any special privileges:
# pip install <package-name> --user
import numpy as np
import pandas as ps
# import gradio as gr
import cv2 as cv


# Internal project's packages
import myPackage

print(myPackage.func_add_numbers(2,6))