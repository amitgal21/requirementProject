from tkinter import *
import globalsVar

global game_button, video_button, music_button, read_button


def clear_screen():
    try:
        game_button.destroy()
    except NameError:
        pass
    try:
        video_button.destroy()
    except NameError:
        pass
    try:
        music_button.destroy()
    except NameError:
        pass
    try:
        read_button.destroy()
    except NameError:
        pass


def init_home_page(window):
    global game_button, video_button, music_button, read_button
    mygames_fol = PhotoImage(file="assets/mygamess.png")

    # create the button and assign the image to it
    game_button = Button(
        window,
        image=mygames_fol,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561", foreground="#525561",
        cursor="hand2", command=lambda: mov_to_games(window))

    # keep a reference to the PhotoImage object
    game_button.image = mygames_fol
    game_button.place(x=400, y=200, width=190, height=70)

    myvideo = PhotoImage(file="assets/myvideo.png")

    # create the button and assign the image to it
    video_button = Button(
        window,
        image=myvideo,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561", foreground="#525561",
        cursor="hand2", command=lambda: mov_to_video(window))

    # keep a reference to the PhotoImage object
    video_button.image = myvideo
    video_button.place(x=700, y=200, width=190, height=70)

    mymusic = PhotoImage(file="assets/mymusic.png")

    # create the button and assign the image to it
    music_button = Button(
        window,
        image=mymusic,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561", foreground="#525561",
        cursor="hand2", command=lambda: mov_to_music(window))

    # keep a reference to the PhotoImage object
    music_button.image = mymusic
    music_button.place(x=400, y=350, width=190, height=70)

    read_img = PhotoImage(file="assets/read.png")

    # create the button and assign the image to it
    read_button = Button(
        window,
        image=read_img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#525561", foreground="#525561",
        cursor="hand2", command=lambda: read_article(window))

    # keep a reference to the PhotoImage object
    read_button.image = read_img
    read_button.place(x=700, y=350, width=190, height=70)


def mov_to_games(window):
    from MyGames import show_games
    show_games(window)


def mov_to_video(window):
    from video_screen import show_video
    show_video(window)


def mov_to_music(window):
    from Music_Screen import show_music
    show_music(window)

def read_article(window):
    from article_screen import show_article
    show_article(window)