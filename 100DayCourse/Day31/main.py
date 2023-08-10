from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- SAVE PROGRESS ------------------------------- #
try:
    data = pandas.read_csv("100DayCourse/Day31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("100DayCourse/Day31/data/korean_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("100DayCourse/Day31/data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- WORD GENERATOR ------------------------------- #

data = pandas.read_csv("100DayCourse/Day31/data/korean_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# ---------------------------- FLASH CARDS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Korean", fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Korean Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="100DayCourse/Day31/images/card_front.png")
card_back_img = PhotoImage(file="100DayCourse/Day31/images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="100DayCourse/Day31/images/wrong.png")
x_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

right_img = PhotoImage(file="100DayCourse/Day31/images/right.png")
y_button = Button(image=right_img, highlightthickness=0, command=is_known)
y_button.grid(row=1, column=1)

next_card()

window.mainloop()