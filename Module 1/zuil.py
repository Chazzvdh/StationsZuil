import datetime
import random

file1 = open("zuil_berichten.txt", "a+")
stations = open('stations.txt').read().splitlines()
station = random.choice(stations)

naam = input("Wat is uw naam?: ")
current_time = datetime.datetime.now()
bericht = input("Voer hier uw bericht in met een maximale va 140 tekens: ")

file1.write("Naam gebruiker: {}\nDatum en tijd {}\nBericht: {}\nStation: {}\n\n".format(naam, current_time, bericht, station))
file1.close()