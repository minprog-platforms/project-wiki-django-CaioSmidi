# PROCESBOEK WIKI


## Caio Smidi


### 3-12:
Vandaag was mijn eerste dag daadwerkelijk werken met Django sinds het kijken van het college, wat alweer een tijdje terug was. Na de belangrijkste dingen uit het college weer even te hebben herhaald, heb ik geprobeerd een begin te maken door de grote lijnen uit te tekenen in mijn Design Document. Door per knop en pagina na te denken over wat de mogelijkheden zijn van de website qua functionaliteit en bereik, werd het voor mijzelf wel wat duidelijker wat er allemaal moest gebeuren. In zekere zin haalde dit ook wat van de onzekerheid weg over waar ik moest beginnen.
Het is mij tot nu toe gelukt om de entry pages correct voor elkaar te krijgen. Het meeste en lastigste werk hiervan zat hem voor mij in het schrijven van de get_entrypage() functie in views.py, en de link hiervan naar entrypage.html. Vooral wat nou precies in de render functie als parameters meegegeven moeten worden en hoe dat zich weer vertaalt in het HTML bestand vond ik lastig. Nu het mij eenmaal gelukt is, heb ik er nog wat beter naar kunnen kijken en snap ik het wel goed.


### 6-12:
Vandaag ben ik aan de slag gegaan met het in orde maken van de index page. Het creëren van de links naar de entrypages was niet heel moeilijk, de moeilijkheid zat hem in het maken van de pages zelf, maar dat had ik gister al gedaan. Vandaag was het dus een kwestie van de juiste URL-links aan de tekst toevoegen.
De zoekbalk maken vond daarentegen wel erg lastig. Hier bleek dat het voor mij toch nog niet helemaal duidelijk was hoe forms nou precies werken. Ik heb van het college nog een keer het deel over forms bekeken, en vooral heel uitvoerig de Lecture Notes en de voorbeelden daarin gelezen. Na het enige uittesten en verdere documentatie op internet lezen ben ik tot een beter begrip gekomen over hoe een form te creëren, de keuze tussen de verschillende methods (POST en GET), en hoe informatie uit forms kan worden opgeslagen en doorgegeven.
Het in orde krijgen van de zoekbalk en de juiste pagina’s weergeven op basis van de search query heeft mij uiteindelijk wel bijna de hele dag gekost, maar het is gelukt. Vooral voor het geval dat de search query een substring van een of meerdere entries is, lukte het lang mij niet om het gewenste resultaat te krijgen. De moeilijkheid zat hier niet in het maken van de search_results.html page, maar in de juiste informatie (entries) doorspelen aan die page. Uiteindelijk is dit dus wel gelukt vandaag.


### 7-12:
Het terugkijken in mijn Design Document heeft heel erg geholpen voor mijn begrip van welke bestanden welke functie hebben binnen mijn repository. Dit bracht ook wat meer structuur in mijn volgorde van de aanpassingen die ik maakte wanneer ik een nieuwe pagina of functionaliteit toevoegde.
Hiermee ging ik aan de slag met het toevoegen van de “Create Page”, en “Edit Page” op iedere entrypage. Ook voor deze functionaliteiten was vooral een goed begrip van hoe forms werken belangrijk, dus mijn lange zoektocht van eerder voor de zoekbalk kwam hier goed van pas. Eigenlijk was dit verder niet heel veel ingewikkelder dan het maken van de zoekbalk, behalve dat er natuurlijk meer input letterlijk moet worden meegenomen in de nieuwe render.


### 9-12:
Vandaag heb ik tot slot de “Random Page” feature toegevoegd. Eigenlijk was dit een kwestie van de random module uit Python importeren en door middel van de choice() functie een willekeurige entry te kiezen uit de lijst en dit te renderen. Gelukkig kostte deze extra feature niet teveel tijd.


### 14-12:
Belangrijke note over GitHub: Ik had tot op heden nog niks gepusht naar GitHub, waardoor mijn voortgang niet te zien is geweest. Ik liep echter tegen een probleem aan dat bij het pushen naar GitHub mijn password authentication niet meer ondersteund werd, en na verschillende pogingen dit met een SSH-key op te lossen is het door hulp van een van de TA’s eindelijk gelukt om wel te kunnen pushen naar GitHub. Ik heb mijn (definitieve) versie van Wiki gepusht naar GitHub, exclusief dit procesboek en mijn Design Document zelf (deze moet ik allebei nog even mijn repository zetten).
Dit zal ik later vanavond doen en daarmee zal dat mijn laatste aanpassing aan het Wiki-project zijn.
