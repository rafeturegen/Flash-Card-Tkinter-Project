from tkinter import *
import random
import pandas
import pyarrow
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
window = Tk()
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}



def flip_card():
    random_english = current_card["English"]
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_english, fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def next_card():
    global random_french,flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    random_french = current_card["French"]
    canvas.itemconfig(language_text,text="French",fill="black")
    canvas.itemconfig(word_text, text=random_french, fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, flip_card)


def right_click():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index= 0)
    next_card()


flip_timer = window.after(3000, flip_card)
canvas = Canvas(bg=WHITE,width=800,height=526)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 283, text="word",font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_click)
right_button.grid(row=1, column=1)

next_card()



window.mainloop()
