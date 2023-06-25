from tkinter import *
from tkinter import messagebox
import pyglet
import os
import globalsVar
from tkvideo import tkvideo
import cv2


def show_video(window):
    toplevel = Toplevel(window)
    toplevel.title('Videos Page')
    toplevel_width = 800
    toplevel_height = 400
    toplevel_position_x = int(window.winfo_width() / 2 - toplevel_width / 2) + window.winfo_x()
    toplevel_position_y = int(window.winfo_height() / 2 - toplevel_height / 2) + window.winfo_y()
    toplevel.geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_position_x}+{toplevel_position_y}')
    toplevel.configure(bg="#272A37")

    are_u_sure = Label(toplevel, text='My Videos', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 18, 'bold'))
    are_u_sure.place(x=50, y=30)

    loNoshem = Button(
        toplevel,
        text="    Lo Noshem Hamefaked",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: play_video("C:\\Users\\amitg\\PycharmProjects\\py\\videos\\Lonos.mp4"),
    )
    loNoshem.place(x=50, y=100, width=150, height=35)


def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
