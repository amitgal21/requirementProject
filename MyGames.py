from tkinter import *
from tkinter import messagebox
import globalsVar


def show_games(window):
    toplevel = Toplevel(window)
    toplevel.title('Games Page')
    toplevel_width = 800
    toplevel_height = 400
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#272A37")

    are_u_sure = Label(toplevel, text='My Games', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 18, 'bold'))
    are_u_sure.place(x=50,y=30)

    # create the PhotoImage object
    Login_button_image_1 = PhotoImage(file="assets/snake.png")

    # create the button and assign the image to it
    Login_button_1 = Button(
        toplevel,
        image=Login_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561",
        cursor="hand2", command=lambda: f1())

    # keep a reference to the PhotoImage object
    Login_button_1.image = Login_button_image_1

    # place the button on the window
    Login_button_1.place(x=30, y=100, width=80, height=80)

    # create the PhotoImage object
    Login_button_image_2 = PhotoImage(file="assets/tic.png")

    # create the button and assign the image to it
    Login_button_2 = Button(
        toplevel,
        image=Login_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2", command=lambda: f2(toplevel))

    # keep a reference to the PhotoImage object
    Login_button_2.image = Login_button_image_2

    # place the button on the window
    Login_button_2.place(x=150, y=100, width=80, height=80)


def f1():
    import game1


def f2(toplevel):
    toplevel.destroy()
    import game2

