from tkinter import *
from tkinter.font import Font
import requests
from PIL import Image, ImageTk
import psycopg2

def import_data_station(row_id):
    try:
        connection = psycopg2.connect(
            host = "localhost",
            database = "projectA",
            user = "postgres",
            password = "Wrdc21291",
            port = "25569")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from station"
        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()
        station_data = data[row_id]

        text2 = station_data
    except (Exception, psycopg2.Error) as error:
        print(f"Error ({error}) tijdens het vragen naar data van PostgreSQL")

    finally:
        if connection:
            cursor.close()
            connection.close()

    return text2

def import_data_bericht(row_id):
    try:
        connection = psycopg2.connect(
            host = "localhost",
            database = "projectA",
            user = "postgres",
            password = "Wrdc21291",
            port = "25569")

        cursor = connection.cursor()
        postgreSQL_select_Query1 = "select * from bericht"
        cursor.execute(postgreSQL_select_Query1)
        berichten_data = cursor.fetchall()
        berichten = berichten_data[row_id]

        bericht = berichten[0]
        datum = berichten[1]
        tijd = berichten[2]
        goedgekeurd = berichten[3]
        naam = berichten[4]
        moderator_id = berichten[5]
        station = berichten[6]

        if station == 1:
            station_naam = "Amsterdam"
        elif station == 2:
            station_naam = "Haarlem"
        elif station == 3:
            station_naam = "Breda"
        else:
            station_naam = "None"

    except (Exception, psycopg2.Error) as error:
        print(f"Error ({error}) tijdens het vragen naar data van PostgreSQL")

    finally:
        if connection:
            cursor.close()
            connection.close()

    return bericht,datum,tijd,goedgekeurd,naam,moderator_id,station,station_naam

def clicked():
    l1.configure(text=f"Station: {option.get()}\nTemperature: {getWeatherData(option.get())[1]}°C\nDescription: {getWeatherData(option.get())[0]}")

    if option.get() == "Amsterdam":
        label3 = Label(master=window, image=img_lift_r)
        label3.grid(row=1, column=1, sticky=W)
        label4 = Label(master=window, image=img_pr_r)
        label4.grid(row=1, column=1, sticky=E)
    elif option.get() == "Haarlem":
        label3 = Label(master=window, image=img_ovfiets_r)
        label3.grid(row=1, column=1, sticky=W)
        label4 = Label(master=window, image=img_toilet_r)
        label4.grid(row=1, column=1, sticky=E)
    elif option.get() == "Breda":
        label3 = Label(master=window, image=img_lift_r)
        label3.grid(row=1, column=1, sticky=W)
        label4 = Label(master=window, image=img_pr_r)
        label4.grid(row=1, column=1, sticky=E)

    #window.update()
    print(f"Refresh weather data voor: '{option.get()}'")
    print(f"Refresh info voor station: '{option.get()}'")
    return

def getWeatherData(station):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ca6a55a3a2834c3f154a90676cb9b565&units=metric&lang=nl'.format(station)

    res = requests.get(url)
    data = res.json()

    description = data['weather'][0]['description']
    temp = data['main']['temp']

    return description.capitalize(),temp

window = Tk()
window.title("Module 3")
window.resizable(False, False)
window.configure(bg="gray20")

img_ovfiets = Image.open("img_ovfiets.png")
resize_image1 = img_ovfiets.resize((80, 80))
img_ovfiets_r = ImageTk.PhotoImage(resize_image1)

img_lift = Image.open("img_lift.png")
resize_image2 = img_lift.resize((80, 80))
img_lift_r = ImageTk.PhotoImage(resize_image2)

img_toilet = Image.open("img_toilet.png")
resize_image3 = img_toilet.resize((80, 80))
img_toilet_r = ImageTk.PhotoImage(resize_image3)

img_pr = Image.open("img_pr.png")
resize_image4 = img_pr.resize((80, 80))
img_pr_r = ImageTk.PhotoImage(resize_image4)

my_font1 = Font(
    family = 'Arial',
    size = 15,
    weight = 'bold',
    slant = 'roman',
    underline = False,
    overstrike = False
)

my_font2 = Font(
    family = 'Arial',
    size = 14,
    weight = 'bold',
    slant = 'roman',
    underline = False,
    overstrike = False
)

label2 = Label(window)
label2.configure(bg="grey18")
label2.grid(row=0, column=0, rowspan=1, columnspan=3, sticky=NSEW)

option = StringVar(window)
option.set("Amsterdam")
option_menu = OptionMenu(window, option, "Amsterdam", "Haarlem", "Breda")
option_menu.configure(font=my_font2, activebackground="grey40", activeforeground="grey100", bg="grey25", fg="white")
option_menu.grid(row=0, column=0, rowspan=1, columnspan=1, ipady=5, ipadx=10, sticky=W)

button1 = Button(window, command=clicked)
button1.configure(text="Refresh", font=my_font2, activebackground="grey40", activeforeground="grey100", bg="grey25", fg="white")
button1.grid(row=0, column=2, rowspan=1, columnspan=1, ipady=5, ipadx=10, sticky=E)

image1 = Image.open("ns-logo2.png")
resize_image = image1.resize((100, 50))
img1 = ImageTk.PhotoImage(resize_image)
label1 = Label(master=window, image=img1)
label1.configure(bg="gray20")
label1.grid(row=1, column=2, rowspan=1, columnspan=1, ipadx=20, ipady=20, sticky=E)

label3 = Label(master=window, image=img_lift_r)
label3.grid(row=1, column=1, sticky=W)
label4 = Label(master=window, image=img_pr_r)
label4.grid(row=1, column=1, sticky=E)

l1 = Label(window, justify=LEFT, text=f"Station: {option.get()}\nTemperature: {getWeatherData(option.get())[1]}°C\nDescription: {getWeatherData(option.get())[0]}")
l1.configure(bg="gray20", fg="gray80", font=my_font1, anchor="center")
l1.grid(row=1, column=0, rowspan=1, columnspan=1, ipadx=10, ipady=10, sticky=W)

# Maak text boxes aan met de bijhorende configuraties en import data vanuit het database
text1 = Text(window, width=100)
text1.configure(font=my_font2, fg="white", bg="grey18", height=6)
text1.insert(INSERT, f"{import_data_bericht(-1)[4]},\n{import_data_bericht(-1)[7]} / {import_data_bericht(-1)[1]} / {import_data_bericht(-1)[2]}\n{import_data_bericht(-1)[0]}")
text1.configure(state="disabled")
text1.grid(row=3, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text2 = Text(window, width=100)
text2.configure(font=my_font2, fg="white", bg="grey18", height=6)
text2.insert(INSERT, f"{import_data_bericht(-2)[4]},\n{import_data_bericht(-2)[7]} / {import_data_bericht(-2)[1]} / {import_data_bericht(-2)[2]}\n{import_data_bericht(-2)[0]}")
text2.configure(state="disabled")
text2.grid(row=4, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text3 = Text(window, width=100)
text3.configure(font=my_font2, fg="white", bg="grey18", height=6)
text3.insert(INSERT, f"{import_data_bericht(-3)[4]},\n{import_data_bericht(-3)[7]} / {import_data_bericht(-3)[1]} / {import_data_bericht(-3)[2]}\n{import_data_bericht(-3)[0]}")
text3.configure(state="disabled")
text3.grid(row=5, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text4 = Text(window, width=100)
text4.configure(font=my_font2, fg="white", bg="grey18", height=6)
text4.insert(INSERT, f"{import_data_bericht(-4)[4]},\n{import_data_bericht(-4)[7]} / {import_data_bericht(-4)[1]} / {import_data_bericht(-4)[2]}\n{import_data_bericht(-4)[0]}")
text4.configure(state="disabled")
text4.grid(row=6, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

text5 = Text(window, width=100)
text5.configure(font=my_font2, fg="white", bg="grey18", height=6)
text5.insert(INSERT, f"{import_data_bericht(-5)[4]},\n{import_data_bericht(-5)[7]} / {import_data_bericht(-5)[1]} / {import_data_bericht(-5)[2]}\n{import_data_bericht(-5)[0]}")
text5.configure(state="disabled")
text5.grid(row=7, column=0, rowspan=1, columnspan=3, ipady=0, ipadx=20, padx=10, pady=5)

window.mainloop()

