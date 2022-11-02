# Import modules
from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import random
goedgekeurd_clicked = False
afgekeurd_clicked = False
def goedgekeurd():
    goedgekeurd_clicked = 'y'
    print("Goedgekeurd")
    return

def afgekeurd():
    afgekeurd_clicked = True
    print("Afgekeurd")
    return

window = Tk()
window.title("Module2")
window.configure()

stations = ["Amsterdam", "Breda", "Haarlem"]
station = random.choice(stations)

time = datetime.now().strftime('%H:%M')

file1 = open("../Module 1/zuil_berichten.txt", "r+")
lines = file1.readlines()
lst = []

window.minsize(1000, 600)
window.maxsize(1000, 600)
window.resizable(False, False)

image = Image.open("nslogo.png")
resize_image = image.resize((100, 50))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.place(x=880, y=20)

label2 = Label(master=window, text=time)
label2.configure(foreground="navy", font=("Helvetica", 40))
label2.place(x=20, y=20)

label3 = Label(master=window, text=station)
label3.configure(font=("Helvetica", 30), foreground="navy")
label3.pack(pady=20,padx=130,side=TOP, anchor='e')

label4 = Label(master=window, text="")
label4.configure(background="navy", width=1000, height=3)
label4.pack(side=BOTTOM, anchor='w')

button1 = Button(master=window, text='Goedgekeurd', command=goedgekeurd)
button1.configure(cursor="hand2", background='white', foreground='navy', width=15, height=2, font=("Helvetica", 15))
button1.place(x=20, y=90)

button2 = Button(master=window, text='Afgekeurd', command=afgekeurd)
button2.configure(cursor="hand2", background='white', foreground='navy', width=15, height=2, font=("Helvetica", 15))
button2.place(x=20, y=170)

txt_edit = Text(window, height=20, width=69)
txt_edit.pack(padx=20, pady=0, anchor='e')
txt_edit.configure(foreground='navy', font=("Helvetica",15))
txt_edit.configure(state='normal')

text = ''

for i in lines:
    info = i.strip("\n").split(";")
    if goedgekeurd_clicked == 'y':
        text += (f"{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}\n\n")

    txt_edit.insert(END, text)

txt_edit.insert(END, text)
txt_edit.configure(state='disabled')

window.mainloop()
