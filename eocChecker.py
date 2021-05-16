import datetime
from threading import Timer
import time
from tkinter.constants import COMMAND, END, FALSE
import urllib.request as urllib2
import tkinter as tk
from tkinter import ttk
import time as t
from tkinter import messagebox
import googlesearch
import webbrowser
from bs4 import BeautifulSoup
import re
from urllib.request import url2pathname
from urllib.request import url2pathname
import urllib
import urllib3
import pyautogui
import requests
import sys
import os
from tkinter import Tk, Label, Button
from pynput import keyboard
import time
import random






window = tk.Tk()

window.title("dev-longknives") 
window.minsize(600,400) 

buttonClicked = False
everyone = False


   

date = datetime.datetime.today()     


def gui(buttonClicked, everyone):
 











 if(buttonClicked == True):
    result = name1.get()
    result1 = name2.get()

    full = result * .7
    full1 = result1 * .3

    result3 = (full + full1)
   
    print("Percentage: " )
    print(result3 )

    
 label = ttk.Label(window, text = "Percent: ") 
 label.grid(column = 10, row = 6) 
 label = ttk.Label(window, text =(int) (result3)) 
 label.grid(column = 11, row = 6) 



 












label = ttk.Label(window, text = "Grade") # text
label.grid(column = 0, row = 3) 


name1 = tk.DoubleVar()
nameEntered1 = ttk.Entry(window, width = 15, textvariable = name1)
nameEntered1.grid(column = 10, row = 3) 


 






name2 = tk.DoubleVar()

nameEntered2 = ttk.Entry(window, width = 15, textvariable = name2)
nameEntered2.grid(column = 10, row = 4) 



label = ttk.Label(window, text = "Eoc") 
label.grid(column = 0, row = 4) 












button1 = ttk.Button(window, text = "Calculate ", command=lambda buttonClicked = True:gui(buttonClicked, everyone))
             
button1.grid(column= 10, row = 5) 








window.mainloop()
