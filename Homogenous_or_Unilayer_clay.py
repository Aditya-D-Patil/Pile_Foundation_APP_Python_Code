from tkinter import *
from tkinter import filedialog
from typing import List
from tkinter import ttk
import pandas as pd
from openpyxl.workbook import Workbook
from xlwt import *
import xlwt
import numpy as np
import os
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror
from datetime import datetime

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1',  cell_overwrite_ok=True)


#global Qb
#global Qf
#global Qu

#global QbList
QbList = []

#global QfList
QfList = []

#global QuList
QuList = []

#global length
length = []

#global dia
dia = []

root = Tk()
root.geometry("1366x768")
root.title("Homogenous or unilayer clayey soil")

click_counter = 0

#to get the value from entry widget and process data to get output
def getval():
    status=0
    cb = float(cbEV.get())
    cu = float(cuEV.get())
    α = float(αEV.get())
    Nc = float(NcEV.get())
    d = float(diaEV.get())
    L = float(lengthEV.get())

    #global Qb
    Qb = cb*Nc*((3.14*d*d)/4)
    #global Qf
    Qf = cu*α*(3.14*d*L)
    #global Qu
    Qu = Qb + Qf

    #global length
    length.append(L)

    #global dia
    dia.append(d)

    #global QbList
    QbList.append(Qb)

    #global QfList
    QfList.append(Qf)

    #global QuList
    QuList.append(Qu)

    QbEW.insert(0, Qb)
    QfEW.insert(0, Qf)
    QuEW.insert(0, Qu)

    #returning list of following so that we can use them in other functions
    return (length, dia, QbList, QfList, QuList)




#to clear entry widget of outputs
def Reset():
    QbEW.delete(0, END)
    QfEW.delete(0, END)
    QuEW.delete(0, END)

#to open a new window to display data in tabular form
def Print_list():
    a,b,c,d,e = getval()
    print(*c, sep = ", ")
    print(*d, sep = ", ")
    print(*e, sep = ", ")
    print(len(c))

    #to form window on click
    newwin = Toplevel(root) 
    newwin.geometry("1366x768")

    #to display data in tabular form
    tv = ttk.Treeview(newwin, height = 30)
    tv['columns']=('SR.NO', 'Length', 'Diameter', 'Qb', 'Qf', 'Qu')
    tv.column('#0', width=0, stretch=NO)
    tv.column('SR.NO', anchor=CENTER, width=70)
    tv.column('Length', anchor=CENTER, width=200)
    tv.column('Diameter', anchor=CENTER, width=200)
    tv.column('Qb', anchor=CENTER, width=200)
    tv.column('Qf', anchor=CENTER, width=200)
    tv.column('Qu', anchor=CENTER, width=200)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('SR.NO', text='SR.NO', anchor=CENTER)
    tv.heading('Length', text='Length', anchor=CENTER)
    tv.heading('Diameter', text='Diameter', anchor=CENTER)
    tv.heading('Qb', text='Qb', anchor=CENTER)
    tv.heading('Qf', text='Qf', anchor=CENTER)
    tv.heading('Qu', text='Qu', anchor=CENTER)

    #adding scrollbar
    scroll = Scrollbar(newwin, orient=VERTICAL, command = tv.yview).grid(row =0, column=1, sticky=NS)
    tv.grid(row =0, column = 5)

    #Adding data to the treeview table formed
    for i in range(len(c)-1):
        tv.insert('', i, values= (i+1, a[i], b[i], "{:.2f}".format(c[i]), "{:.2f}".format(d[i]), "{:.2f}".format(e[i])))

    B5 = Button(newwin, text = "Export to Excel", command = Export).grid(row=0, column=7, ipadx = 10)

#to export the treeview table data(data in lists) to excel
def Export():
        
        a,b,c,d,e = getval() #calling getval func and storing list in variable to use them here
        # now = datetime.now()
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #print("1")
        name = NameEW.get()
        a_list = [str(name), '.csv']

        FN = ''.join(a_list)
        dirname = os.path.dirname(__file__)
        #print("2")
        filename1 = os.path.join(dirname, FN)
        #print("3")
        dict = {'Length': a, 'Diameter': b, 'Qb': QbList, 'Qf' : QfList, 'Qu':QuList}
        #print("4")
        df = pd.DataFrame(dict) 
        #print("5")
        count_row = df.shape[0]
        df = df.head(count_row - 2)
        #print("6")
        df.to_csv(f"{filename1}", header=True, index=False)
        #print("7")
        #print("Exported Sucessfully")
        
        # #making headings bold
        # style = xlwt.easyxf('font: bold 1')
        # sheet1.write(0, 0, 'SR.NO' , style)
        # sheet1.write(0, 1, 'Length', style)
        # sheet1.write(0, 2, 'Diameter', style)
        # sheet1.write(0, 3, 'Qb', style)
        # sheet1.write(0, 4, 'Qf', style)
        # sheet1.write(0, 5, 'Qu', style)

        # #writting data to excel
        # for i in range(len(c)-2):
        #     sheet1.write(i+1, 0, i+1)
        #     sheet1.write(i+1, 1, a[i])
        #     sheet1.write(i+1, 2,b[i])
        #     sheet1.write(i+1, 3, QbList[i])
        #     sheet1.write(i+1, 4, QfList[i])
        #     sheet1.write(i+1, 5, QuList[i])
        
        # #saving the excel to location described, here b4 location r is used !
        # wb.save(r"C:\Users\Addi\Documents\python\New_homo_clay.xls")
        


#label
#UnitLabel = Label(root, text = "Select the Unit System")
cbLabel = Label(root, text ='Enter cb')
cuLabel = Label(root, text ='Enter cu')
αLabel = Label(root, text ='Enter α')
NcLabel = Label(root, text ='Enter Nc')
diaLabel = Label(root, text ='diameter')
lengthLabel = Label(root, text ='length')
QbLabel = Label(root, text ='Qb in KN/m')
QfLabel = Label(root, text ='Qf in KN/m')
QuLabel = Label(root, text ='Qu in KN/m')
NameLabel = Label(root, text = "Enter File name")


#packing label
#UnitLabel.grid(row=0, column=0, pady=10)
cbLabel.grid(row=1, column=0, pady=10)
cuLabel.grid(row=2, column=0, pady=10)
αLabel.grid(row=3, column=0, pady=10)
NcLabel.grid(row=4, column=0, pady=10)
diaLabel.grid(row=5, pady=10)
lengthLabel.grid(row=6, pady=10)
QbLabel.grid(row=8, pady=10)
QfLabel.grid(row=9, pady=10)
QuLabel.grid(row=10, pady=10)
NameLabel.grid(row=11, column = 0, pady =10)


#entry variable
cbEV = StringVar()
cuEV = StringVar()
αEV = StringVar()
NcEV = StringVar()
diaEV = StringVar()
lengthEV = StringVar()
NameEV = StringVar()

#entry widget
cbEW = Entry(root, textvariable = cbEV).grid(row=1, column=1, pady=10)
cuEW = Entry(root, textvariable = cuEV).grid(row=2, column=1, pady=10)
αEW = Entry(root, textvariable = αEV).grid(row=3, column=1, pady=10)
NcEW = Entry(root, textvariable = NcEV).grid(row=4, column=1, pady=10)
diaEW = Entry(root,  textvariable = diaEV).grid(row=5, column=1, pady=10)
lengthEW = Entry(root,  textvariable = lengthEV).grid(row=6, column=1, pady=10)
NameEW = Entry(root,  textvariable = NameEV)

QbEW = Entry(root)
QfEW = Entry(root)
QuEW = Entry(root)

NameEW.grid(row=11, column=1, pady=10)
QbEW.grid(row=8, column=1, pady=10)
QfEW.grid(row=9, column=1, pady=10)
QuEW.grid(row=10, column=1, pady=10)

# #checkbutton status
# C1status = IntVar()
# C2status = IntVar()
# C3status = IntVar()

# #checkbutton
# C1 = Checkbutton(root, text="KN/mm", variable = C1status).grid(row=0, column=1)
# C2 = Checkbutton(root, text="KN/m", variable = C2status).grid(row=0, column=2)
# C3 = Checkbutton(root, text="lf/ft", variable = C3status).grid(row=0, column=3)

B1 = Button(text="submit", command=getval).grid(row=7, column=0)
B2 = Button(text="Exit", command = root.destroy).grid(row=7, column =1)
B3 = Button(text = "Reset", command = Reset).grid(row =7, column =2)
B4 = Button(root, text = "Print list", command = Print_list).grid(row=7, column =3)

root.mainloop()
