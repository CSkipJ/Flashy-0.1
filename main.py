from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
timer = None

df = pandas.read_csv('./data/french_words.csv')
to_learn = df.to_dict(orient='records')


def get_new_card():
    new_card = choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_vocab, text=new_card['French'], fill='black')
    card_timer(3, new_card)


def flip_card(card):
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_vocab, text=card['English'], fill='black')


def card_timer(count, card):
    global timer
    if count < 1:  # check flag value before scheduling next call
        root.after_cancel(timer)
        flip_card(card)
    else:
        print(count)
        timer = root.after(1000, card_timer, count - 1, card)


root = Tk()
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.title('Flash Card')

# card front declaration
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Card front text objects
card_title = canvas.create_text(400, 150, text='test', font=('Ariel', 40, 'italic'))
card_vocab = canvas.create_text(400, 263, text='test', font=('Ariel', 60, 'bold'))

# X button declaration
wrong_icon = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_icon, highlightthickness=0, command=get_new_card)
wrong_button.grid(row=1, column=0)

# Check mark button declaration
right_icon = PhotoImage(file='./images/right.png')
right_button = Button(image=right_icon, highlightthickness=0, command=get_new_card)
right_button.grid(row=1, column=1)

get_new_card()

root.mainloop()
