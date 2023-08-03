from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20,pady=20)

def calculate():
    result = float(user_input.get()) * 1.60934
    conversion.config(text= result)

user_input = Entry(width=7)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

conversion = Label(text="0")
conversion.grid(column=1, row=1)


window.mainloop()