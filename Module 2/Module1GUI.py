import tkinter as tk

file1 = open("../Module 1/zuil_berichten.txt", "r")
file1_data = file1.read()

# Configure window
window = tk.Tk()
window.title("Module 2 GUI")
window.geometry("500x500")
window.maxsize(700, 625)
window.minsize(700, 625)
window.configure(background='gold')

# Configure rows and columns
window.columnconfigure(0, minsize=180, weight=0)
window.columnconfigure(1, minsize=100, weight=1)
window.rowconfigure(0, minsize=30, weight=0)
window.rowconfigure(1, minsize=20, weight=0)

# Text window
txt_edit = tk.Text(window, height=35, width=55)
txt_edit.grid(row=1, column=1)
txt_edit.configure(background='lightblue')
txt_edit.configure(state='normal')
txt_edit.insert(tk.END, file1_data)
txt_edit.configure(state='disabled')

# Label
label_2 = tk.Label(window, text="Stations Zuil\nberichten systeembeheer", width=25, font=("bold", 10), background='gold')
label_2.grid(row=0, column=1)
label_2.place(x=0,y=0)

# Option Menu
OPTIONS = ["Breda", "Hoofddorp", "Almere"]

variable = tk.StringVar(window)
variable.set(OPTIONS[0])

station_list = tk.OptionMenu(window, variable, *OPTIONS)
station_list.grid(row=0, column=1)
station_list.place(x=10, y=50)

# Main loop
window.mainloop()
