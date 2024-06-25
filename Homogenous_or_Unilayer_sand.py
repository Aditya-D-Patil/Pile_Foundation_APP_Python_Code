from tkinter import *
from typing import List
from tkinter import ttk
import pandas as pd
from openpyxl.workbook import Workbook
from xlwt import *
import math
import xlwt
import numpy as np
import os


# root = Tk()
# root.geometry("1366x768")


class new_homo_sand:

    def __init__(self, master): 
        #Label(master, text="Select the unit system").grid(row=0, column=0, padx= 10, pady=10)
        Label(master, text = "Enter Length").grid(row=1, column=0, padx= 10, pady=10)
        Label(master, text = "Enter diamter").grid(row=2, column=0, padx= 10, pady=10)
        Label(master, text = "Enter water table depth").grid(row=3, column=0, padx= 10, pady=10)
        Label(master, text = "Enter Φ").grid(row=4, column=0, padx= 10, pady=10)
        Label(master, text = "Enter Γ").grid(row=5, column=0, padx= 10, pady=10)
        Label(master, text = "Enter Ks").grid(row=6, column=0, padx= 10, pady=10)
        Label(master, text = "Enter L/D").grid(row=7, column=0, padx= 10, pady=10)
        Label(master, text = "Nq").grid(row=8, column=0, padx= 10, pady=10)
        Label(master, text = "Qb").grid(row=9, column=0, padx= 10, pady=10)
        Label(master, text = "Qf").grid(row=10, column=0, padx= 10, pady=10)
        Label(master, text = "Qu").grid(row=11, column=0, padx= 10, pady=10)
        Label(master, text = "Name of File").grid(row=12, column=0, padx= 10, pady=10)

        self.LengthEV = StringVar()
        self.diaEV = StringVar()
        self.gwtEV = StringVar()
        self.ΦEV = StringVar()
        self.ΓEV = StringVar()
        self.KsEV = StringVar()
        self.LDEV = StringVar()
        self.Nq = StringVar()
        self.NameEV = StringVar()

        Entry(master, textvariable=self.LengthEV).grid(row=1, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.diaEV).grid(row=2, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.gwtEV).grid(row=3, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.ΦEV).grid(row=4, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.ΓEV).grid(row=5, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.KsEV).grid(row=6, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.LDEV).grid(row=7, column=1, padx= 10, pady=10)
        Entry(master, textvariable=self.NameEV).grid(row=12, column=1, padx= 10, pady=10)
        self.NqEW = Entry(master, textvariable=self.Nq)
        self.NqEW.grid(row=8, column=1, padx= 10, pady=10)
        self.QbEW = Entry(master)
        self.QbEW.grid(row=9, column=1, padx= 10, pady=10)
        self.QfEW = Entry(master)
        self.QfEW.grid(row=10, column=1, padx= 10, pady=10)
        self.QuEW = Entry(master)
        self.QuEW.grid(row=11, column=1, padx= 10, pady=10)


        self.B1 = Button(master, text="Get Nq", command = self.GetNq).grid(row=8, column=2, padx=10, pady=10)
        self.B2 = Button(master, text = "Submit", command = self.Submit).grid(row=8, column=3, padx=10, pady =10)
        self.B3 = Button(master, text = "Reset", command = self.Reset).grid(row=8, column=4, padx=10, pady =10)
        self.B4 = Button(master, text = "Print List", command = self.Print_list).grid(row=8, column=5, padx=10, pady =10)
        self.B5 = Button(master, text = "Export", command = self.Export).grid(row = 8, column = 6, padx =10, pady=10)

        self.Length_list = []
        self.dia_list = []
        self.Qb_list = []
        self.Qf_list = []
        self.Qu_list = []

    def GetNq(self):


        if float(self.ΦEV.get()) == 25:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.ΦEV.get()))) + 2.741)
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.ΦEV.get()))) + 2.5274)
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.ΦEV.get()))) + 2.341)
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.ΦEV.get()))) + 2.1564)
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.ΦEV.get()))) + 1.9517)
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.ΦEV.get()))) + 1.7572)
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.ΦEV.get()))) + 1.586)
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.ΦEV.get()))) + 1.48)
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.ΦEV.get()))) + 1.4)
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.ΦEV.get()))) + 1.32)
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.ΦEV.get()))) + -1.25)
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.ΦEV.get()))) + 1.16)
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.ΦEV.get()))) + 1.08)
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.ΦEV.get()))) + 1)
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.ΦEV.get()))) + 0.9)

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.ΦEV.get()))) + 0.83)
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.ΦEV.get()))) + 0.76)
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.ΦEV.get()))) + 0.66)
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.ΦEV.get()))) + 0.58)
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.ΦEV.get()))) + 0.51)
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.ΦEV.get()))) + 0.42)
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.ΦEV.get()))) + 0.35)
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.ΦEV.get()))) + 0.47)
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.ΦEV.get()))) + 0.19)
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.ΦEV.get()))) + 0.12)
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.ΦEV.get()))) + 0.03)
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.ΦEV.get()))) )
        
            self.NqEW.insert(0, "{:.2f}".format(self.Nq))

        if float(self.ΦEV.get()) == 30:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.ΦEV.get()))) + 1.019)
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.ΦEV.get()))) + 0.9623)
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.ΦEV.get()))) + 0.9128)
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.ΦEV.get()))) + 0.821)
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.ΦEV.get()))) + 0.806)
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.ΦEV.get()))) + 0.752)
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.ΦEV.get()))) + 0.645)
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.ΦEV.get()))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.ΦEV.get()))) )            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.ΦEV.get()))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.ΦEV.get()))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.ΦEV.get()))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.ΦEV.get()))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.ΦEV.get()))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.ΦEV.get()))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.ΦEV.get()))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.ΦEV.get()))) )
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.ΦEV.get()))) )
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.ΦEV.get()))) )
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.ΦEV.get()))) )
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.ΦEV.get()))) )
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.ΦEV.get()))) )
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.ΦEV.get()))) )
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.ΦEV.get()))) )
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.ΦEV.get()))) )
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.ΦEV.get()))) )
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.ΦEV.get()))) )
            
            self.NqEW.insert(0, "{:.2f}".format(self.Nq))

        if float(self.ΦEV.get()) == 35:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.ΦEV.get()))))
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.ΦEV.get()))))
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.ΦEV.get()))))
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.ΦEV.get()))))
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.ΦEV.get()))))
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.ΦEV.get()))))
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.ΦEV.get()))))
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.ΦEV.get()))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.ΦEV.get()))) )
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.ΦEV.get()))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.ΦEV.get()))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.ΦEV.get()))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.ΦEV.get()))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.ΦEV.get()))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.ΦEV.get()))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.ΦEV.get()))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.ΦEV.get()))) )
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.ΦEV.get()))) )
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.ΦEV.get()))) )
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.ΦEV.get()))))
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.ΦEV.get()))))
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.ΦEV.get()))) )
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.ΦEV.get()))))
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.ΦEV.get()))))
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.ΦEV.get()))))
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.ΦEV.get()))))
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.ΦEV.get()))))
            
            self.NqEW.insert(0, "{:.2f}".format(self.Nq))

        if float(self.ΦEV.get()) == 40:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.ΦEV.get())))+5.707)
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.ΦEV.get())))+5.603)
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.ΦEV.get())))+4.6102)
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.ΦEV.get())))+3.902)
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.ΦEV.get())))+2.545)
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.ΦEV.get())))+1.518)
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.ΦEV.get())))+0.6531)
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.ΦEV.get()))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.ΦEV.get()))) )
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.ΦEV.get()))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.ΦEV.get()))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.ΦEV.get()))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.ΦEV.get()))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.ΦEV.get()))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.ΦEV.get()))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.ΦEV.get()))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.ΦEV.get()))) + 1.586)
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.ΦEV.get()))) - 1.11)
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.ΦEV.get()))) -1.23)
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.ΦEV.get())))- 1.11)
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.ΦEV.get()))) -1.17)
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.ΦEV.get()))) -1.51)
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.ΦEV.get()))) )
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.ΦEV.get()))) - 1.846)
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.ΦEV.get()))) - 1.84)
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.ΦEV.get()))) - 2.01)
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.ΦEV.get()))) - 2.5)
            
            self.NqEW.insert(0, "{:.2f}".format(self.Nq))

        if 25 < float(self.ΦEV.get()) < 40 and float(self.ΦEV.get()) != 25 or 30 or 35 or 40:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.ΦEV.get()))))
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.ΦEV.get()))))
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.ΦEV.get()))))
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.ΦEV.get()))))
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.ΦEV.get()))))
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.ΦEV.get()))))
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.ΦEV.get()))))
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.ΦEV.get()))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.ΦEV.get()))) )
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.ΦEV.get()))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.ΦEV.get()))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.ΦEV.get()))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.ΦEV.get()))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.ΦEV.get()))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.ΦEV.get()))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.ΦEV.get()))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.ΦEV.get()))) )
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.ΦEV.get()))) )
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.ΦEV.get()))) )
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.ΦEV.get()))))
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.ΦEV.get()))))
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.ΦEV.get()))) )
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.ΦEV.get()))) )
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.ΦEV.get()))) )
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.ΦEV.get()))) )
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.ΦEV.get()))) )
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.ΦEV.get()))) )

            self.NqEW.insert(0, "{:.2f}".format(self.Nq))


    def Submit(self):
        self.a = float(self.gwtEV.get())
        self.d = float(self.diaEV.get() )
        self.L = float(self.LengthEV.get())
        self.b = float(self.LengthEV.get() ) - self.a
        self.Γ = float(self.ΓEV.get())
        self.Γsub = float(self.Γ - 10)
        self.Nq = float(self.Nq)
        self.Ks = float(self.KsEV.get())
        self.Φ = float(self.ΦEV.get())
        self.delta = 0.75*(self.Φ)*(math.pi/180)

        if  0 <= self.Φ <2.5:
            self.NΓ = 0
        if  2.5 <= self.Φ <5:
            self.NΓ = 0.225
        if  5 <= self.Φ <7.5:
            self.NΓ = 0.45
        if  7.5 <= self.Φ <10:
            self.NΓ = 0.835
        if  10 <= self.Φ <12.5:
            self.NΓ = 1.22
        if  12.5 <= self.Φ <15:
            self.NΓ = 1.935
        if  15 <= self.Φ <17.5:
            self.NΓ = 2.65
        if  17.5 <= self.Φ <20:
            self.NΓ = 4.02
        if  20 <= self.Φ <22.5:
            self.NΓ = 5.39
        if  22.5 <= self.Φ <25:
            self.NΓ = 8.135
        if  25 <= self.Φ <27.5:
            self.NΓ = 10.88
        if  27.5 <= self.Φ <30:
            self.NΓ = 16.64
        if  30 <= self.Φ <32.5:
            self.NΓ = 22.40
        if  32.5 <= self.Φ <35:
            self.NΓ = 35.225
        if  35 <= self.Φ <37.5:
            self.NΓ = 48.03
        if  37.5 <= self.Φ <40:
            self.NΓ = 78.73
        if  40 <= self.Φ <42.5:
            self.NΓ = 109.41
        if  42.5 <= self.Φ <45:
            self.NΓ = 190.585
        if  45 <= self.Φ <47.5:
            self.NΓ = 271.76
        if  47.5 <= self.Φ <50:
            self.NΓ = 517.325

        if   self.Φ == 50:
            self.NΓ = 762.89
        
        if self.a >= self.L:
            self.b = 0
            self.a = self.L
            

        if self.a >= self.L:
            self.QB1 = (0.5*self.d*self.NΓ*self.Γ*(3.14*self.d*self.d/4))
        else:
            self.QB1 = (0.5*self.d*self.NΓ*self.Γsub*(3.14*self.d*self.d/4))


        self.Qb = ((3.14*self.d*self.d/4)*((self.Γ*self.a) + (self.Γsub*self.b))*self.Nq) + self.QB1
        print(self.a , self.d , self.b, self.Qb, self.QB1)

        if self.a < self.L:
            
            self.Qf_sub = (1/2)*((self.Γ*self.a) + (self.Γ*self.a) + (self.Γsub*self.b))*3.14*self.L*self.d*self.Ks*np.tan(self.delta)
            self.Qf_dry = (1/2)*(self.Γ*self.a)*3.14*self.a*self.d*self.Ks*np.tan(self.delta)
            self.Qf = self.Qf_dry + self.Qf_sub
        else:
            self.Qf = (1/2)*((self.Γ*self.L))*3.14*self.d*self.L*self.Ks*np.tan(self.delta)


        print(self.L, self.Γ, self.d,  self.Ks, np.tan(self.delta), self.delta)

        self.Qu = self.Qb + self.Qf
        
        self.QbEW.insert(0, "{:.2f}".format(self.Qb))
        self.QfEW.insert(0, "{:.2f}".format(self.Qf))
        self.QuEW.insert(0, "{:.2f}".format(self.Qu))

        self.Qb_list.append("{:.2f}".format(self.Qb))
        self.Qf_list.append("{:.2f}".format(self.Qf))
        self.Qu_list.append("{:.2f}".format(self.Qu))
        self.Length_list.append(self.L)
        self.dia_list.append(self.d)

    def Reset(self):
        self.QbEW.delete(0, END)
        self.QfEW.delete(0, END)
        self.QuEW.delete(0, END)
        self.NqEW.delete(0, END)

    def Print_list(self):
        print(self.Qb_list, self.Qf_list, self.Qu_list ,self.Length_list, self.dia_list)

         #to form window on click
        self.newwin = Toplevel(root) 
        self.newwin.geometry("1366x768")
        


        self.tv = ttk.Treeview(self.newwin, height = 70)
        self.tv['columns']=('SR.NO', 'Length', 'Diameter', 'Qb', 'Qf', 'Qu')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('SR.NO', anchor=CENTER, width=70)
        self.tv.column('Length', anchor=CENTER, width=100)
        self.tv.column('Diameter', anchor=CENTER, width=100)
        self.tv.column('Qb', anchor=CENTER, width=100)
        self.tv.column('Qf', anchor=CENTER, width=100)
        self.tv.column('Qu', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('SR.NO', text='SR.NO', anchor=CENTER)
        self.tv.heading('Length', text='Length', anchor=CENTER)
        self.tv.heading('Diameter', text='Diameter', anchor=CENTER)
        self.tv.heading('Qb', text='Qb', anchor=CENTER)
        self.tv.heading('Qf', text='Qf', anchor=CENTER)
        self.tv.heading('Qu', text='Qu', anchor=CENTER)

        self.scrollbar = Scrollbar(self.newwin, orient=VERTICAL, command = self.tv.yview).grid(row =0, column=1, sticky=NS)
        self.tv.grid(row =0, column = 5, sticky= NSEW)

        for i in range(len(self.Qb_list)):
            self.tv.insert('', i, values= (i+1, self.Length_list[i], self.dia_list[i], (self.Qb_list[i]), (self.Qf_list[i]), (self.Qu_list[i])))

    def Export(self):
        #print(1)

        self.Name = self.NameEV.get()
        a_list = [str(self.Name), '.csv']

        FN = ''.join(a_list)

        dirname = os.path.dirname(__file__)
        filename1 = os.path.join(dirname, FN)
        dict = {'Length': self.Length_list, 'Diameter': self.dia_list, 'Qb': self.Qb_list, 'Qf' : self.Qf_list, 'Qu':self.Qu_list}
        df = pd.DataFrame(dict) 
        df.to_csv(f"{filename1}", header=True, index=False)
        # self.wb = Workbook()
        # self.sheet1 = self.wb.add_sheet('Sheet 1',  cell_overwrite_ok=True)

        # #making headings bold
        # self.style = xlwt.easyxf('font: bold 1')
        # self.sheet1.write(0, 0, 'SR.NO' , self.style)
        # self.sheet1.write(0, 1, 'Length', self.style)
        # self.sheet1.write(0, 2, 'Diameter', self.style)
        # self.sheet1.write(0, 3, 'Qb', self.style)
        # self.sheet1.write(0, 4, 'Qf', self.style)
        # self.sheet1.write(0, 5, 'Qu', self.style)


        # #writting data to excel
        # for i in range(len(self.Qb_list)):
        #     self.sheet1.write(i+1, 0, i+1)
        #     self.sheet1.write(i+1, 1, self.Length_list[i])
        #     self.sheet1.write(i+1, 2, self.dia_list[i])
        #     self.sheet1.write(i+1, 3, self.Qb_list[i])
        #     self.sheet1.write(i+1, 4, self.Qf_list[i])
        #     self.sheet1.write(i+1, 5, self.Qu_list[i])
        #     print("Export")

        #os.chmod("C:\Users\Addi\Documents\python\New_hetro_clay2.xls")

        #saving the excel to location described, here b4 location r is used !
        #self.wb.save(r"C:\Users\Addi\Documents\python\New_homo_sand.xls")

#a = new_homo_sand(root)

#root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry("1366x768")
    a = new_homo_sand(root)

    root.mainloop()