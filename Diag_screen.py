from tkinter import *
from tkinter import messagebox

global text1, text2, text3, text4, text5, text6, image1_button


# ==================== initialize the diagnose screen in user screen ==================
def start_Screen(window):
    global text1, text2, text3, text4, text5, text6, image1_button
    text1 = Label(
        window,
        anchor="nw",
        text="Hello! We're checking in to see how you're doing today. How are you feeling?",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37"
    )
    text1.place(x=350, y=200)


# ==================== are you sure screen for button in diagnose screen in user ==================
def func1(window):
    from areUsure import areUsurefunc
    areUsurefunc(window)


# ==================== function for clear the diagnose screen in user screen ==================
def clDscr():
    text1.destroy()
