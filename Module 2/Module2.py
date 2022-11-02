import random
from datetime import datetime
import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "projectA",
    user = "postgres",
    password = "Wrdc21291",
    port = "25569")

cursor = connection.cursor()

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

def moderatie():
    while True:
        print("-----MODULE 2-----")
        email = input("Wat is uw email adres: ")
        naam = input("Wat is uw naam: ")

        cursor.execute("SELECT naam, email FROM moderator WHERE email = %s", [email])
        info = cursor.fetchone()

        if not info:
            break
        if naam == info[0]:
            break
        print("Naam/Email incorrect")

    cursor.execute("INSERT INTO moderator(naam, email) VALUES(%s,%s) ON CONFLICT DO NOTHING", [naam, email])
    cursor.execute("SELECT moderatorid FROM moderator WHERE email = %s", [email])
    moderatorId = cursor.fetchone()[0]

    with open("zuil_berichten.txt", "r+") as file:
        lines = file.readlines()

    lst = []
    for i in lines:

        info = i.strip("\n").split(";")
        print(f"{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}")

        while True:

            goedkeuring = input("Bericht goedgekeurd (y/n): ")
            if goedkeuring == "stop":
                break
            if goedkeuring == "y" or goedkeuring == "n":
                lst.append(i)
                break
            print("Ongelidge input")

        if goedkeuring == "y":
            goedkeuring = True
        else:
            goedkeuring = False

    with open("zuil_berichten.txt", "w") as file:
        for a in lines:
            if a not in lst:
                file.write(a)

        cursor.execute("SELECT stationid FROM station WHERE locatie = %s", [info[1]])
        stationId = cursor.fetchone()[0]
        cursor.execute("INSERT into bericht(bericht, datum, tijd, goedgekeurd, moderatorid, stationid, reiziger) VALUES(%s, %s, %s, %s, %s, %s, %s)", [info[3], info[0].split("-")[0], info[0].split("-")[1], goedkeuring, moderatorId, stationId, info[2]])
        connection.commit()

module1()
moderatie()