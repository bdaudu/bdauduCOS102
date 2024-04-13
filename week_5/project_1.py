import tkinter as tk
from tkinter import messagebox
from tkinter import *

def welcomeMessage(username):

    window = tk.Toplevel(root)
    window.title("GIG Logistics")
    window.geometry("500x200")

    label_1 = tk.Label(window, text = f"Welcome {username}, Existing Employee\n")
    label_1.pack()
    label_2 = tk.Label(window, text = f"You have successfully logged into GIG Logistics!!!")
    label_2.pack()

    root.mainloop()


def submit():
    username = username_entry.get()
    dep = department_entry.get()

    gig = {"ADENIRAN Oluwatamilore" : "Logistics","ADEWUMI Ayomide" : "Accounting", "ADOH-AJAGBE Oshim" : "Delivery", "AGBAKURU-NWOGU Chukwunonye" : "Accounting", "AGBAKWURU Chiemeziem" : "Logistics", 
       "AKINDE Oluwatimilehin" : "Accounting", "ARNIKA Osose" : "Logistics", "ATELLY Daniel" : "Delivery", "AZOGU Onyekachi" : "Delivery", "BETURE Shalom" : "Delivery", 
       "CHUKWUMA Nedi" : "Logistics", "EBI Stephanie" : "Accounting", "EGBORO Jason" : "Administration", "EJEDIMU Edward" : "Delivery", "ELERI Otu" : "Administration", 
       "EZE Onyinyechi" : "Administration", "EZEONYE Makuochukwu" : "Logistics", "GIWA Moyosore" : "Logistics", "ICHA Ayonete" : "Accounting", "IKPATI Eche" : "Accounting", 
       "ILOENYOSI Michael" : "Delivery", "IYAWE Oluwadamilola" : "Delivery", "NWOKOLO Chijindu": "Logistics", "NWOTOKUBO Joseph" : "Logistics", "OBASOGIE Daisy" : "Accounting", 
       "OBI Samuel" : "Accounting", "OBIALOR Betha" : "Accounitng", "OGBONNA Boluwatife" : "Delivery", "OIGBOCHIE Mary" : "Delivery", "OKOCHA-OJEAH Raphael" : "Administration", 
       "OKOLO Victor" : "Administration", "OKORO Derek" : "Logistics", "OLOWOKERE Akorede" : "Accounting", "OLUBUADE Rasheed" : "Accounting", "OSEMEKE Daniel" : "Accounting", 
       "OSSAI Mary-Cynthia" : "Logistics", "PETER Owoede" : "Logistics", "QUADRI Oluwafikunmi" : "Delivery", "UDE-IBE Uchenna" : "Delivery", "UMEH Ejike" : "Administration"}
    
    if username in gig and gig[username] == dep:
        welcomeMessage(username)
    else:
        messagebox.showerror("Login" , "Invalid username or department\nOR\nYou are a non-existing employee\nNOTE:\nSurname must be in capital letters.\nIf surname or name has a hyphen, leave no spaces.")

root = tk.Tk()
root.title("GIG Login")
root.geometry("500x200")

username_label= tk.Label(root, text = "Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

department_label= tk.Label(root, text = "Department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

submit_button = tk.Button(root, text = "Submit", command = submit)
submit_button.pack()


root.mainloop()



