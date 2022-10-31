from tkinter import *
from tkinter import messagebox
from functools import partial
import os

def validateLogin(username, password):
    print(username.get())
    print(password.get())
    if username.get() == "Chazz" and password.get() == 'chazz@ns.nl':
        os.system('python Module2GUI.py')
    else:
        messagebox.showerror('Error', 'Error: Informatie onjuist!')
    return

# window
window2 = Tk()
window2.title('Login')
window2.minsize(400, 300)
window2.maxsize(400, 300)

# username label and text entry box
usernameLabel = Label(window2, text="Naam")
usernameLabel.pack()
username = StringVar()
usernameEntry = Entry(window2, textvariable=username)
usernameEntry.pack()

# password label and password entry box
passwordLabel = Label(window2, text="E-Mail")
passwordLabel.pack()
password = StringVar()
passwordEntry = Entry(window2, textvariable=password)
passwordEntry.pack()

validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(window2, text="Login", command=validateLogin)
loginButton.pack()

window2.mainloop()
