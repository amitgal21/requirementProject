from tkinter import *

import globalsVar

global text1, text2, text3, text4, text5, text6, text7


def put_text_on_screen(window):
    global text1, text2, text3, text4, text5, text6, text7
    text1 = Label(
        window,
        anchor="nw",
        text="Welcome to our project to bring joy and comfort to cancer patients in isolation. ",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16 * -1),
        bg="#272A37"
    )
    text1.place(x=350, y=200)
    text2 = Label(
        window,
        anchor="nw",
        text="Our system provides a variety of features, from playing music to making video calls,",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16 * -1),
        bg="#272A37"
    )
    text2.place(x=350, y=230)
    text3 = Label(
        window,
        anchor="nw",
        text="to help patients feel more connected and engaged during treatment.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16 * -1),
        bg="#272A37"
    )
    text3.place(x=350, y=260)
    text4 = Label(
        window,
        anchor="nw",
        text=" We're here to support you and your loved ones on your cancer journey",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16* -1),
        bg="#272A37"
    )
    text4.place(x=350, y=290)
    text7 = Label(
        window,
        anchor="nw",
        text="even in complex or ambiguous cases.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16 * -1),
        bg="#272A37"
    )
    text7.place(x=350, y=320)
    text5 = Label(
        window,
        anchor="nw",
        text=" Our team is composed of experts in AI, and software "
             "development, who are passionate about",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16 * -1),
        bg="#272A37"
    )
    text5.place(x=350, y=350)
    text6 = Label(
        window,
        anchor="nw",
        text="pushing the boundaries of what is possible with AI in Coding.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 16 * -1),
        bg="#272A37"
    )
    text6.place(x=350, y=380)


def clear_screen():
    # destroy only the labels that you want to clear
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    text7.destroy()
