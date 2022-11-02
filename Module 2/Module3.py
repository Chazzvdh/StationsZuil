import random
from tkinter import *
from tkinter.font import Font
import requests
from PIL import Image, ImageTk

def clicked():
    l1.configure(text=f"Station: {option.get()}\nTemperature: {getData(option.get())[4]}°C\nDescription: {getData(option.get())[3]}")
    window.update()
    print(f"Refresh weather data voor: '{option.get()}'")
    return

def getData(station):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ca6a55a3a2834c3f154a90676cb9b565&units=metric&lang=nl'.format(station)

    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    return humidity,pressure,wind,description.capitalize(),temp

window = Tk()
window.title("Module 3")
window.resizable(False, False)
window.configure(bg="gray20")

my_font1 = Font(
    family = 'Arial',
    size = 20,
    weight = 'bold',
    slant = 'roman',
    underline = False,
    overstrike = False
)

my_font2 = Font(
    family = 'Arial',
    weight = 'bold',
    slant = 'roman',
    underline = False,
    overstrike = False
)

label2 = Label(window)
label2.configure(bg="grey18")
label2.grid(row=0, column=0, rowspan=1, columnspan=4, sticky=NSEW)

option = StringVar(window)
option.set("Amsterdam")
option_menu = OptionMenu(window, option, "Amsterdam", "Haarlem", "Breda")
option_menu.configure(font=my_font2, activebackground="grey40", activeforeground="grey100", bg="grey25", fg="gray100")
option_menu.grid(row=0, column=0, rowspan=1, columnspan=1, ipady=5, ipadx=10, sticky=W)

button1 = Button(window, command=clicked)
button1.configure(text="Refresh", font=my_font2, activebackground="grey40", activeforeground="grey100", bg="grey25", fg="gray100")
button1.grid(row=0, column=3, rowspan=1, columnspan=1, ipady=5, ipadx=10, sticky=E)

image = Image.open("ns-logo2.png")
resize_image = image.resize((100, 50))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(master=window, image=img)
label1.configure(bg="gray20")
label1.grid(row=1, column=3, rowspan=1, columnspan=1, ipadx=20, ipady=20, sticky=E)

l1 = Label(window, justify=LEFT, text=f"Station: {option.get()}\nTemperature: {getData(option.get())[4]}°C\nDescription: {getData(option.get())[3]}")
l1.configure(bg="gray20", fg="gray80", font=my_font1, anchor="center")
l1.grid(row=1, column=0, rowspan=1, columnspan=1, ipadx=10, ipady=10, sticky=W)

text1 = Text(window)
text1.configure(font=my_font2, fg="white", bg="grey18", height=6)
text1.configure(state="disabled")
text1.grid(row=3, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text2 = Text(window)
text2.configure(font=my_font2, fg="white", bg="grey18", height=6)
text2.configure(state="disabled")
text2.grid(row=4, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text3 = Text(window)
text3.configure(font=my_font2, fg="white", bg="grey18", height=6)
text3.configure(state="disabled")
text3.grid(row=5, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text4 = Text(window)
text4.configure(font=my_font2, fg="white", bg="grey18", height=6)
text4.configure(state="disabled")
text4.grid(row=6, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text5 = Text(window)
text5.configure(font=my_font2, fg="white", bg="grey18", height=6)
text5.configure(state="disabled")
text5.grid(row=7, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)


window.mainloop()

