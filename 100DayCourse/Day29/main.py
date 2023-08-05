from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    if len(website_entry.get()) == 0:
        messagebox.showerror(title="No Entry", message="Please go back and enter a website.")
    else:
        try:
            with open("100DayCourse/Day29/data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="No Data File", message="No data file found.")
        else:
            if website_entry.get() in data:
                email = data[website_entry.get()]["email"]
                password = data[website_entry.get()]["password"]
                messagebox.showinfo(title=website_entry.get(), message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="No Data", message=f"No details for {website_entry.get()} exists.")
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def aipass():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8,10))]
    password_symbols = [choice(symbols) for i in range(randint(2,4))]
    password_numbers = [choice(numbers) for i in range(randint(2,5))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="No Entry", message="Please go back and fill out the blanks")
    else:


        is_ok = messagebox.askokcancel(title=website, message=f"These are the details: \nEmail: {email}\nPassword: {password}\n\nIs this correct?")

        if is_ok:
            try:
                with open("100DayCourse/Day29/data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("100DayCourse/Day29/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("100DayCourse/Day29/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="100DayCourse/Day29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.insert(END, "huandrew321@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="W")

generate_button = Button(text="Generate Password", command=aipass)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")


window.mainloop()