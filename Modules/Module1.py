# import libraries
# library voor het ophalen van tijd en datum informatie
from datetime import datetime
# library random voor in dit geval random keuzes
import random

# Functie van Module 1
def module1():
    print("-----MODULE 1-----")

    # Open "zuil_berichten.txt" met de naam file1
    file1 = open("zuil_berichten.txt", "a+")

    # Maak een list met 3 gekozen stations aan
    stations = ["Amsterdam", "Breda", "Haarlem"]

    # Kies 1 van de 3 stations
    station = random.choice(stations)

    # Input naar naam van de reiziger
    naam = input("Wat is uw naam?: ")

    # Stel de naam wordt niet ingevuld dan zal er "Anoniem" komen te staan
    if naam == "":
        naam = "Anoniem"

    # While True voor wanneer een bericht langer is dan 140 tekens
    while True:
        # Vragen naar het bericht van de reiziger
        bericht = input("Voer hier uw bericht in (maximaal 140 tekens): ")

        #Stel het bericht is langer dan 140 tekens dan zal het programma je vragen om het opnieuw te proberen
        if len(bericht) > 140:
            print("Het bericht mag niet langer zijn dan 140 tekens.")
            print("Uw bericht was {} tekens lang.\nprobeer het opnieuw:".format(len(bericht)))
            # continue betekend dat de While True opnieuw zal starten
            continue
        else:
            # Stel het bericht is korter dan 140 tekens,
            # zal de tijd, datum, random station, naam en het bericht worden geschreven naar het bestand
            file1.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')};{station};{naam};{bericht}\n")
            # Sluit het bestand
            file1.close()
            break
    # Voor extra informatie aan de reiziger zal het programma de naam en het bericht sturen
    print(f"Hallo {naam}!\nUw bericht:\n({bericht})\nzal worden nagekeken door een van onze moderators!")
    print("------------------")

# Run de functie module1()
module1()