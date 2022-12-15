import time
class Person(): #Her har vi en klasse for person. Alle personene følger denne og har egne subklasser innenfor som du bl.a ser på linje 15 nedenfor.
    def __init__(self, navn, alder, liker, likerIkke, linje, førsteValg=0, andreValg=0, sisteValg=0) -> None: #Her legger vi til atributtene navn, alder, hva de liker og ikke i tillegg til linjen de går.
        self.navn = navn
        self.alder = alder
        self.liker = liker
        self.likerIkke = likerIkke
        self.linje = linje
        self.førsteValg = førsteValg # Valgene er også atributter som har startverdi 0 og som endres til boolean for en positiv eller negativ reaksjon senere i programmet.
        self.andreValg = andreValg
        self.sisteValg = sisteValg
    
    def introduksjon(self): # Her har vi en metode innenfor Person som introduserer personen. De forskjellige klassene bruker også denne bortsett fra Brian sin hvor den oppdateres til å skrive ut "han" istedenfor "hun". Under ser vi også en forklaring av metoden som vil vises når du bruker den.
        """Funksjonen introduserer personene som er subklasser av Person-klassen. Defaulten er med pronomen hun og brukes for Olivia og Kat."""
        skrivOrd(f"{self.navn}, hun er {self.alder} år gammel. Hun liker {self.liker}, men liker ikke {self.likerIkke}. Hun går {self.linje}.")

class Olivia(Person): # Her har vi den første subklassen til Person hvor denne har alle funksjonene til Olivia
    def __init__(self, navn, alder, liker, likerIkke, linje, førsteValg=0, andreValg=0, sisteValg=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, førsteValg, andreValg, sisteValg) # Her innhenter den de tidligere atributtene til Person.
        
    def førsteSpørsmål(self): # Alle karakterene har en lik funksjon som heter førsteSpørsmål, men hva de sier er ulikt som forklarer hvorfor de står i hver subklasse.
        "Funksjonen tar ikke inn noen parametere og returnerer ingen verdier. Den endrer førsteValg til True eller False basert på om spilleren er frekk eller vennlig. Funksjonen finnes i hver av person-subklassene og gjør at svarene til hver person er unik. Hvilken rekkefølge man får opp svarene fra hver person bestemmes av spilleren"
        skrivOrd(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?") # Her får du spørsmålet om du vil være vennlig eller frekk
        førsteValg = sjekkVennFrekk() #Kaller funksjonen som sikrer at svaret er enten "frekk" eller "vennlig"
        if førsteValg == "vennlig": #Printer ut tekst basert på om spilleren valgte å være vennlig eller frekk
            self.førsteValg = True
            skrivOrd("")
            skrivOrd(f"{spillerNavn}: Hei! Jeg heter {spillerNavn}! Jeg synes du så hyggelig ut. ")
            skrivOrd("Olivia: Hei! Du er den nye eleven fra Malvik, er du ikke det? Veldig fint å hilse på deg. Jeg heter Olivia. ")
            skrivOrd(f"{spillerNavn}: Det er litt skummelt å være helt ny, men det er fint å vite at folk her er så hyggelige! ")
            skrivOrd("Olivia: Du bør snakke med Kat også, hun er kjempehyggelig. Mange synes hun er litt rar, hun er kjempeopptatt av spillet Minecraft, men det har jo ingenting å si. Hvis du har tid bør du bli kjent med henne. ")
            skrivOrd("(Dere snakker en stund helt til Olivia må gå. Kanskje du har tid til å snakke med noen andre?)")
            skrivOrd("")
        elif førsteValg == "frekk":
            self.førsteValg = False
            skrivOrd("")
            skrivOrd("(Du går bort til Olivia med et irritert ansiktuttrykk. Hun ser litt skremt ut)")
            skrivOrd(f"{spillerNavn}: Hva er problemet ditt da?")
            skrivOrd("Olivia: Uhm, ingenting. Jeg står her bare. Hvem er du? ")
            skrivOrd(f"{spillerNavn}: {spillerNavn}. Er ny på skolen. ")
            skrivOrd("Olivia: Ja ikke sant... Uansett...")
            skrivOrd("(Olivia snur seg tilbake til vennegruppen, uten å gi deg plass til å stå i ringen. Du snur deg og ser om du har noen andre å snakke med før timen starter.)")
            skrivOrd("")
        
    def andreSpørsmål(self): #Alle karakterene har denne funksjonen. Den spilles av hvis du velger å bli ekstra kjent med denne personen.
        skrivOrd("")
        skrivOrd(f"Du møter Olivia i mattetimen. Dere snakker litt underveis, men får ordentlig tid til å bli kjent i pausen.")
        skrivOrd("Hun viser deg en av hennes favorittbøker.")
        skrivOrd("Olivia: Han er så flink til å skrive! Kjenner du til forfatteren?")
        forfatterSvar = input()
        forfatterSvar = sjekkLaddeOrd(forfatterSvar)
        if forfatterSvar == False:
            skrivOrd("Olivia: Jaja, det er helt greit.")
            self.andreValg = False
        elif forfatterSvar == True:
            skrivOrd("Olivia: ...ja, hvem da? Du trenger ikke å lyge for at jeg skal like deg. ")
        elif forfatterSvar == "Lars Larsson":
            skrivOrd("Olivia: Vet du også om han? Så kult!")
            self.andreValg = True
        else:
            skrivOrd("Olivia: Hvem er det?")
            self.andreValg = False
    
    def sisteSpørsmål(self): #Alle karakterene har denne funksjonen. Spilles av etter andreSpørsmål. 
        skrivOrd("")
        skrivOrd("Olivia: Jeg har et veldig viktig spørsmål for deg. ")
        skrivOrd(f"{spillerNavn}: Oi. Nå ble jeg nervøs. ")
        skrivOrd("Olivia: Hva liker du best, hunder eller katter?")
        dyrValg = input()
        if dyrValg == "Hunder" or dyrValg == "hunder":
            self.sisteValg = True
            skrivOrd("Olivia: Jeg visste vi passet godt sammen! ")
        elif dyrValg == "Katter" or dyrValg == "katter":
            self.sisteValg = False
            skrivOrd("Olivia: Ugh nei, hunder er så mye bedre! ")
        else:
            self.sisteValg = False
            skrivOrd(f"Du er en merkelig type {spillerNavn}")

    def braEnding(self): #Alle karakterene har denne funksjonen. Spilles av hvis 2/3 valg  eller 3/3 valg er positive
        skrivOrd("")
        skrivOrd("(Det er nå to uker senere, og du og Olivia har blitt mye bedre kjent. En dag sitter dere og snakker hjemme hos henne.")
        skrivOrd("Olivia: Du, vi passer egentlig ganske godt sammen, har du tenkt over det?")
        skrivOrd(f"{spillerNavn}: Ja, det må jeg si meg enig i.")
        skrivOrd("(Du smiler til henne. Hun smiler tilbake)")
        skrivOrd("(Ett år senere er dere fortsatt sammen, og begge går på NTNU. Olivia studerer litteratur, og ønsker å bli enda bedre enn helten hennes Lars Larsson.)")
        skrivOrd("")
        skrivOrd("Du fikk ending 1, den brae endingen til Olivia, gratulerer! Det er totalt 6 forskjellige endings i spillet.")

    def dårligEnding(self): #Alle karakterene har denne funksjonen. Spilles av hvis 2/3 valg eller 3/3 valg er negative
        skrivOrd("")
        skrivOrd("(Olivia likte deg fra første gang dere møttes, men var redd for å si noe)")
        skrivOrd("(Etter at du og Olivia ikke kom godt overens, var Olivia helt knust. Hun droppet ut av skolen rett før slutten av vg3, og bor i dag i kjelleren til moren, uten å ha oppnådd noe i livet.)")
        skrivOrd("")
        skrivOrd("Du fikk ending 2, den dårlige endingen til Olivia. Det er totalt 6 forskjellige endings i spillet.")

class Kat(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, førsteValg=0, andreValg=0, sisteValg=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, førsteValg, andreValg=0, sisteValg=0)

    def førsteSpørsmål(self):
        skrivOrd(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        førsteValg = sjekkVennFrekk()
        if førsteValg == "vennlig":
            self.førsteValg = True
            skrivOrd("")
            skrivOrd(f"{spillerNavn}: Hei! Jeg er ny her og syntest du så snill ut. Jeg heter {spillerNavn}.")
            skrivOrd(f"Kat: Hei {spillerNavn}. Jeg heter Kat og går esportlinja fordi jeg elsker gaming. Du må ikke tro at jeg er glad i å lese. (Hun peker på boka hun har i hånda). Jeg leser den fordi den er av Lars Larsson, han er favorittforfatteren til Olivia. Kjenner du henne? Hun er ganske trivelig.")
            skrivOrd("(Dere snakker en stund om interesser dere begge har, helt til Kat må gå fordi hun har et prosjekt hun skal gjøre ferdig. Du leter igjen etter noen å snakke med før timen starter.)")
            skrivOrd("")
        elif førsteValg == "frekk":
            self.førsteValg = False
            skrivOrd("")
            skrivOrd(f"{spillerNavn}: Hvem er du da? Du ser rar ut.")
            skrivOrd(f"Kat: Uh hei? Hva er problemet ditt da? Jeg vet ikke engang hvem du er?")
            skrivOrd(f"{spillerNavn}: Jeg er {spillerNavn}.")
            skrivOrd("Kat: Åja. Du er den nye eleven fra Malvik.")
            skrivOrd("(Kat snur seg og går.)")
            skrivOrd("")
        
    def andreSpørsmål(self):
        skrivOrd("")
        skrivOrd("Du møter på Kat på bussholdeplassen på vei hjem.")
        skrivOrd(f"Kat: Hei {spillerNavn}, tar du også 3-bussen?")
        skrivOrd(f"{spillerNavn}:Ja det gjør jeg. Deilig å slutte tidlig eller? Jeg gleder meg til å komme hjem og ta en power-nap. ")
        skrivOrd("Kat: Jeg gleder meg til å komme hjem og spille favorittspillet mitt ")
        skrivOrd("(Du kommer på at du har hørt henne snakke om det før, men hva het det spillet igjen?)")
        favSpillSvar = input()
        if favSpillSvar == "Minecraft":
            self.andreValg = True
            skrivOrd("Kat: Ja! Elsker det spillet! ")
        else:
            self.andreValg = False
            skrivOrd("Kat: Hvilket spill er det? Har aldri hørt om det før. ")

    def sisteSpørsmål(self):
        skrivOrd("")
        skrivOrd("Kat: Du, jeg har et spørsmål til deg.")
        skrivOrd(f"{spillerNavn}: Oi, er det noe viktig?")
        skrivOrd("Kat: Hva er best, cola eller pepsi?")
        brusValg = input()
        if (brusValg == "Pepsi" or brusValg == "pepsi"):
            self.sisteValg = True
            skrivOrd("Kat: Niceee, helt enig.")
        elif (brusValg == "Monster" or brusValg == "monster"):
            self.sisteValg = True
            skrivOrd("Kat: Det var egentlig ikke et alternativ, men er likevel heelt enig.")
        elif brusValg == "Cola" or brusValg == "cola":
            self.sisteValg = False
            skrivOrd("Kat: Nei æsj hva er galt med deg.")
        else:
            self.sisteValg = False
            skrivOrd("Kat: Hæ hva mener du med det?")

    def braEnding(self):
        skrivOrd("")
        skrivOrd("(Etter en uke er du og Kat blitt veldig nære venner. Dere er hjemme hos deg og spiller Minecraft sammen.")
        skrivOrd("(Kat snur seg mot deg og kysser deg. Du blir overrasket, men kysser hun tilbake.)")
        skrivOrd("(Ett år senere er dere fortsatt sammen. Kat ble proff esportspiller og har allerede tjent store premiepenger i forskjellige konkurranser.)")
        skrivOrd("")
        skrivOrd("Du fikk ending 3, den brae endingen til Kat, gratulerer! Det er totalt 6 forskjellige endings i spillet.")

    def dårligEnding(self):
        skrivOrd("")
        skrivOrd("(Du og Kat har gått dårlig overens den første skoledagen på den nye skolen. Dagen etter finner du en lapp i skapet ditt.)")
        skrivOrd("Lapp: Finn meg bak skolen ved søppeldunken kl 14.00. -Kat")
        skrivOrd("(Du gjør som lappen sa, og ser Kat stå på det bestemte møtestedet deres.)")
        skrivOrd("Kat: Hvis det er en ting du bør vite om meg, er det at jeg ikke liker når andre ikke har respekt for meg. Det er flaut å bli sett med deg.")
        skrivOrd(f"{spillerNavn}: Sier du? Du er jo kjent på skolen for å være en skikkelig raring??")
        skrivOrd("(Fjeset til Kat blir rødt av sinne. Hun brøler noen banneord du ikke vet hva betyr engang. De virker alvorlige.)")
        skrivOrd("(Kat vokser og vokser, helt til hun dekker til solen. Hun har blitt om til et monster. Du hyler, men det er for sent. Hun spiser deg hel.)")
        skrivOrd("")
        skrivOrd("Du fikk ending 4, den dårlige endingen til Kat. Det er totalt 6 forskjellige endings i spillet.")

class Brian(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, førsteValg=0, andreValg=0, sisteValg=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, førsteValg, andreValg, sisteValg)
    
    def introduksjon(self):
        """Funksjonen introduserer Brian med pronomen han."""
        skrivOrd(f"{self.navn}, han er {self.alder} år gammel. Han liker {self.liker}, men liker ikke {self.likerIkke}. Han går {self.linje}.")

    def førsteSpørsmål(self):
        skrivOrd(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        førsteValg = sjekkVennFrekk()
        if førsteValg == "vennlig":
            self.førsteValg = True
            skrivOrd(f"{spillerNavn}: Hei! Jeg er ny her og syntest du så snill ut. Jeg heter {spillerNavn}.")
            skrivOrd(f"Brian: Hei {spillerNavn} jeg heter Brian. Jeg er 20 år, liker film, og går derfor media")
            skrivOrd("Du introduserer deg og dere snakker litt om skolen. Du ser deg rundt etter noen å snakke med før timen starter.")
            skrivOrd("")
        elif førsteValg == "frekk":
            self.førsteValg = False
            skrivOrd(f"{spillerNavn}: Halla kæm e du. Koffor går du rundt med så rare klær og den jalla røde kapsen")
            skrivOrd(f"Brian: Æ hete Brian kæm tror du at du e? Snakke om mine klær mens du går rundt som en jævla uteligger. Lukte dårlig og")
            skrivOrd("Brian: Du e en jævla nisse komm dæ ut av ansiktet mitt")
            skrivOrd("(Du går vekk)")
            skrivOrd("")
            
    def andreSpørsmål(self):
        skrivOrd("")
        skrivOrd(f"Du møter Brian i spansktimen. Han lurer litt på hva du liker og ikke liker.")
        skrivOrd("Brian: Hva synes du om filmer? ")
        filmValg1 = input()
        skrivOrd("Aaah ok. Har du sett interstellar da? Liker du den? ")
        filmValg1 = input()
        filmValg1 = sjekkLaddeOrd(filmValg1)
        if filmValg1 == True:
            skrivOrd("Herlig det er favorittfilmen min")
        elif filmValg1 == False:
            skrivOrd("Ok, skjønner.")
        else:
            skrivOrd("Hva betyr det?")
        skrivOrd("Brian: Liker du edderkopper da? ")
        
        eddiSvar = input()
        eddiSvar = sjekkLaddeOrd(eddiSvar)
        if eddiSvar == False:
            skrivOrd("Brian: Er helt enig med deg de er helt forferdelige")
            self.andreValg = True
        elif eddiSvar == True:
            skrivOrd("Brian: Hva faen er galt med deg de er jo så ekle")
            self.andreValg = False
        else:
            skrivOrd("Brian: Hæ")
            self.andreValg = False
    
    def sisteSpørsmål(self):
        skrivOrd("")
        skrivOrd("Brian: Yo kiz æ har et viktig spørsmål te dæ")
        skrivOrd(f"{spillerNavn}: Ait bet ka e det? ")
        skrivOrd("Brian: Trump eller Biden")
        presValg = input()
        if presValg == "Trump" or presValg == "trump":
            self.sisteValg = True
            skrivOrd("Brian: Jeg visste visste du ikke var en  ")
        elif presValg == "Biden" or presValg == "bide":
            self.sisteValg = False
            skrivOrd("Brian: Din jævla kommunist faan ")
        else:
            self.sisteValg = False
            skrivOrd(f"Virkelig??")

    def braEnding(self):
        skrivOrd("")
        skrivOrd("(Du tenker til deg selv at Brian var en snillere elev enn du trodde.)")
        skrivOrd("(Brian kommer senere under oppsyn av politiet for drap.)")
        skrivOrd("(Du tenker. Han var jo så snill det er jo umulig at han kunne gjort noe sånt)")
        skrivOrd("(Han flytter og kommer aldri tilbake.)")
        skrivOrd("")
        skrivOrd("Du fikk ending 5, den brae endingen til Brian, gratulerer! Det er totalt 6 forskjellige endings i spillet.")

    def dårligEnding(self):
        skrivOrd("")
        skrivOrd("(Brian virket fortsatt ganske hyggelig etter deres tidligere møte og innviterte deg ut å drikke)")
        skrivOrd("(Dere drakk ekstremt mye så du klarer ikke komme deg hjem.)")
        skrivOrd("Brian: Du kan overnatte hos meg jeg har en ekstra sofa og bor rett borti her.")
        skrivOrd("(Du går inn og ser at hele leiligheten er dekt i plastfolie. Du tenker ikke mye over det og han ber deg ta en plass på sofaen.)")
        skrivOrd("(Brian går på badet og kommer ut noen minutter senere i full regndrakt og en øks.)")
        skrivOrd(f"Brian: {spillerNavn} din jævla kommunist du fortjene å dø")
        skrivOrd("(Han løper mot deg og dreper deg med øksen)")
        skrivOrd("")
        skrivOrd("Du fikk ending 6, den dårlige endingen til Brian. Det er totalt 6 forskjellige endings i spillet.")

def gyldigSvar(valg):
    while valg!="Olivia":
        valg=input()
        if valg=="Brian":
            break
        elif valg=="Kat":
            break
        elif valg != "Olivia":
            skrivOrd("Navnet er ikke gyldig, prøv på nytt.")
    return valg
    
def sjekkVennFrekk():
    i=0
    while i==0:
        valg=input()
        if valg=="frekk":
            break
        elif valg == "vennlig":
            break
        else:
            skrivOrd("Svaret er ikke gyldig, prøv på nytt.")
    return valg
    print("")
    
#Sjekker om inputen fra spilleren er positivt eller negativt ladd
def sjekkLaddeOrd(spillerValg):
    """Funksjonen tar inn en tekststreng og sjekker hvert ord opp mot to lister, en med positivt ladde ord og en annen med negativt ladde ord. Den tar inn en tekststreng, som vil være inputen til spilleren, endrer så på den boolske verdien til variabelen (True for positivt og False for negativt), og returnerer denne nye verdien."""
    if " " in spillerValg:
            spillerValg = spillerValg.split()
            for i in spillerValg:
                for j in negativeOrd:
                    if i == j:
                        spillerValg = False
                for k in positiveOrd:
                    if k == i:
                        spillerValg = True
    else:
        for j in negativeOrd:
            if spillerValg == j:
                spillerValg = False
        for k in positiveOrd:
            if spillerValg == k:
                spillerValg = True
    return spillerValg

#Bytter ut "print" og skriver ut hvert ord separat med 0.15 sekunder mellom hver  
def skrivOrd(tekst):
    """Funksjonen skriver ut slik en print-funksjon gjør, men med 0.15 sekunder mellom hvert ord. Den tar inn tekststrenger, og returnerer ingenting."""
    x = tekst.split()
    for m in x:
        print(m+" ", end="")
        time.sleep(0.15)
    print("")

#To lister, den ene inneholder positivt ladde ord og den andre negativt ladde ord. Disse brukes til å sammenlikne med inputs fra spilleren for å tolke om inputen er positiv eller negativ
positiveOrd = ["Ja", "ja", "Definitivt", "definitivt", "Jepp", "jepp", "Jupp", "jupp", "Yes", "yes", "Jada", "jada", "Jo", "jo", "Ganske", "ganske", "Sikkert", "sikkert", "Jau", "jau"]
negativeOrd = ["Nei", "nei", "Ikke", "ikke", "Niks", "niks", "Tvilsomt", "tvilsomt", "Nope", "nope", "Nah", "nah", "No", "no", "Tja", "tja", "Tviler", "tviler", "idk", "Idk"]

Olivia = Olivia("Olivia", 18, "å bake", "trening", "studiespesialisering") #Definerer verdiene til attributtene til subklassen Olivia
Brian = Brian("Brian", 20, "film", "edderkopper", "MK") #Definerer verdiene til attributtene til subklassen Brian
Kat = Kat("Kat", 19, "videospill", "skole", "Esport") #Definerer verdiene til attributtene til subklassen Kat

personListe = ["Olivia", "Brian", "Kat"] #Definerer listen over personene, som brukes i dannelsen av rekkefølgen som spilleren bestemmer

#Her starter selve spillet, alt over er definisjoner av klasser, subklasser, funksjoner, ordbøker og lister
skrivOrd("")
skrivOrd("Hei, velkommen til charlottenlund videregående skole. Det er din første dag på denne skolen etter at du flyttet fra gokk(Malvik). Nå er det lunsj, men du fant ingen å spise lunsj med i klassen din. Du ser tre vennlige fjes som du kanskje vil bli kjent med bedre.")
skrivOrd("Hva heter du?")
spillerNavn = input()
skrivOrd("")

skrivOrd("Først har vi ") #Introduserer alle karakterene med funksjoner som ligger under klassen person og subklassen Brian
Olivia.introduksjon()
skrivOrd("Så har vi ")
Brian.introduksjon()
skrivOrd("Til slutt har vi ")
Kat.introduksjon()
skrivOrd("")


skrivOrd(f"Hvem vil du snakke med? {personListe[0]}, {personListe[1]} eller {personListe[2]}? ") #Spilleren velger den første personen de vil snakke med. Man må snakke med alle tre for å bli introdusert ordentlig, men kan velge rekkefølgen
personValg1 = ""
personValg1 = gyldigSvar(personValg1)
i=0

if personValg1 == "Olivia": #Lar personen velge rekkefølgen man vil snakke med personene i. Inneholder også biter med kode som passer på at det som skrives inn er gyldig.
    Olivia.førsteSpørsmål()
    personListe.remove("Olivia")
    skrivOrd(f"Hvem vil du snakke med nå? {personListe[0]} eller {personListe[1]}? ")
    nestValg1=""
    while i==0:
        nesteValg1=input()
        if nesteValg1==personListe[0]:
            break
        elif nesteValg1==personListe[1]:
            break
        else:
            skrivOrd("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Brian":
        Brian.førsteSpørsmål()
        personListe.remove("Brian")
    elif nesteValg1 == "Kat":
        Kat.førsteSpørsmål()
        personListe.remove("Kat")        

elif personValg1 == "Brian": 
    Brian.førsteSpørsmål()
    personListe.remove("Brian")
    skrivOrd(f"Hvem vil du snakke med nå? {personListe[0]} eller {personListe[1]}? ")
    nesteValg1 = ""
    while i==0:
        nesteValg1=input()
        if nesteValg1==personListe[1]:
            break
        elif nesteValg1 == personListe[0]:
            break
        else:
            skrivOrd("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Olivia":
        Olivia.førsteSpørsmål()
        personListe.remove("Olivia")
    elif nesteValg1 == "Kat":
        Kat.førsteSpørsmål()        
        personListe.remove("Kat")

elif personValg1 == "Kat": 
    Kat.førsteSpørsmål()
    personListe.remove("Kat")
    skrivOrd(f"Hvem vil du snakke med nå? {personListe[0]} eller {personListe[1]}? ")
    nesteValg1 = ""
    while nesteValg1!=personListe[0]:
        nesteValg1=input()
        if nesteValg1==personListe[1]:
            break
        elif nesteValg1 == personListe[0]:
            break
        else:
            skrivOrd("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Brian":
        Brian.førsteSpørsmål()
        personListe.remove("Brian")
    elif nesteValg1 == "Olivia":
        Olivia.førsteSpørsmål()
        personListe.remove("Olivia")

if personListe[0] == "Olivia":
    Olivia.førsteSpørsmål()
elif personListe[0] == "Brian":
    Brian.førsteSpørsmål()
elif personListe[0] == "Kat":
    Kat.førsteSpørsmål()

skrivOrd("")
skrivOrd("Timen starter, så du har ikke tid til å snakke med flere. I timen sitter du og reflekterer over de tre ny personene du har møtt i lunsjpausen.")
skrivOrd("")   
skrivOrd("Du føler deg spesielt tiltrukket til en av dem, og tenker at du vil bli ekstra godt kjent med de. Hvem er det?")
personValg2 = ""
personValg2 = gyldigSvar(personValg2) #Lar spilleren velge hvilken person de vil snakke videre med. Da lukkes endings for de andre to personene.

if personValg2 == "Olivia": #Gjør om fra tekstinputen som er en string og til subklassen til personen
    personValg2 = Olivia
elif personValg2 == "Brian":
    personValg2 = Brian
elif personValg2 == "Kat":
    personValg2 = Kat

personValg2.andreSpørsmål() #Spiller av den valgte personens andre spørsmål

personValg2.sisteSpørsmål() #Spiller av den valgte personens siste spørsmål

antallpositiv = 0
if personValg2.førsteValg == True: #Teller opp hvor mange av de tre valgene var positive. Hvis valget = True, ble det motatt positivt
    antallpositiv+=1
if personValg2.andreValg == True:
    antallpositiv+=1
if personValg2.sisteValg == True:
    antallpositiv+=1

if (antallpositiv >=2): #Hvis 2/3 eller 3/3 valg var positivt motatt vil den bra endingen til den valgte personen spilles av. Eller spilles av den dårlige endingen
    personValg2.braEnding()
else:
    personValg2.dårligEnding()