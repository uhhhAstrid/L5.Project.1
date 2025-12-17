from tkinter import *
import game_classes 


window = Tk()
window.title("Sorry")
window.geometry("500x500")
text_label_1 = Label(window, text = "Player One")
text_label_2 = Label(window, text = "Player Two")
text_label_1.place(x=20, y=0)
text_label_2.place(x=400, y=0)
text_label_cards = Label(window, text = ("draw"))


def clicked():
    Drawing_cards = Button( text = "Click me to draw a new card" ,fg = "red", command=clicked)

command=game.shuffle()


window.mainloop()
