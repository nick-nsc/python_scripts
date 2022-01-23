from tkinter import *
from math import *

def calculate(event):
    expression = input_field.get()
    input_field.delete(0,END)
    try:
            input_field.insert(0, eval(expression))  # insert result to the entry field
    except:
            input_field.insert(0, "Invalid syntax")  # an error occured while evaluating the expression
    
top = Tk()

# create an input field that will cover three columns in the first row
input_field = Entry(top)
input_field.grid(row=0,columnspan=3)

# create buttons and bind them to a position
b1=Button(top,text="1")
b1.grid(row=1,column=0)
b2=Button(top,text="2")
b2.grid(row=1,column=1)
b3=Button(top,text="3")
b3.grid(row=1,column=2)
b4=Button(top,text="4")
b4.grid(row=2,column=0)
b5=Button(top,text="5")
b5.grid(row=2,column=1)
b6=Button(top,text="6")
b6.grid(row=2,column=2)
b7=Button(top,text="7")
b7.grid(row=3,column=0)
b8=Button(top,text="8")
b8.grid(row=3,column=1)
b9=Button(top,text="9")
b9.grid(row=3,column=2)
b0=Button(top,text="0")
b0.grid(row=4,column=1)
bplus=Button(top,text="+")
bplus.grid(row=0,column=3)
bminus=Button(top,text="-")
bminus.grid(row=1,column=3)
bmult=Button(top,text="*")
bmult.grid(row=2,column=3)
bdiv=Button(top,text="/")
bdiv.grid(row=3,column=3)
bequal=Button(top,text="=")
bequal.grid(row=4,column=3)
bdel=Button(top,text="DEL")
bdel.grid(row=4,column=2)

# bind and name the buttons
b1.bind("<Button-1>", lambda x: input_field.insert(END,"1"))
b2.bind("<Button-1>", lambda x: input_field.insert(END,"2"))
b3.bind("<Button-1>", lambda x: input_field.insert(END,"3"))
b4.bind("<Button-1>", lambda x: input_field.insert(END,"4"))
b5.bind("<Button-1>", lambda x: input_field.insert(END,"5"))
b6.bind("<Button-1>", lambda x: input_field.insert(END,"6"))
b7.bind("<Button-1>", lambda x: input_field.insert(END,"7"))
b8.bind("<Button-1>", lambda x: input_field.insert(END,"8"))
b9.bind("<Button-1>", lambda x: input_field.insert(END,"9"))
b0.bind("<Button-1>", lambda x: input_field.insert(END,"0"))
bplus.bind("<Button-1>", lambda x: input_field.insert(END,"+"))
bminus.bind("<Button-1>", lambda x: input_field.insert(END,"-"))
bmult.bind("<Button-1>", lambda x: input_field.insert(END,"*"))
bdiv.bind("<Button-1>", lambda x: input_field.insert(END,"/"))
bequal.bind("<Button-1>", calculate)
bdel.bind("<Button-1>", lambda x: input_field.delete(0,END))

top.mainloop()
