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

root=Tk()
root.geometry("1360x768")
root.title("Heterogenous or multilayer clayey soil")

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
        self.LayerLabel = Label(self.frame, text="Enter the no. of layer")
        self.LayerLabel.grid(row=1, column=0, pady=10)
        # self.UnitLabel = Label(self.frame, text = "Select the Unit System")
        # self.UnitLabel.grid(row=0, column=0, pady=10)
        self.nEV = IntVar()
        self.nEW = Entry(self.frame, textvariable = self.nEV)
        self.nEW.grid(row=1, column=1, padx=10, pady =10)
        #rint(self.nEV.get())
        self.diaEV = StringVar()
        self.NameEV = StringVar()
        Label(self.frame, text="Enter the diameter").grid(row=3, column=0, pady=10)
        Entry(self.frame, textvariable=self.diaEV).grid(row=3, column=1, pady=10)
        Label(self.frame, text="Name of File").grid(row=7, column=3, pady=10)
        Entry(self.frame, textvariable=self.NameEV).grid(row=7, column=4, pady=10)
        Text(self.frame, height=2, width = 10).grid(row=0, column=10)

        self.B1 = Button(self.frame , text="Proceed", command= lambda:[self.proceed(), self.proceed2()] ).grid(row=1, column=2, padx=10, pady=10)
        self.B4 = Button(self.frame, text= "Exit", command = self.frame.destroy).grid(row=1, column=5, padx=10, pady=10)
        self.B2 = Button(self.frame, text = "Submit", command = lambda: [self.getval(), self.proceed2()] ).grid(row=1, column=3, padx=10, pady=10)
        self.B5 = Button(self.frame, text = "Print Table", command = self.Print_List).grid(row =1, column = 6, padx=10, pady=10)
        self.B6 = Button(self.frame, text = "Reset", command = self.Reset).grid(row=1, column=4, padx=10, pady=10)
        self.B7 = Button(self.frame, text="Export", command=self.Export).grid(row=1, column=7)

        self.QbList = []
        self.QfList = []
        self.QuList = []
        self.Length = []
        self.d = []

    def Reset(self):
        self.QbEW.delete(0, END)
        self.QfEW.delete(0, END)
        self.QuEW.delete(0, END)

    def proceed(self):

        #Label
        for i in range(self.nEV.get()):
            Label(self.frame, text = "Enter the length of layer" + str(i+1)).grid(row=4*(i+1), column=0, pady=10)
            Label(self.frame, text = "Enter the α of layer" + str(i+1)).grid(row=(4*(i+1))+1, column=0, pady=10)
            Label(self.frame, text = "Enter the cu of layer" + str(i+1)).grid(row=(4*(i+1))+2, column=0, pady=10)
            Label(self.frame, text = "Enter the cb of layer" + str(i+1)).grid(row=(4*(i+1))+3, column=0, pady=10)

    def proceed2(self):
        
        #Entry_variable
        self.L = [0]*100
        self.α = [0]*100
        self.cu = [0]*100
        self.cb = [0]*100

        for i in range(self.nEV.get()):
            self.L[i] = StringVar()
            self.α[i] = StringVar()
            self.cu[i] = StringVar()
            self.cb[i] = StringVar()
           
 
        #Entry_widget
        for i in range(self.nEV.get()):
            Entry(self.frame, textvariable=self.L[i]).grid(row=4*(i+1), column=1, pady=10)
            Entry(self.frame, textvariable=self.α[i]).grid(row=(4*(i+1))+1, column=1, pady=10)
            Entry(self.frame, textvariable=self.cu[i]).grid(row=(4*(i+1))+2, column=1, pady=10)
            Entry(self.frame, textvariable=self.cb[i]).grid(row=(4*(i+1))+3, column=1, pady=10)

    def getval(self):

        self.dia = float(self.diaEV.get())
        #print("1")
        for i in range(self.nEV.get()):
            self.L[i] = float(self.L[i].get())
            self.α[i] = float(self.α[i].get())
            self.cu[i] = float(self.cu[i].get())
            self.cb[i] = float(self.cb[i].get())

        print(self.dia)

        self.Qb = 9*self.cb[int(self.nEV.get()-1)]*(3.14*self.dia*self.dia)/4
    
        self.x=0
    
        for i in range(self.nEV.get()):
          self.Qf = 3.14*self.dia*self.L[i]*self.α[i]*self.cu[i]
          self.x = self.Qf + self.x

        self.Qu = self.Qb + self.x

        #print(self.Qb, self.x, self.Qu)

        Label(self.frame, text= "Qb").grid(row=3, column=3, pady=10, padx=5)
        Label(self.frame, text= "Qf").grid(row=3, column=4, pady=10, padx=5)
        Label(self.frame, text= "Qu").grid(row=3, column=5, pady=10, padx=5)

        self.QbEW = Entry(self.frame)
        self.QbEW.grid(row=4, column=3, pady=10, padx=5)
        self.QfEW = Entry(self.frame)
        self.QfEW.grid(row=4, column=4, pady=10, padx=5)
        self.QuEW = Entry(self.frame)
        self.QuEW.grid(row=4, column=5, pady=10, padx=5)

        self.QbEW.insert(0, self.Qb)
        self.QfEW.insert(0, self.x)
        self.QuEW.insert(0, self.Qu)

        self.QbList.append(self.Qb)
        self.QfList.append(self.x)
        self.QuList.append(self.Qu)

        self.b=0
        for i in range(self.nEV.get()):
            self.b = self.L[i] + self.b

        self.Length.append(self.b)
        self.d.append(self.dia)

    
    
    def Print_List(self):
        print(self.QbList, self.QfList, self.QuList )

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

        for i in range(len(self.QbList)):
            self.tv.insert('', i, values= (i+1, self.Length[i], self.d[i], "{:.2f}".format(self.QbList[i]), "{:.2f}".format(self.QfList[i]), "{:.2f}".format(self.QuList[i])))

    def Export(self):
        self.Name = self.NameEV.get()
        a_list = [str(self.Name), '.csv']

        FN = ''.join(a_list)
        dirname = os.path.dirname(__file__)
        filename1 = os.path.join(dirname, FN)
        dict = {'Length': self.Length, 'Diameter': self.d, 'Qb': self.QbList, 'Qf' : self.QfList, 'Qu':self.QuList}
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
        # for i in range(len(self.QbList)):
        #     self.sheet1.write(i+1, 0, i+1)
        #     self.sheet1.write(i+1, 1, self.Length[i])
        #     self.sheet1.write(i+1, 2, self.d[i])
        #     self.sheet1.write(i+1, 3, self.QbList[i])
        #     self.sheet1.write(i+1, 4, self.QfList[i])
        #     self.sheet1.write(i+1, 5, self.QuList[i])
        #     print("Export")

        # #os.chmod("C:\Users\Addi\Documents\python\New_hetro_clay2.xls")

        # #saving the excel to location described, here b4 location r is used !
        # self.wb.save(r"C:\Users\Addi\Documents\python\New_hetro_clay2.xls")

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


example = Example(root)
example.pack(side="top", fill="both", expand=True)
root.mainloop()