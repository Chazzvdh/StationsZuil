# Import libraries

# import datatime voor de tijd en datum
from datetime import datetime

# import psycopg2 voor de connectie met PostgreSQL en het database
import psycopg2

# Benodigde informatie om bij PostgreSQL in te loggen
connection = psycopg2.connect(
    host = "localhost",
    database = "projectA",
    user = "postgres",
    password = "Wrdc21291",
    port = "25569")

# Maak variabel cursor aan om uit het database te kunnen lezen
cursor = connection.cursor()

# Functie voor Module 2
def moderatie():

    # While true voor checken informatie moderator
    while True:
        print("-----MODULE 2-----")

        # Opvragen informatie moderator (naam, e-mail)
        email = input("Wat is uw email adres: ")
        naam = input("Wat is uw naam: ")

        # Check datum en tijd
        checktime = datetime.now().strftime('%H:%M:%S')
        checkdate = datetime.now().strftime('%d/%m/%Y')

        # Zoek een lees vanuit het database
        # naam, email.
        # Waar email hetzelfde is als de ingevoerde email.
        cursor.execute("SELECT naam, email FROM moderator WHERE email = %s", [email])

        # verzamel alle informatie van dat deel van de database
        info = cursor.fetchone()

        # Stel er is geen info dan zal het programma een email adres met naam toevoegen
        if not info:
            print("Er is geen moderator info beschikbaar,")
            print("uw email en naam wordt toegevoegd aan het database!")
            break
        # Stel de combinatie is correct dan zal het programma door gaan met de ingevoerde informatie
        if naam == info[0]:
            break
        # Stel de combinatie is niet correct dan zal het programma
        # opnieuw vragen naar de informatie van de moderator.
        print("Naam/Email incorrect")


    # Stel de moderator informatie bestaat al dan zal er niets worden toegevoegd.
    cursor.execute("INSERT INTO moderator(naam, email) VALUES(%s,%s) ON CONFLICT DO NOTHING", [naam, email])

    # Welke moderator bezig is met het systeem wordt opgeslagen
    cursor.execute("SELECT moderatorid FROM moderator WHERE email = %s", [email])
    moderatorId = cursor.fetchone()[0]

    print("------------------")

    # Open "zuil_berichten.txt" als file
    with open("zuil_berichten.txt", "r+") as file:
        # Lees alle lines uit
        lines = file.readlines()

    # Maak een list aan genaamd lst
    lst = []

    # Ga alle lines af in de opgeslagen informatie uit het bestand
    for i in lines:

        # Split alle info bij ";"
        info = i.strip("\n").split(";")

        # Print alle info met een bepaalde volgorde
        print(f"{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}")

        # While True voor wanneer er geen geldige invoer is.
        while True:

            # Vraag om goedkeuring van het bericht
            goedkeuring = input("Bericht goedgekeurd (y/n): ")

            # Stel de input is "Stop" dan zal het programme stoppen
            if goedkeuring == "stop":
                break
            # Stel de moderator voert "y" of "n" in,
            # zal alle informatie worden opgeslagen in de list "lst"
            if goedkeuring == "y" or goedkeuring == "n":
                lst.append(i)
                break
            # Ongeldige input
            print("Input ongeldig, gebruik alstublieft: y/n")

        # Goedkeuring True of False opgeslagen in een variabel
        if goedkeuring == "y":
            goedkeuring = True
        else:
            goedkeuring = False

        # Open "zuil_berichten.txt" als file
        with open("zuil_berichten.txt", "w") as file:
            # Maakt het bestand leeg
            for a in lines:
                if a not in lst:
                    file.write(a)

            # Selecteer het station waar het station gelijk staat aan het meegegeven station uit de txt file
            cursor.execute("SELECT stationid FROM station WHERE locatie = %s", [info[1]])

            # Selecteer alle informatie uit stationid
            stationId = cursor.fetchone()[0]

            # Voeg alle verzamelde informatie toe aan de commit informatie voor het database
            cursor.execute("INSERT into bericht(bericht, datum, tijd, goedgekeurd, moderatorid, stationid, reiziger, checktime, checkdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", [info[3], info[0].split("-")[0], info[0].split("-")[1], goedkeuring, moderatorId, stationId, info[2], checktime, checkdate])

            # Commit alle informatie naar het database
            connection.commit()

    print("------------------")

# Run de functie moderatie()
moderatie()