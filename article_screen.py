import os
import pygame
from tkinter import *
from tkinter import messagebox
import globalsVar

global like_button, like_button2, disslike_button, dlike_button2
global text1, text2

def show_article(window):
    global like_button, like_button2, disslike_button, dlike_button2
    toplevel = Toplevel(window)
    toplevel.title('Article Page')
    toplevel_width = 800
    toplevel_height = 500
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#272A37")

    are_u_sure = Label(toplevel, text='Article List', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 18, 'bold'))
    are_u_sure.place(x=50, y=30)

    image1 = PhotoImage(file="assets/article1/article1.png")
    # Use the reference to the image to create the button.
    image1_button = Button(
        toplevel,
        image=image1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: show_article1(toplevel, "assets/article1/article11.png")
    )
    image1_button.image = image1  # Keep a reference to the image.
    image1_button.place(x=80, y=100, width=400, height=136)

    like_image = PhotoImage(file="assets/like4.png")
    like_button = Button(
        toplevel,
        image=like_image,
        borderwidth=0,
        highlightthickness=0,  # Set to the exact color value of the window's background color
        relief="flat",
        activebackground="#272A37",
        cursor="hand2", command=lambda: vote(1, 2, toplevel)
    )
    like_button.image = like_image  # Keep a reference to the image.
    like_button.place(x=500, y=160, width=97, height=42)

    disslike_image = PhotoImage(file="assets/dislike4.png")
    disslike_button = Button(
        toplevel,
        image=disslike_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2", command=lambda: vote(1, 1, toplevel)
    )
    disslike_button.image = disslike_image  # Keep a reference to the image.
    disslike_button.place(x=650, y=160, width=97, height=42)

    image2 = PhotoImage(file="assets/article2/article2.png")
    image2_button = Button(
        toplevel,
        image=image2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: show_article2(toplevel, "assets/article2/article21.png")
    )
    image2_button.image = image2  # Keep a reference to the image.
    image2_button.place(x=80, y=280, width=400, height=155)

    like_image2 = PhotoImage(file="assets/like4.png")
    like_button2 = Button(
        toplevel,
        image=like_image2,
        borderwidth=0,
        highlightthickness=0,  # Set to the exact color value of the window's background color
        relief="flat",
        activebackground="#272A37",
        cursor="hand2", command=lambda: vote(2, 2, toplevel)
    )
    like_button2.image = like_image2  # Keep a reference to the image.
    like_button2.place(x=500, y=320, width=97, height=42)

    disslike2_image = PhotoImage(file="assets/dislike4.png")
    dlike_button2 = Button(
        toplevel,
        image=disslike2_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2", command=lambda: vote(2, 1, toplevel)
    )
    dlike_button2.image = disslike2_image  # Keep a reference to the image.
    dlike_button2.place(x=650, y=320, width=97, height=42)


def show_article1(window, path_article):
    toplevel = Toplevel(window)
    toplevel.title('Article')
    toplevel_width = 750
    toplevel_height = 735
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#525561")

    article = PhotoImage(file=path_article)
    label = Label(toplevel, width=650, height=735)
    label.image = article
    label.configure(image=article)
    label.pack()
    next_button = PhotoImage(file="assets/next.png")


def show_article2(window, path_article):
    toplevel = Toplevel(window)
    toplevel.title('Article')
    toplevel_width = 750
    toplevel_height = 735
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#525561")

    article = PhotoImage(file=path_article)
    label = Label(toplevel, width=650, height=735)
    label.image = article
    label.configure(image=article)
    label.pack()


def vote(i, j, window):
    global text1, text2
    if i == 1:
        disslike_button.destroy()
        like_button.destroy()
        if j == 1:
            str_txt = "Next Time We Will Do It Better"
            color = "red"
            globalsVar.itsClick1 = 1
        else:
            str_txt = "Thank You Very Much"
            color = "green"
            globalsVar.itsClick2 = 1
    else:
        like_button2.destroy()
        dlike_button2.destroy()
        if j == 1:
            str_txt = "Next Time We Will Do It Better"
            color = "red"
            globalsVar.itsClick3 = 1
        else:
            str_txt = "Thank You Very Much"
            color = "green"
            globalsVar.itsClick4 = 1

    if i == 1:
        text1 = Label(
            window,
            anchor="nw",
            text=str_txt,
            fg=color,
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text1.place(x=500, y=160)
    else:
        text2 = Label(
            window,
            anchor="nw",
            text=str_txt,
            fg=color,
            font=("yu gothic ui Bold", 17 * -1),
            bg="#272A37"
        )
        text2.place(x=500, y=320)
