import os
import pygame
from tkinter import *
from tkinter import messagebox
import globalsVar

global text1, text2, text3, text4, text5, text6, text7


def show_music(window):
    toplevel = Toplevel(window)
    toplevel.title('Music Page')
    toplevel_width = 800
    toplevel_height = 400
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#272A37")

    are_u_sure = Label(toplevel, text='My Music', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 18, 'bold'))
    are_u_sure.place(x=50, y=30)

    # ================ Forgot Password ====================
    noakirel = Button(
        toplevel,
        text="Noa Kirel - UniCorn",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: play_music("Unicorn.mp3", toplevel),
    )
    noakirel.place(x=50, y=100, width=150, height=35)

    ballon = Button(
        toplevel,
        text="Eyal Golan - Balloons",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: play_music("balloons.mp3", toplevel),
    )
    ballon.place(x=50, y=150, width=150, height=35)

    wishyou = Button(
        toplevel,
        text="Lewis Capaldi - Wish You The Best",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: play_music("wishyou.mp3", toplevel),
    )
    wishyou.place(x=50, y=200, width=230, height=35)

    Braude = Button(
        toplevel,
        text="Ort Braude Official Song",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: play_music("Braude.mp3", toplevel),
    )
    Braude.place(x=50, y=250, width=180, height=35)


def play_music(file_name, toplevel):
    if file_name == "Unicorn.mp3":
        uni_corn_words(toplevel)
    file_path = os.path.join("Music", file_name)
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def uni_corn_words(toplevel):
    global text1, text2, text3, text4, text5, text6, text7
    text1 = Label(
        toplevel,
        anchor="nw",
        text="I'm gonna stand here like a unicorn",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text1.place(x=400, y=60)
    text2 = Label(
        toplevel,
        anchor="nw",
        text="Out here on my own",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text2.place(x=400, y=100)
    text3 = Label(
        toplevel,
        anchor="nw",
        text="I got the power of a unicorn",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text3.place(x=400, y=140)
    text4 = Label(
        toplevel,
        anchor="nw",
        text="Don't you ever learn?",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text4.place(x=400, y=180)
    text5 = Label(
        toplevel,
        anchor="nw",
        text="That I won't look back, I won't look down",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text5.place(x=400, y=220)
    text6 = Label(
        toplevel,
        anchor="nw",
        text="I'm going up, you better turn around",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text6.place(x=400, y=260)
    text7 = Label(
        toplevel,
        anchor="nw",
        text="The power of a unicorn, the power of a unicorn",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text7.place(x=400, y=300)




