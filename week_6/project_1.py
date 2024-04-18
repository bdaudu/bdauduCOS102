import tkinter as tk
from tkinter import messagebox
from tkinter import *

def price(w,location):

    naira = tk.Tk()
    naira.title("Simi Services Price Window")
    naira.geometry("500x200")
    naira.config(bg = "purple")

    
    if w >= 10 and location == "Ibeju-Lekki":
        nlabel = tk.Label(naira, text = f"Your price for this {w}kg product to {location} is 5,000 Naira")
        nlabel.pack()
    elif w < 10 and location == "Ibeju-Lekki":
        nlabel_2 = tk.Label(naira, text = f"Your price for this {w}kg product to {location} is 3,500 Naira")
        nlabel_2.pack()
    elif w >= 10 and location == "Epe":
        nlabel_3 = tk.Label(naira, text = f"Your price for this {w}kg product to {location} is 10,000 Naira")
        nlabel_3.pack()
    elif w < 10 and location == "Epe":
        nlabel_4 = tk.Label(naira, text = f"Your price for this {w}kg product to {location} is 5,000 Naira")
        nlabel_4.pack()
    else:
        messagebox.showerror("Oops!","Try Again Next Time")


    naira.mainloop()


def weight_and_location():
    weight = weight_entry.get()
    location = location_entry.get()

    w = int(weight)

    if w >= 10 and location == "Ibeju-Lekki":
        price(w,location)
    elif w < 10 and location == "Ibeju-Lekki":
        price(w,location)
    elif w >= 10 and location == "Epe":
        price(w,location)
    elif w < 10 and location == "Epe":
        price(w,location)
    else:
        messagebox.showerror("Error!", "Sorry. An error has ocurred")
    
window = tk.Tk()
window.title("Simi Sercives Weight and Location Check")
window.geometry("500x400")
window.config(bg = "black")

weight_label = tk.Label(window, text = "Weight Input")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

weight_label.config(fg = "red", bg = "black")

location_label = tk.Label(window, text = "Location Input")
location_label.pack()
location_entry = tk.Entry(window)
location_entry.pack()

location_label.config(fg = "red", bg = "black")

submit_button = tk.Button(window, text = "Go!", command = weight_and_location)
submit_button.pack()

submit_button.config(fg = "black", bg = "green")
window.mainloop()


def price(w,location):

    naira = tk.Tk(window)
    naira.title("Simi Services Price Window")
    naira.geometry("200x300")


