import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "C:\\Users\\ADMIN\\Desktop\\Attendance System - FYP\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\ADMIN\\Desktop\\Attendance System - FYP\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\ADMIN\\Desktop\\Attendance System - FYP\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\ADMIN\\Desktop\\Attendance System - FYP\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\ADMIN\\Desktop\\Attendance System - FYP\\Attendance"


window = Tk()
window.title("Face recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="white")


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="white")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Roll No & Name required!!!",
        fg="black",
        bg="white",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="white",
        bg="purple",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/Mehran_logo.svg")
logo = logo.resize((50, 47), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="white", relief=RIDGE, bd=10, font=("times new roman", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="white",)
l1.place(x=400, y=10)

titl = tk.Label(
    window, text="MUET Attendance System", bg="white", fg="black", font=("times new roman", 27),
)
titl.place(x=500, y=12)


ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=150)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=900, y=150)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=500, y=150)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="white")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="purple", relief=FLAT, bd=10, font=("times new roman", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Student's Face", bg="purple", fg="white", font=("times new roman", 30),
    )
    titl.place(x=250, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="white",
        fg="black",
        bd=10,
        font=("times new roman", 24),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Roll No",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        font=("times new roman", 15, "bold"),
    )
    lbl1.place(x=120, y=125)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 15, "bold"),
    )
    txt1.place(x=250, y=135)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        font=("times new roman", 15, "bold"),
    )
    lbl2.place(x=120, y=195)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 15, "bold"),
    )
    txt2.place(x=250, y=205)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        font=("times new roman", 15, "bold"),
    )
    lbl3.place(x=120, y=265)
    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=277)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="purple",
        fg="white",
        height=1,
        width=12,
        relief=FLAT,
    )
    takeImg.place(x=130, y=355)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="purple",
        fg="white",
        height=1,
        width=12,
        relief=FLAT,
    )
    trainImg.place(x=360, y=355)


r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="purple",
    fg="white",
    height=2,
    width=17,
    relief=FLAT,
)
r.place(x=100, y=400)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="purple",
    fg="white",
    height=2,
    width=17,
    relief=FLAT,
)
r.place(x=500, y=400)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="purple",
    fg="white",
    height=2,
    width=17,
    relief=FLAT,
)
r.place(x=900, y=400)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="purple",
    fg="white",
    height=2,
    width=17,
    relief=FLAT,
)
r.place(x=500, y=550)

window.mainloop()
