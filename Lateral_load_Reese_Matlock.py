from ast import If
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
root.title("Lateral Laod by Reese & Matlock method")

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
        Label(self.frame, text = "Enter LOAD").grid(row=0, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Enter MOMENT").grid(row=1, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Young's Modulus").grid(row=2, column=0, padx= 10, pady=10)
        Label(self.frame, text = "MOI").grid(row=3, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Stiffness Factor").grid(row=4, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Total Length").grid(row=5, column=0, padx= 10, pady=10)
        Label(self.frame, text = "Name of File").grid(row=6, column=0, padx= 10, pady=10)

        #Entry variable initialization
        self.LoadEV = StringVar()
        self.MEV = StringVar()
        self.EEV = StringVar()
        self.MOIEV = StringVar()
        self.TEV = StringVar()
        self.LEV = StringVar()
        self.NameEV = StringVar()

        #Entry Widget
        Entry(self.frame, textvariable=self.LoadEV).grid(row=0, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.MEV).grid(row=1, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.EEV).grid(row=2, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.MOIEV).grid(row=3, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.TEV).grid(row=4, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.LEV).grid(row=5, column=1, padx= 10, pady=10)
        Entry(self.frame, textvariable=self.NameEV).grid(row=6, column=1, padx= 10, pady=10)


        Button(self.frame, text="Submit", command = self.Submit).grid(row=1, column =2, padx=10, pady=10)
        Button(self.frame, text="list", command = self.Print).grid(row=2, column =2, padx=10, pady=10)
        Button(self.frame, text="Graph", command = self.Graph).grid(row=3, column =2, padx=10, pady=10)
        Button(self.frame, text="Export", command = self.Export).grid(row=4, column =2, padx=10, pady=10)

    def Submit(self):

        self.Load = float(self.LoadEV.get())
        self.M = float(self.MEV.get())
        self.E = float(self.EEV.get())
        self.MOI = float(self.MOIEV.get())
        self.T = float(self.TEV.get())
        self.L = float(self.LEV.get())




        self.z = []
        self.zmax = float(self.L / self.T)
        #self.b  = int(self.zmax + 1)


        for i in np.arange(0, self.L , 0.1):
            if(( float(i) / self.T) <= 5):
                self.z.append( float(i) / self.T)

        #print(self.z)

        self.Ay = []
        self.By = []
        self.Y1 = []
        self.Y2 = []
        self.Y = []
        
        self.As = []
        self.Bs = []
        self.S1 = []
        self.S2 = []
        self.S = []
        
        self.Am = []
        self.Bm = []
        self.M1 = []
        self.M2 = []
        self.M3 = []
        
        self.Ap = []
        self.Bp = []
        self.P1 = []
        self.P2 = []
        self.P = []


        for i in range(len(self.z)):
            self.Ay.append((-0.0381*(self.z[i]**3)) + (0.4878*(self.z[i]**2)) - (1.9827*(self.z[i]**1)) + 2.4895)
            self.By.append((0.0049*(self.z[i]**4)) - (0.0982*(self.z[i]**3)) + (0.673*(self.z[i]**2)) - (1.8449*(self.z[i]**1)) + 1.6332)
            self.Y1.append(((self.Load*(self.T**3))*(self.Ay[i]))/(self.E*self.MOI)) 
            self.Y2.append(((self.M*(self.T**2))*(self.By[i]))/(self.E*self.MOI))
            self.Y.append(self.Y1[i] + self.Y2[i])

            
            if self.z[i] < 3:
                self.As.append((-0.0012*(self.z[i]**6)) + (0.0152*(self.z[i]**5)) - (0.0473*(self.z[i]**4)) - (0.0891*(self.z[i]**3)) + (0.5635*(self.z[i]**2)) - (0.0157*(self.z[i]**1)) - (1.6222))
            else:
                self.As.append( (-0.0018*(self.z[i]**5)) + (0.0403*(self.z[i]**4)) - (0.294*(self.z[i]**3)) + (0.7773*(self.z[i]**2)) - (0.0984*(self.z[i]**1)) - 1.6162)

            self.Bs.append( (-0.0024*(self.z[i]**5)) + (0.0359*(self.z[i]**4)) - (0.1718*(self.z[i]**3)) + (0.1383*(self.z[i]**2)) + (0.9573*(self.z[i]**1)) - 1.7473)
            self.S1.append(((self.Load*(self.T**2))*(self.As[i]))/(self.E*self.MOI)) 
            self.S2.append(((self.M*(self.T))*(self.Bs[i]))/(self.E*self.MOI))
            self.S.append(self.S1[i] + self.S2[i])



            self.Am.append( (0.002*(self.z[i]**6)) - (0.0338*(self.z[i]**5)) + (0.2054*(self.z[i]**4)) - (0.4818*(self.z[i]**3)) + (0.0394*(self.z[i]**2)) + (0.9956*(self.z[i]**1)) + 0.0003)
            if self.z[i] < 3:
                self.Bm.append( (-0.0126*(self.z[i]**4)) + (0.1466*(self.z[i]**3)) - (0.5039*(self.z[i]**2)) + (0.2348*(self.z[i]**1)) + 0.9778) 
            else:
                self.Bm.append( (-0.0034*(self.z[i]**5)) + (0.0276*(self.z[i]**4)) - (0.0146*(self.z[i]**3)) - (0.2458*(self.z[i]**2)) + (0.0885*(self.z[i]**1)) + 0.9945)
            self.M1.append(self.Load*(self.Am[i])*self.T)
            self.M2.append(self.M*self.Bm[i])
            self.M3.append(self.M1[i] + self.M2[i])



            self.Ap.append( (-0.0036*(self.z[i]**6)) + (0.0489*(self.z[i]**5)) - (0.1937*(self.z[i]**4)) - (0.0322*(self.z[i]**3)) + (1.6427*(self.z[i]**2)) - (2.4056*(self.z[i]**1)) - 0.0168)
            self.Bp.append( (-0.0082*(self.z[i]**5)) + (0.1352*(self.z[i]**4)) - (0.8102*(self.z[i]**3)) + (2.0386*(self.z[i]**2)) - (1.7225*(self.z[i]**1)) + 0.0066)
            self.P1.append(self.Load * self.Ap[i] /self.T)
            self.P2.append(self.M * self.Bp[i] / self.T**2)
            self.P.append(self.P1[i] + self.P2[i])
      
      
      
      
      
       # print(self.Y1)
        #print(self.Y2)
        #print(len(self.z))
        #print(len(self.Y))

        #for i in range(len(self.z)):
             
        self.b = []
        for i in np.arange(len(self.z)):
            self.b.append(self.z[i]*self.T)

        #print(self.b)
        #print(len(self.b))  
    def Graph(self): 

        fig, axes = plt.subplots(nrows=1, ncols=4)
        
        self.x1 = self.Y
        self.y1 = self.b
        plt.subplot(1,4,1)
        plt.xlabel("Deflection")
        plt.ylabel("Length")
        plt.title("Deflection vs Length")
        plt.plot(self.x1,self.y1)
        plt.ylim(max(self.y1), min(self.y1))
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

        
        self.x2 = self.S
        self.y2 = self.b
        plt.subplot(1,4,2)
        plt.xlabel("Slope")
        plt.ylabel("Length")
        plt.title("Slope vs Length")
        plt.plot(self.x2,self.y2)
        plt.ylim(max(self.y2), min(self.y2))
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)


        self.x3 = self.M3
        self.y3 = self.b
        plt.subplot(1,4,3)
        plt.xlabel("Moment")
        plt.ylabel("Length")
        plt.title("Moment vs Length")
        plt.plot(self.x3,self.y3)
        plt.ylim(max(self.y3), min(self.y3))
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)


        self.x4 = self.P
        self.y4 = self.b
        plt.subplot(1,4,4)
        plt.xlabel("Soil Reaction")
        plt.ylabel("Length")
        plt.title("Soil Reaction vs Length")
        plt.plot(self.x4,self.y4)
        plt.ylim(max(self.y4), min(self.y4))
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        fig.tight_layout()
        plt.show()


    def Print(self):

        #print(self.Y)
         #to form window on click
        self.newwin = Toplevel(root) 
        self.newwin.geometry("1366x768")
        


        self.tv = ttk.Treeview(self.newwin, height = 70)
        #self.tv['columns']=('SR.NO', 'Length', 'Diameter', 'Qb', 'Qf', 'Qu')
        self.tv['columns']=('SR.NO', 'Length', 'Deflection', 'Slope', 'Moment', 'Soil Reaction')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('SR.NO', anchor=CENTER, width=70)
        self.tv.column('Length', anchor=CENTER, width=100)
        self.tv.column('Deflection', anchor=CENTER, width=100)
        self.tv.column('Slope', anchor=CENTER, width=100)
        self.tv.column('Moment', anchor=CENTER, width=100)
        self.tv.column('Soil Reaction', anchor=CENTER, width=100)
        
        #self.tv.column('Qu', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('SR.NO', text='SR.NO', anchor=CENTER)
        self.tv.heading('Length', text='Length', anchor=CENTER)
        self.tv.heading('Deflection', text='Deflection', anchor=CENTER)
        self.tv.heading('Slope', text='Slope', anchor=CENTER)
        self.tv.heading('Moment', text='Moment', anchor=CENTER)
        self.tv.heading('Soil Reaction', text='Soil Reaction', anchor=CENTER)
        
        # self.tv.heading('Qu', text='Qu', anchor=CENTER)

        self.scrollbar = Scrollbar(self.newwin, orient=VERTICAL, command = self.tv.yview).grid(row =0, column=1, sticky=NS)
        self.tv.grid(row =0, column = 5, sticky= NSEW)

        for i in range(len(self.z)):
            #self.tv.insert('', i, values= (i+1, self.Length[i], self.d[i], "{:.2f}".format(self.QbList[i]), "{:.2f}".format(self.QfList[i]), "{:.2f}".format(self.QuList[i])))
            self.tv.insert('', i, values= (i+1, "{:.2f}".format(self.b[i]), "{:.4f}".format(self.Y[i]), "{:.4f}".format(self.S[i]), "{:.4f}".format(self.M3[i]), "{:.4f}".format(self.P[i])))
    
    def Export(self):

        self.Name = self.NameEV.get()
        a_list = [str(self.Name), '.csv']

        FN = ''.join(a_list)

        dirname = os.path.dirname(__file__)
        filename1 = os.path.join(dirname, FN)
        dict = {'Length': self.b, 'Deflection': self.Y, 'Slope': self.S, 'Moment' : self.M3, 'Soil Reaction':self.P}
        df = pd.DataFrame(dict) 
        df.to_csv(f"{filename1}", header=True, index=False)
    
    
    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


example = Example(root)
example.pack(side="top", fill="both", expand=True)
root.mainloop()