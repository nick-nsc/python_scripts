import tkinter

def handleButton(event):
    global field_input
    global field_result
    field_result['text'] = eval(field_input.get())

# create a window
top = tkinter.Tk()

# create an input field t
field_input = tkinter.Entry(top)
field_input.pack()

# create a label to display the result to
field_result = tkinter.Label(top,text="")
field_result.pack()

# create the calculate-button
b = tkinter.Button(top,text="Calculate!")
b.pack()

# add button funcitonality
b.bind('<Button-1>', handleButton)

top.mainloop()
