#import Libraries

from tkinter import *                                       #import (*)all
from translate import Translator
#--------------------------------------------------------------------------------------
#Translator Function

def translate():
    translator=Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation=translator.translate(var.get())
    var1.set(translation)
#--------------------------------------------------------------------------------------
#Tkinter rootWindow with Title 
    
root=Tk()
root.title("Translator")
#--------------------------------------------------------------------------------------
#Creating A Frame and Grid to hold the content

mainframe=Frame(root)
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)
mainframe.pack(pady=100,padx=100)
#---------------------------------------------------------------------------------------
#Variables For DropDown list

lan1=StringVar(root)
lan2=StringVar(root)
#----------------------------------------------------------------------------------------
#Choices To show

choices={"English","Hindi","Spanish","German"}
lan1.set("English")
lan2.set("Hindi")
#-----------------------------------------------------------------------------------------
#Creating DropDown and Arranging in the grid

lan1menu=OptionMenu(mainframe,lan1,*choices)
Label(mainframe,text="Select a Language").grid(row=0,column=1)
lan1menu.grid(row=1,column=1)

lan2menu=OptionMenu(mainframe,lan2,*choices)
Label(mainframe,text="Select a Language").grid(row=0,column=2)
lan2menu.grid(row=1,column=2)
#-----------------------------------------------------------------------------------------
#Text Box To enter User Input

Label(mainframe,text="Enter Text").grid(row=2,column=0)
var=StringVar()
textbox=Entry(mainframe,textvariable=var).grid(row=2,column=1)
#------------------------------------------------------------------------------------------
#Text Box To Show Output

Label(mainframe,text="Output").grid(row=2,column=2)
var1=StringVar()
textbox=Entry(mainframe,textvariable=var1).grid(row=2,column=3)
#------------------------------------------------------------------------------------------
#Creating Button to call Translator Function

b=Button(mainframe,text="Translate",command=translate).grid(row=3,column=1,columnspan=3)
#------------------------------------------------------------------------------------------


root.mainloop()
