from ast import Pass
from tkinter import *
from typing import List
from tkinter import ttk
import pandas as pd
from openpyxl.workbook import Workbook
from xlwt import *
import xlwt
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
import os


root=Tk()
root.geometry("1360x768")
root.title("Lateral Load by IS Code Method")

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

        #Checkbox variable
        self.C = IntVar()


        #Checkbox
        Radiobutton(self.frame, text= "Free Head", variable= self.C, value=1).grid(row= 0, column=1, padx= 5, pady=5 )
        Radiobutton(self.frame, text= "Fix Head", variable= self.C, value=2).grid(row= 0, column=2, padx= 5, pady=5 )


        #labels
        Label(self.frame, text = "Select the Boundary condition").grid(row=0, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Load").grid(row=1, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Young's Modulus").grid(row=2, column=0, padx= 10, pady=10)
        Label(self.frame, text = "MOI").grid(row=3, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Zf").grid(row=4, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Cantilever length 'e' ").grid(row=5, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Deflection y ").grid(row=6, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Fixed End Moment M ").grid(row=7, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Name of File ").grid(row=9, column=0, padx= 10, pady=10)


        #Entry variable initialization
        self.LoadEV = StringVar()
        self.EEV = StringVar()
        self.MOIEV = StringVar()
        self.ZEV = StringVar()
        self.CLEV = StringVar()
        self.NameEV = StringVar()

        #Entry Widget
        Entry(self.frame, textvariable=self.LoadEV).grid(row=1, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.EEV).grid(row=2, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.MOIEV).grid(row=3, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.ZEV).grid(row=4, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.CLEV).grid(row=5, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.NameEV).grid(row=9, column=1, padx= 10, pady=10)
        
        #Entry widget for result output
        self.YEW = Entry(self.frame)
        self.YEW.grid(row=6, column=1, padx= 10, pady=10)
        self.DEW = Entry(self.frame)
        self.DEW.grid(row=7, column=1, padx= 10, pady=10)

        #Buttons
        Button(self.frame, text="Submit", command = self.Submit).grid(row=5, column =2, padx=10, pady=10)
        Button(self.frame, text="Print Table", command = self.Print_list).grid(row=6, column =2, padx=10, pady=10)
        Button(self.frame, text="Graph Load vs Y and M", command= self.Graph).grid(row=6, column =3, padx=10, pady=10)
        Button(self.frame, text="Reset", command = self.Reset).grid(row=5, column =3, padx=10, pady=10)
        Button(self.frame, text="Exit", command=self.destroy).grid(row=7, column =2, padx=10, pady=10)
        Button(self.frame, text="Export", command=self.Export).grid(row=8, column =2, padx=10, pady=10)

        #List for storing data
        self.LoadList = []
        self.EList = []
        self.MOIList = []
        self.ZList = []
        self.CLList = []
        self.YList = []
        self.DList = []
    
    def Submit(self):
    
        #initialising values from entry widget variable to normal varialble 
        self.Load = float(self.LoadEV.get())
        self.E = float(self.EEV.get())
        self.MOI = float(self.MOIEV.get())
        self.Z = float(self.ZEV.get())
        self.CL = float(self.CLEV.get())
        # print(1)
        # print(self.Load)
        # print(2)

        #giving condition for free head
        if self.C.get() == 1:
            self.Y = float((self.Load*((self.CL  + self.Z)**3)*1000)/(3*self.E*self.MOI))
            self.D = float(self.Load*(self.CL + self.Z))
            self.YEW.insert(0, "{:.2f}".format(self.Y))
            self.DEW.insert(0, "{:.2f}".format(self.D))
        
        #giving condition for fixed head
        if self.C.get()==2:
            self.Y = float((self.Load*((self.CL  + self.Z)**3)*1000)/(12*self.E*self.MOI))
            self.D = float((self.Load*(self.CL + self.Z))/2)
            self.YEW.insert(0, "{:.2f}".format(self.Y))
            self.DEW.insert(0, "{:.2f}".format(self.D))
        

        #appending values in list created above to show comparative data table
        self.LoadList.append(self.Load)
        self.EList.append(self.E)
        self.MOIList.append(self.MOI)
        self.ZList.append(self.Z)
        self.CLList.append(self.CL)
        self.YList.append(self.Y)
        self.DList.append(self.D)

    def Graph(self):

        fig, axes = plt.subplots(nrows=1, ncols=2)

        self.x1 = self.YList
        self.y1 = self.LoadList
        plt.subplot(1,2,1)
        plt.xlabel("Deflection")
        plt.ylabel("Load")
        plt.title("Deflection vs Load")
        plt.plot(self.x1,self.y1)
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)


        self.x2 = self.DList
        self.y2 = self.LoadList
        plt.subplot(1,2,2)
        plt.xlabel("Moment")
        plt.ylabel("Load")
        plt.title("Moment vs Load")
        plt.plot(self.x2,self.y2)
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

        fig.tight_layout()
        plt.show()
    
    def Print_list(self):

         #to form window on click
        self.newwin = Toplevel(root) 
        self.newwin.geometry("1366x768")
        


        self.tv = ttk.Treeview(self.newwin, height = 70)
        self.tv['columns']=('SR.NO', 'Load', 'MOI', 'E', 'Z', 'CL', 'Y', 'D')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('SR.NO', anchor=CENTER, width=70)
        self.tv.column('Load', anchor=CENTER, width=100)
        self.tv.column('MOI', anchor=CENTER, width=100)
        self.tv.column('E', anchor=CENTER, width=100)
        self.tv.column('Z', anchor=CENTER, width=100)
        self.tv.column('CL', anchor=CENTER, width=100)
        self.tv.column('Y', anchor=CENTER, width=100)
        self.tv.column('D', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('SR.NO', text='SR.NO', anchor=CENTER)
        self.tv.heading('Load', text='Load', anchor=CENTER)
        self.tv.heading('MOI', text='MOI', anchor=CENTER)
        self.tv.heading('E', text='E', anchor=CENTER)
        self.tv.heading('Z', text='Z', anchor=CENTER)
        self.tv.heading('CL', text='Cantilever', anchor=CENTER)
        self.tv.heading('Y', text='Deflection', anchor=CENTER)
        self.tv.heading('D', text='Moment', anchor=CENTER)

        #attaching scrollbar
        self.scrollbar = Scrollbar(self.newwin, orient=VERTICAL, command = self.tv.yview).grid(row =0, column=1, sticky=NS)
        self.tv.grid(row =0, column = 5, sticky= NSEW)

        print(len(self.YList))

        for i in range(len(self.YList)):
            self.tv.insert('', i, values= (i+1,  "{:.2f}".format(self.LoadList[i]),  "{:.2f}".format(self.MOIList[i]),  "{:.2f}".format(self.EList[i]),  "{:.2f}".format(self.ZList[i]),  "{:.2f}".format(self.CLList[i]),  "{:.2f}".format(self.YList[i]),  "{:.2f}".format(self.DList[i])))


    #Resetting entry widget to null after every result
    def Reset(self):
        self.YEW.delete(0, END)
        self.DEW.delete(0, END)

    def Export(self):

        self.Name = self.NameEV.get()
        a_list = [str(self.Name), '.csv']

        FN = ''.join(a_list)
        dirname = os.path.dirname(__file__)
        filename1 = os.path.join(dirname, FN)
        dict = {'Load': self.LoadList, 'MOI': self.MOIList, 'Young Mod': self.EList, 'Zf' : self.ZList, 'Cantilever length':self.CLList, 'Deflection':self.YList, 'End Moment':self.DList}
        df = pd.DataFrame(dict) 
        df.to_csv(f"{filename1}", header=True, index=False)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


example = Example(root)
example.pack(side="top", fill="both", expand=True)
root.mainloop()
