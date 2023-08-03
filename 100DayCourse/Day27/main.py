from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label",font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)

# Change/Update
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="Click Me 2!", command=button_clicked)
new_button.grid(column=2, row=0)
# Entry component
input = Entry()
input.grid(column=3, row=2)














window.mainloop()