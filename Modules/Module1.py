from datetime import datetime
import random

def module1():
    print("-----MODULE 1-----")
    file1 = open("zuil_berichten.txt", "a+")
    stations = ["Amsterdam", "Breda", "Haarlem"]
    station = random.choice(stations)

    naam = input("Wat is uw naam?: ")

    if naam == "":
        naam = "Anoniem"

    while True:
        bericht = input("Voer hier uw bericht in (maximaal 140 tekens): ")
        if len(bericht) > 140:
            print("Het bericht mag niet langer zijn dan 140 tekens.")
            print("Uw bericht was {} tekens lang.\nprobeer het opnieuw:".format(len(bericht)))
            continue
        else:
            file1.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')};{station};{naam};{bericht}\n")
            file1.close()
            break
    print(f"Hallo {naam}!\nUw bericht:\n({bericht})\nzal worden nagekeken door een van onze moderators!")
    print("------------------")

module1()