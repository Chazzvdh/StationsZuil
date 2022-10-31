import datetime
import random

file1 = open("zuil_berichten.txt", "a+")
stations = ["Amsterdam", "Breda", "Haarlem"]
station = random.choice(stations)

naam = input("Wat is uw naam?: ")
current_time = datetime.datetime.now().strftime('%y-%m-%d %H:%M')

if naam == "":
    naam = "Anoniem"

while True:
    bericht = input("Voer hier uw bericht in (maximaal 140 tekens): ")
    if len(bericht) > 140:
        print("Het bericht mag niet langer zijn dan 140 tekens.")
        print("Uw bericht was {} tekens lang.\nprobeer het opnieuw:".format(len(bericht)))
        continue
    else:
        file1.write("Naam gebruiker: {};"
                    "Datum en tijd {};"
                    "Bericht: {};"
                    "Station: {};\n".format(naam, current_time, bericht, station))
        file1.close()
        break

file1 = open("zuil_berichten.txt", "r")
data = file1.read()
data = data.split(";")
print(data)
file1.close()



