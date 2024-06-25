
from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import math
from xlwt import *
import xlwt
from openpyxl.workbook import Workbook
import pandas as pd
import os
#from new_homo_sand import new_homo_sand

root=Tk()
root.geometry("1360x768")
root.title("Heterogenous or multilayer sandy soil")

class Example(Frame):
    
    def __init__(self, parent):
        
        Frame.__init__(self, parent)
        #new_homo_sand.__init__(self, master )
        self.canvas = Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.default_page()

    def default_page(self):
        '''Put in some fake data'''

        #labels
        #Label(self.frame, text= "Select the unit system").grid(row=0, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Enter No of layers").grid(row=1, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Enter diamter").grid(row=2, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Enter water table depth").grid(row=3, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Enter L/D").grid(row=4, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Name of File").grid(row=7, column=3, padx= 10, pady=10)

        #Label(self.frame, text = "Nq").grid(row=5, column=0, padx= 10, pady=10)
        

        
        #Label(self.frame, text = "Enter Length").grid(row=1, column=0, padx= 10, pady=10)   
        #Label(self.frame, text = "Enter Φ").grid(row=4, column=0, padx= 10, pady=10)
        #Label(self.frame, text = "Enter Γ").grid(row=5, column=0, padx= 10, pady=10)
        #Label(self.frame, text = "Enter Ks").grid(row=6, column=0, padx= 10, pady=10)

        #entry variable initialisation
        self.layersEV = StringVar()
        self.diaEV = StringVar()
        self.gwtEV = StringVar()
        self.LDEV = StringVar()
        self.NameEV = StringVar()
        #self.Nq = StringVar()
        self.lengthEV = [0]*100
        self.ΓEV= [0]*100
        self.Γ_satEV = [0]*100
        self.ΦEV = [0]*100

        for i in range(100):
            self.lengthEV[i] = StringVar()
            self.ΓEV[i] = StringVar()
            self.Γ_satEV[i] = StringVar()
            self.ΦEV[i] = StringVar()

        
    
        #entry widget
        Entry(self.frame, textvariable=self.layersEV).grid(row=1, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.diaEV).grid(row=2, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.gwtEV).grid(row=3, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.LDEV).grid(row=4, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.NameEV).grid(row=7, column=4, padx= 10, pady=10)
        #self.NqEW = Entry(self.frame, textvariable=self.Nq)
        #self.NqEW.grid(row=5, column=1, padx= 10, pady=10)
    



        #buttons
        Button(self.frame, text="Proceed", command= self.Proceed).grid(row=1, column=2, padx=10, pady=10)
        Button(self.frame, text="Submit", command= self.get_val).grid(row=1, column=3, padx=10, pady=10)
        Button(self.frame, text="Reset", command= self.Reset).grid(row=1, column=4, padx=10, pady=10)
        Button(self.frame, text="print", command= self.Print).grid(row=1, column=5, padx=10, pady=10)
        Button(self.frame, text="Export", command= self.Export).grid(row=1, column=6, padx=10, pady=10)
    
    def Proceed(self):

        for i in range(int(self.layersEV.get())):
            Label(self.frame, text=f"Enter the length of layer {i+1}").grid(row = (2*(2*(i+1))+1), column=0, padx=10, pady=5)
            Label(self.frame, text=f"Enter the Γ of layer {i+1}").grid(row = (2*(2*(i+1))+1) +1, column=0, padx=10, pady=5)
            Label(self.frame, text=f"Enter the Γ_sat of layer {i+1}").grid(row = (2*(2*(i+1))+1) +2, column=0, padx=10, pady=5)
            Label(self.frame, text=f"Enter the Φ of layer {i+1}").grid(row = (2*(2*(i+1))+1) +3, column=0, padx=10, pady=5)

            Entry(self.frame, textvariable=self.lengthEV[i]).grid(row=(2*(2*(i+1))+1), column=1, padx= 10, pady=10)
            Entry(self.frame, textvariable=self.ΓEV[i]).grid(row=(2*(2*(i+1))+1) +1, column=1, padx= 10, pady=10)
            Entry(self.frame, textvariable=self.Γ_satEV[i]).grid(row=(2*(2*(i+1))+1) +2, column=1, padx= 10, pady=10)
            Entry(self.frame, textvariable=self.ΦEV[i]).grid(row=(2*(2*(i+1))+1) +3, column=1, padx= 10, pady=10)
            

            
        self.Qb = []
        self.Qf = []
        self.Qu = []
        self.L = []
        self.q = []
        self.ks = []
        self.δ = []
        self.d = []
        self.l = []

        self.length = [0]*100
        self.Γ = [0]*100
        self.Γ_sat = [0]*100
        self.Φ = [0]*100

        

    def Reset(self):
        self.QbEW.delete(0, END)
        self.QfEW.delete(0, END)
        self.QuEW.delete(0, END)

        for i in range (int(self.layersEV.get()) + 1):
            self.length[i] = 0
            self.Γ[i] = 0
            self.Γ_sat[i] = 0
            self.Φ[i] = 0
        
        self.q = []
        self.ks = []
        self.δ = []
        

    def get_val(self):
       

        for i in range(int(self.layersEV.get())):
            #print(i)
            self.length[i] = float(self.lengthEV[i].get())
            self.Γ[i] = float(self.ΓEV[i].get())
            self.Γ_sat[i] = float(self.Γ_satEV[i].get())
            self.Φ[i] = float(self.ΦEV[i].get())

        #print(self.length)
        x=0
        self.flag = 0
        #print(1)
        #while self.flag == 0:
            #print(2)
        for i in range(int(self.layersEV.get())):
            
            if self.flag == 0:
                #print(3)
                x=0
                for j in range(i+1):
                    x = x + self.length[j]
                #print(x)
                if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
                   #print(x - float(self.gwtEV.get()))
                   #print(self.length[j] - (x - float(self.gwtEV.get())))
                   self.y = self.length[j] - (x - float(self.gwtEV.get()))
                   self.length.remove(self.length[j])
                   self.length.insert(j,self.y)  
                   self.length.insert(j+1,x - float(self.gwtEV.get())) 
                   self.Γ.insert(j, self.Γ[j])
                   self.Γ_sat.insert(j, self.Γ_sat[j])
                   self.Φ.insert(j, self.Φ[j])
                   self.j = j 
                   break  
                          
        #print(self.length)
        #print(self.Γ)
        #print(self.Γ_sat)
        #print(self.Φ)
        #print(self.j)

        
        self.x= 0
        if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
            for i in range(self.j+1):
                for k in range(i):
                    self.x = self.x + (self.length[k]*self.Γ[k])
                self.x = self.x + 0.5*self.length[i]*self.Γ[i]
                self.q.append(self.x)
                self.x=0

        self.x = 0
        if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
            for i in range(self.j + 1, (int(self.layersEV.get())+1)):
                for k in range(i):
                    self.x = self.x + (self.length[k]*(self.Γ_sat[k] - 10))
                self.x = self.x + 0.5*self.length[i]*(self.Γ_sat[i] - 10)
                self.q.append(self.x)
                self.x=0
        
        self.x = 0
        if float(self.gwtEV.get()) >= sum(self.length) :
            for i in range((int(self.layersEV.get()))):
                for k in range(i):
                    self.x = self.x + (self.length[k]*self.Γ[k])
                self.x = self.x + 0.5*self.length[i]*self.Γ[i]
                self.q.append(self.x)
                self.x=0


        #print(self.q)

        #print(self.Φ)
        for i in range ((int(self.layersEV.get())+1)):
            #self.Φ[i] = (self.Φ[i]*math.pi)/180
            #self.ks.append(0.5*(np.tan((45 + (self.Φ[i]/2))*(math.pi/180))*(np.tan((45 + (self.Φ[i]/2))*(math.pi/180)))))
            self.ks.append((0.5*np.tan((45 + (self.Φ[i]/2))*(math.pi/180))*np.tan((45 + (self.Φ[i]/2))*(math.pi/180))))
        #print(self.ks)
    
        for i in range (int(self.layersEV.get())+1):
            self.δ.append((np.tan(0.75*self.Φ[i]*(math.pi/180))))
        #print(self.δ)

        self.dia = float(self.diaEV.get())
        self.t = 0

        if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
            for i in range((int(self.layersEV.get())+1)):
                self.t = float((3.14159)*(self.dia)*(self.length[i])*(self.q[i])*(self.ks[i])*(self.δ[i])) + self.t
        
        if float(self.gwtEV.get()) >= sum(self.length) :
            for i in range((int(self.layersEV.get()))):
                self.t = float((3.14159)*(self.dia)*(self.length[i])*(self.q[i])*(self.ks[i])*(self.δ[i])) + self.t
        
        self.Qf.append(self.t)

    
        print(self.Qf)
        
        self.b = 0
        if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
            for i in range(self.j + 1):
                self.b = self.b + self.length[i]*self.Γ[i]
                #print(self.b)
        

        if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
            for i in range(self.j + 1, (int(self.layersEV.get())+1)):
                self.b =self.b + self.length[i]*(self.Γ_sat[i] - 10)
                #print(self.b)

        
        if float(self.gwtEV.get()) >= sum(self.length) :
            self.b = 0
            for i in range((int(self.layersEV.get()))):
                self.b = self.b + self.length[i]*self.Γ[i]
            #print(self.b)

        print(self.b)

#getting value of Nq

        if (x - float(self.gwtEV.get())) > 0 and float(self.gwtEV.get()) < sum(self.length) :
            self.Φ_last = self.Φ[(int(self.layersEV.get()))]  
            print(self.Φ_last)

        if float(self.gwtEV.get()) >= sum(self.length) :
            self.Φ_last = self.Φ[(int(self.layersEV.get())-1)]
            print(self.Φ_last)


        if float(self.Φ_last) == 25:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.Φ_last))) + 2.741)
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.Φ_last))) + 2.5274)
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.Φ_last))) + 2.341)
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.Φ_last))) + 2.1564)
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.Φ_last))) + 1.9517)
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.Φ_last))) + 1.7572)
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.Φ_last))) + 1.586)
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.Φ_last))) + 1.48)
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.Φ_last))) + 1.4)
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.Φ_last))) + 1.32)
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.Φ_last))) + -1.25)
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.Φ_last))) + 1.16)
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.Φ_last))) + 1.08)
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.Φ_last))) + 1)
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.Φ_last))) + 0.9)

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.Φ_last))) + 0.83)
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.Φ_last))) + 0.76)
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.Φ_last))) + 0.66)
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.Φ_last))) + 0.58)
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.Φ_last))) + 0.51)
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.Φ_last))) + 0.42)
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.Φ_last))) + 0.35)
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.Φ_last))) + 0.47)
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.Φ_last))) + 0.19)
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.Φ_last))) + 0.12)
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.Φ_last))) + 0.03)
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.Φ_last))) )


        if float(self.Φ_last) == 30:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.Φ_last))) + 1.019)
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.Φ_last))) + 0.9623)
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.Φ_last))) + 0.9128)
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.Φ_last))) + 0.821)
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.Φ_last))) + 0.806)
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.Φ_last))) + 0.752)
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.Φ_last))) + 0.645)
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.Φ_last))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.Φ_last))) )            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.Φ_last))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.Φ_last))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.Φ_last))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.Φ_last))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.Φ_last))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.Φ_last))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.Φ_last))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.Φ_last))) )
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.Φ_last))) )
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.Φ_last))) )
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.Φ_last))) )
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.Φ_last))) )
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.Φ_last))) )
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.Φ_last))) )
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.Φ_last))) )
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.Φ_last))) )
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.Φ_last))) )
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.Φ_last))) )

        if float(self.Φ_last) == 35:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.Φ_last))))
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.Φ_last))))
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.Φ_last))))
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.Φ_last))))
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.Φ_last))))
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.Φ_last))))
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.Φ_last))))
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.Φ_last))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.Φ_last))) )
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.Φ_last))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.Φ_last))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.Φ_last))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.Φ_last))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.Φ_last))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.Φ_last))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.Φ_last))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.Φ_last))) )
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.Φ_last))) )
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.Φ_last))) )
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.Φ_last))))
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.Φ_last))))
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.Φ_last))) )
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.Φ_last))))
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.Φ_last))))
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.Φ_last))))
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.Φ_last))))
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.Φ_last))))

        if float(self.Φ_last) == 40:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.Φ_last)))+5.707)
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.Φ_last)))+5.603)
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.Φ_last)))+4.6102)
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.Φ_last)))+3.902)
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.Φ_last)))+2.545)
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.Φ_last)))+1.518)
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.Φ_last)))+0.6531)
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.Φ_last))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.Φ_last))) )
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.Φ_last))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.Φ_last))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.Φ_last))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.Φ_last))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.Φ_last))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.Φ_last))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.Φ_last))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.Φ_last))) + 1.586)
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.Φ_last))) - 1.11)
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.Φ_last))) -1.23)
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.Φ_last)))- 1.11)
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.Φ_last))) -1.17)
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.Φ_last))) -1.51)
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.Φ_last))) )
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.Φ_last))) - 1.846)
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.Φ_last))) - 1.84)
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.Φ_last))) - 2.01)
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.Φ_last))) - 2.5)


        if 25 < float(self.Φ_last) < 40 and float(self.Φ_last) != 25 or 30 or 35 or 40:
            if 0 <= float(self.LDEV.get()) <= 5 :
                self.Nq = (0.0872*(2.71828**(0.1892*float(self.Φ_last))))
            if 5 < float(self.LDEV.get()) <= 7.5 :
                self.Nq = (0.0816*(2.71828**(0.1901*float(self.Φ_last))))
            if 7.5 < float(self.LDEV.get()) <= 10 :
                self.Nq = (0.0749*(2.71828**(0.1916*float(self.Φ_last))))
            if 10 < float(self.LDEV.get()) <= 12.5 :
                self.Nq = (0.0683*(2.71828**(0.1932*float(self.Φ_last))))
            if 12.5 < float(self.LDEV.get()) <= 15 :
                self.Nq = (0.062*(2.71828**(0.195*float(self.Φ_last))))
            if 15 < float(self.LDEV.get()) <= 17.5 :
                self.Nq = (0.0559*(2.71828**(0.1969*float(self.Φ_last))))
            if 17.5 < float(self.LDEV.get()) <= 20 :
                self.Nq = (0.0497*(2.71828**(0.1991*float(self.Φ_last))))
            
            if 20 < float(self.LDEV.get()) <= 22.5 :
                self.Nq = (0.0484*(2.71828**(0.1996*float(self.Φ_last))) )
            
            if 22.5 < float(self.LDEV.get()) <= 25 :
                self.Nq = (0.0468*(2.71828**(0.2003*float(self.Φ_last))) )
            
            if 25 < float(self.LDEV.get()) <= 27.5 :
                self.Nq = (0.0452*(2.71828**(0.201*float(self.Φ_last))) )
            
            if 27.5 < float(self.LDEV.get()) <= 30 :
                self.Nq = (0.0437*(2.71828**(0.2017*float(self.Φ_last))) )
           
            if 30 < float(self.LDEV.get()) <= 32.5 :
                self.Nq = (0.0422*(2.71828**(0.2024*float(self.Φ_last))) )
            
            if 32.5 < float(self.LDEV.get()) <= 35 :
                self.Nq = (0.0407*(2.71828**(0.2031*float(self.Φ_last))) )
            
            if 35 < float(self.LDEV.get()) <= 37.5 :
                self.Nq = (0.0392*(2.71828**(0.2039*float(self.Φ_last))) )
            
            if 37.5 < float(self.LDEV.get()) <= 40 :
                self.Nq = (0.0378*(2.71828**(0.2047*float(self.Φ_last))) )

            if 40 < float(self.LDEV.get()) <= 42.5 :
                self.Nq = (0.0364*(2.71828**(0.2055*float(self.Φ_last))) )
            
            if 42.5 < float(self.LDEV.get()) <= 45 :
                self.Nq = (0.0349*(2.71828**(0.2063*float(self.Φ_last))) )
            
            if 45 < float(self.LDEV.get()) <= 47.5 :
                self.Nq = (0.0336*(2.71828**(0.2072*float(self.Φ_last))) )
            
            if 47.5 < float(self.LDEV.get()) <= 50 :
                self.Nq = (0.0322*(2.71828**(0.2081*float(self.Φ_last))) )
            
            if 50 < float(self.LDEV.get()) <= 52.5 :
                self.Nq = (0.0308*(2.71828**(0.209*float(self.Φ_last))))
            
            if 52.5 < float(self.LDEV.get()) <= 55 :
                self.Nq = (0.0295*(2.71828**(0.2099*float(self.Φ_last))))
            
            if 55 < float(self.LDEV.get()) <= 57.5 :
                self.Nq = (0.0282*(2.71828**(0.2109*float(self.Φ_last))) )
            
            if 57.5 < float(self.LDEV.get()) <= 60 :
                self.Nq = (0.0269*(2.71828**(0.2119*float(self.Φ_last))) )
            
            if 60 < float(self.LDEV.get()) <= 62.5 :
                self.Nq = (0.0257*(2.71828**(0.2129*float(self.Φ_last))) )
            
            if 62.5 < float(self.LDEV.get()) <= 65 :
                self.Nq = (0.0244*(2.71828**(0.214*float(self.Φ_last))) )
            
            if 65 < float(self.LDEV.get()) <= 67.5 :
                self.Nq = (0.0232*(2.71828**(0.2151*float(self.Φ_last))) )
            
            if 67.5 < float(self.LDEV.get()) <= 70 :
                self.Nq = (0.0222*(2.71828**(0.2161*float(self.Φ_last))) )

        print(self.Nq)

        self.u = ((self.Nq*self.b*3.14159*self.dia*self.dia)/4) #CALC Qb
        self.v = self.u + self.t  #calc Qu
        
        self.Qb.append(self.u)
        self.Qu.append(self.v)


        Label(self.frame, text= "Qb").grid(row=3, column=3, pady=10, padx=5)
        Label(self.frame, text= "Qf").grid(row=3, column=4, pady=10, padx=5)
        Label(self.frame, text= "Qu").grid(row=3, column=5, pady=10, padx=5)
        
        self.QbEW = Entry(self.frame)
        self.QbEW.grid(row=4, column=3, pady=10, padx=5)
        self.QfEW = Entry(self.frame)
        self.QfEW.grid(row=4, column=4, pady=10, padx=5)
        self.QuEW = Entry(self.frame)
        self.QuEW.grid(row=4, column=5, pady=10, padx=5)

        self.QbEW.insert(0, self.u)
        self.QfEW.insert(0, self.t)
        self.QuEW.insert(0, self.v)
    

        self.d.append(self.dia)
        self.l.append(sum(self.length))

   
    
    
    def Print(self):
        
        print(self.Qf)
        print(self.Qb)
        print(self.Qu)
        # print(self.Φ)
        # print(self.Φ[(int(self.layersEV.get()))])
        # print(self.ks)
        # print(self.δ)
        # print(self.q)
        # print(self.dia)
        # print(self.length)

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

        for i in range(len(self.Qb)):
            self.tv.insert('', i, values= (i+1, self.l[i], self.d[i], "{:.2f}".format(self.Qb[i]), "{:.2f}".format(self.Qf[i]), "{:.2f}".format(self.Qu[i])))

    def Export(self):
        
        self.Name = self.NameEV.get()
        a_list = [str(self.Name), '.csv']

        FN = ''.join(a_list)
        dirname = os.path.dirname(__file__)
        filename1 = os.path.join(dirname, FN)
        dict = {'Length': self.l, 'Diameter': self.d, 'Qb': self.Qb, 'Qf' : self.Qf, 'Qu':self.Qu}
        df = pd.DataFrame(dict) 
        df.to_csv(f"{filename1}", header=True, index=False)
        #print(1)
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

        # #os.chmod("C:\Users\Addi\Documents\python\New_hetro_clay2.xls")

        # #saving the excel to location described, here b4 location r is used !
        # self.wb.save(r"C:\Users\Addi\Documents\python\New_hetro_sand.xls")
    
    
    
    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


example = Example(root)
example.pack(side="top", fill="both", expand=True)
root.mainloop()