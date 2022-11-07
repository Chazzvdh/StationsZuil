PROJECT StationsZuil 2022
Door: Chazz van den Hof
HBO-ICT / Utrecht

-----Module 1: Zuil-----

Op een zuil op een willekeurig NS-station kunnen reizigers hun bericht van maximaal 140 karakters invoeren. 
Het bericht moet worden opgeslagen in een tekstbestand met een logische structuur. 
Sla de onderstaande gegevens op in een gestructureerd tekstbestand:

* het bericht
* de datum en tijd van het bericht
* de naam van de reiziger – als de reiziger geen naam invult, gebruik dan als naam ‘anoniem’;
* het station – deze locatie van de zuil mag in de module zelf worden vastgelegd op basis van een random choice van drie stations. 
  De computer (jouw python computer programma) kiest dan één station uit deze lijstlijst downloaden en dat station wordt dan gekoppeld aan het bericht.
<img width="789" alt="image" src="https://user-images.githubusercontent.com/114153884/200292669-826b4b46-d1cc-4463-847f-88f16b6cf786.png">

-----Module 2: Moderatie-----

Voordat een bericht ook daadwerkelijk op het stationshalscherm wordt gezet, 
wordt er door een moderator van de NS naar de berichten gekeken. 
De moderator kan een bericht goed- of afkeuren. 
Alleen goedgekeurde berichten worden gepubliceerd op het stationshalscherm.

Deze module leest de berichten uit het gestructureerde tekstbestand (zoals beschreven bij module 1) in, 
beginnend bij het oudste bericht. 
Na beoordeling door een moderator wordt het hele bericht (inclusief datum, tijd, naam en station) naar een database geschreven. 
Daarnaast wordt de volgende data toegevoegd:

* Of het bericht is goedgekeurd of afgekeurd;
* De datum en tijd van beoordeling;
* De naam van moderator die het bericht heeft beoordeeld;
* Het email-adres van de moderator.
<img width="509" alt="image" src="https://user-images.githubusercontent.com/114153884/200293139-4ef35698-51f9-4ca5-8305-26900142b9b8.png">

-----Module 3: Stationshalscherm-----

In elke stationshal van Nederland komt een stationshalscherm te hangen. 
Op dit scherm worden de geplaatste berichten uit heel Nederland getoond:

* De berichten worden getoond op chronologische volgorde van invoeren. 
  Alleen de laatste 5 berichten worden getoond.
* Ook worden de beschikbare faciliteiten op het station getoond op het scherm. 
  Het gaat hierbij om het station waar het bericht is geschreven. 
  Een station heeft één of meer van de volgende faciliteiten: 
  	OV-fietsen, 
	lift, 
	toilet, 
	P+R. 
  De beschikbare faciliteiten staan in deze tabeltabel downloaden, 
  deze moet je toevoegen aan je database. 
  Je kunt eventueel gebruik maken van deze iconeniconen downloaden.
* Ten slotte wordt op het stationshalscherm de weersvoorspelling op de locatie van het station getoond. 
  Het gaat hierbij om het station waar het stationshalscherm hangt. 
  Voor het ophalen van de weersvoorspelling maak je gebruik van de OpenWeatherMap API
  (https://openweathermap.org/Koppelingen naar een externe site.).
<img width="872" alt="image" src="https://user-images.githubusercontent.com/114153884/200293280-103926e9-b498-4f37-a1e3-6c683aade0f4.png">
