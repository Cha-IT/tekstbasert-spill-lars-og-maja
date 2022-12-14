class Person():
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0, valg3=0) -> None:
        self.navn = navn
        self.alder = alder
        self.liker = liker
        self.likerIkke = likerIkke
        self.linje = linje
        self.valg2 = valg2
        self.valg3 = valg3
    
    def introduksjon(self):
        """Funksjonen introduserer personene som er subklasser av Person-klassen. Defaulten er med pronomen hun og brukes for Olivia og Kat."""
        print(f"{self.navn}, hun er {self.alder} år gammel. Hun liker {self.liker}, men liker ikke {self.likerIkke}. Hun går {self.linje}.")

class Olivia(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0, valg3=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, valg2, valg3)
        
    def førsteSpørsmål(self):
        print(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        valg2 = ""
        i=0
        while i==0:
            valg2=input()
            if valg2=="frekk":
                break
            elif valg2 == "vennlig":
                break
            else:
                print("Svaret er ikke gyldig, prøv på nytt.")
        if valg2 == "vennlig":
            self.valg2 = True
            print("")
            print(f"{spillerNavn}: Hei! Jeg heter {spillerNavn}! Jeg synes du så hyggelig ut. ")
            print("Olivia: Hei! Du er den nye eleven fra Malvik, er du ikke det? Veldig fint å hilse på deg. Jeg heter Olivia. ")
            print(f"{spillerNavn}: Det er litt skummelt å være helt ny, men det er fint å vite at folk her er så hyggelige! ")
            print("Olivia: Du bør snakke med Kat også, hun er kjempehyggelig. Mange synes hun er litt rar, hun er kjempeopptatt av spillet Minecraft, men det har jo ingenting å si. Hvis du har tid bør du bli kjent med henne. ")
            print("(Dere snakker en stund helt til Olivia må gå. Kanskje du har tid til å snakke med noen andre?)")
            print("")
        elif valg2 == "frekk":
            self.valg2 = False
            print("")
            print("(Du går bort til Olivia med et irritert ansiktuttrykk. Hun ser litt skremt ut)")
            print(f"{spillerNavn}: Hva er problemet ditt da?")
            print("Olivia: Uhm, ingenting. Jeg står her bare. Hvem er du? ")
            print(f"{spillerNavn}: {spillerNavn}. Er ny på skolen. ")
            print("Olivia: Ja ikke sant... Uansett...")
            print("(Olivia snur seg tilbake til vennegruppen, uten å gi deg plass til å stå i ringen. Du snur deg og ser om du har noen andre å snakke med før timen starter.)")
            print("")
        
    def andreSpørsmål(self):
        print("")
        print(f"Du møter Olivia i mattetimen. Dere snakker litt underveis, men får ordentlig tid til å bli kjent i pausen.")
        print("Hun viser deg en av hennes favorittbøker.")
        print("Olivia: Han er så flink til å skrive! Kjenner du til forfatteren?")
        forfatterSvar = input()
        if forfatterSvar == "Nei":
            print("Olivia: Jaja, det er helt greit.")
            self.valg3 = False
        elif forfatterSvar == "Lars Larsson":
            print("Olivia: Vet du også om han? Så kult!")
            self.valg3 = True
        else:
            print("Olivia: Hvem er det?")
            self.valg3 = False
    
    def sisteSpørsmål(self):
        print("")
        print("Olivia: Jeg har et veldig viktig spørsmål for deg. ")
        print(f"{spillerNavn}: Oi. Nå ble jeg nervøs. ")
        print("Olivia: Hva liker du best, hunder eller katter?")
        dyrValg = input()
        if dyrValg == "Hunder" or dyrValg == "hunder":
            self.valg4 = True
            print("Olivia: Jeg visste vi passet godt sammen! ")
        elif dyrValg == "Katter" or dyrValg == "katter":
            self.valg4 = False
            print("Olivia: Ugh nei, hunder er så mye bedre! ")
        else:
            self.valg4 = False
            print(f"Du er en merkelig type {spillerNavn}")

    def braEnding(self):
        print("")
        print("(Det er nå to uker senere, og du og Olivia har blitt mye bedre kjent. En dag sitter dere og snakker hjemme hos henne.")
        print("Olivia: Du, vi passer egentlig ganske godt sammen, har du tenkt over det?")
        print(f"{spillerNavn}: Ja, det må jeg si meg enig i.")
        print("(Du smiler til henne. Hun smiler tilbake)")
        print("(Ett år senere er dere fortsatt sammen, og begge går på NTNU. Olivia studerer litteratur, og ønsker å bli enda bedre enn helten hennes Lars Larsson.)")
        print("")
        print("Du fikk ending 1, den brae endingen til Olivia, gratulerer! Det er totalt 6 forskjellige endings i spillet.")

    def dårligEnding(self):
        print("")
        print("(Olivia likte deg fra første gang dere møttes, men var redd for å si noe)")
        print("(Etter at du og Olivia ikke kom godt overens, var Olivia helt knust. Hun droppet ut av skolen rett før slutten av vg3, og bor i dag i kjelleren til moren, uten å ha oppnådd noe i livet.)")
        print("")
        print("Du fikk ending 2, den dårlige endingen til Olivia. Det er totalt 6 forskjellige endings i spillet.")

class Kat(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, valg2)

    def førsteSpørsmål(self):
        print(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        valg2 = ""
        i=0
        while i==0:
            valg2=input()
            if valg2=="frekk":
                break
            elif valg2 == "vennlig":
                break
            else:
                print("Svaret er ikke gyldig, prøv på nytt.")
                
        if valg2 == "vennlig":
            self.valg2 = True
            print("")
            print(f"{spillerNavn}: Hei! Jeg er ny her og syntest du så snill ut. Jeg heter {spillerNavn}.")
            print(f"Kat: Hei {spillerNavn}. Jeg heter Kat og går esportlinja fordi jeg elsker gaming. Du må ikke tro at jeg er glad i å lese. (Hun peker på boka hun har i hånda). Jeg leser den fordi den er av Lars Larsson, han er favorittforfatteren til Olivia. Kjenner du henne? Hun er ganske trivelig.")
            print("(Dere snakker en stund om interesser dere begge har, helt til Kat må gå fordi hun har et prosjekt hun skal gjøre ferdig. Du leter igjen etter noen å snakke med før timen starter.)")
            print("")
        elif valg2 == "frekk":
            self.valg2 = False
            print("")
            print(f"{spillerNavn}: Hvem er du da? Du ser rar ut.")
            print(f"Kat: Uh hei? Hva er problemet ditt da? Jeg vet ikke engang hvem du er?")
            print(f"{spillerNavn}: Jeg er {spillerNavn}.")
            print("Kat: Åja. Du er den nye eleven fra Malvik.")
            print("(Kat snur seg og går.)")
            print("")
        
    def andreSpørsmål(self):
        print("")
        print("Du møter på Kat på bussholdeplassen på vei hjem.")
        print(f"Kat: Hei {spillerNavn}, tar du også 3-bussen?")
        print(f"{spillerNavn}:Ja det gjør jeg. Deilig å slutte tidlig eller? Jeg gleder meg til å komme hjem og ta en power-nap. ")
        print("Kat: Jeg gleder meg til å komme hjem og spille favorittspillet mitt ")
        print("(Du kommer på at du har hørt henne snakke om det før, men hva het det spillet igjen?)")
        favSpillSvar = input()
        if favSpillSvar == "Minecraft":
            self.valg3 = True
            print("Kat: Ja! Elsker det spillet! ")
        else:
            self.valg3 = False
            print("Kat: Hvilket spill er det? Har aldri hørt om det før. ")

    def sisteSpørsmål(self):
        print("")
        print("Kat: Du, jeg har et spørsmål til deg.")
        print(f"{spillerNavn}: Oi, er det noe viktig?")
        print("Kat: Hva er best, cola eller pepsi?")
        brusValg = input()
        if (brusValg == "Pepsi" or brusValg == "pepsi"):
            self.valg4 = True
            print("Kat: Niceee, helt enig.")
        elif (brusValg == "Monster" or brusValg == "monster"):
            self.valg4 = True
            print("Kat: Det var egentlig ikke et alternativ, men er likevel heelt enig.")
        elif brusValg == "Cola" or brusValg == "cola":
            self.valg4 = False
            print("Kat: Nei æsj hva er galt med deg.")
        else:
            self.valg4 = False
            print("Kat: Hæ hva mener du med det?")

    def braEnding(self):
        print("")
        print("(Etter en uke er du og Kat blitt veldig nære venner. Dere er hjemme hos deg og spiller Minecraft sammen.")
        print("(Kat snur seg mot deg og kysser deg. Du blir overrasket, men kysser hun tilbake.)")
        print("(Ett år senere er dere fortsatt sammen. Kat ble proff esportspiller og har allerede tjent store premiepenger i forskjellige konkurranser.)")
        print("")
        print("Du fikk ending 3, den brae endingen til Kat, gratulerer! Det er totalt 6 forskjellige endings i spillet.")

    def dårligEnding(self):
        print("")
        print("(Du og Kat har gått dårlig overens den første skoledagen på den nye skolen. Dagen etter finner du en lapp i skapet ditt.)")
        print("Lapp: Finn meg bak skolen ved søppeldunken kl 14.00. -Kat")
        print("(Du gjør som lappen sa, og ser Kat stå på det bestemte møtestedet deres.)")
        print("Kat: Hvis det er en ting du bør vite om meg, er det at jeg ikke liker når andre ikke har respekt for meg. Det er flaut å bli sett med deg.")
        print(f"{spillerNavn}: Sier du? Du er jo kjent på skolen for å være en skikkelig raring??")
        print("(Fjeset til Kat blir rødt av sinne. Hun brøler noen banneord du ikke vet hva betyr engang. De virker alvorlige.)")
        print("(Kat vokser og vokser, helt til hun dekker til solen. Hun har blitt om til et monster. Du hyler, men det er for sent. Hun spiser deg hel.)")
        print("")
        print("Du fikk ending 4, den dårlige endingen til Kat. Det er totalt 6 forskjellige endings i spillet.")

class Brian(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, valg2)
    
    def introduksjon(self):
        """Funksjonen introduserer Brian med pronomen han."""
        print(f"{self.navn}, han er {self.alder} år gammel. Han liker {self.liker}, men liker ikke {self.likerIkke}. Han går {self.linje}.")

    def førsteSpørsmål(self):
        print(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        valg2 = ""
        i==0
        while i==0:
            valg2=input()
            if valg2=="frekk":
                break
            elif valg2 == "vennlig":
                break
            else:
                print("Svaret er ikke gyldig, prøv på nytt.")
        if valg2 == "vennlig":
            self.valg2 = True
            print(f"{spillerNavn}: Hei! Jeg er ny her og syntest du så snill ut. Jeg heter {spillerNavn}.")
            print(f"Brian: Hei {spillerNavn} jeg heter Brian. Jeg er 20 år, liker film, og går derfor media")
            print("Du introduserer deg og dere snakker litt om skolen. Du ser deg rundt etter noen å snakke med før timen starter.")
            print("")
        elif valg2 == "frekk":
            self.valg2 = False
            print(f"{spillerNavn}: Halla kæm e du. Koffor går du rundt med så rare klær og den jalla røde kapsen")
            print(f"Brian: Æ hete Brian kæm tror du at du e? Snakke om mine klær mens du går rundt som en jævla uteligger. Lukte dårlig og")
            print("Brian: Du e en jævla nisse komm dæ ut av ansiktet mitt")
            print("(Du går vekk)")
            print("")
            
    def andreSpørsmål(self):
        print("")
        print(f"Du møter Brian i spansktimen. Han lurer litt på hva du liker og ikke liker.")
        print("Brian: Hva synes du om filmer? ")
        filmValg1 = input()
        print("Aaah ok. Har du sett interstellar da? Liker du den? ")
        filmValg2 = input()
        if filmValg2 == "Ja" or filmValg2 == "ja":
            print("Herlig det er favorittfilmen min")
        else:
            print("Ok skjønner")
        print("Brian: Liker du edderkopper da? ")
        
        eddiSvar = input()
        if eddiSvar == "Nei" or eddiSvar == "nei":
            print("Brian: Er helt enig med deg de er helt forferdelige")
            self.valg3 = True
        elif eddiSvar == "Ja" or eddiSvar == "ja":
            print("Brian: Hva faen er galt med deg de er jo så ekle")
            self.valg3 = False
        else:
            print("Brian: Hæ")
            self.valg3 = False
    
    def sisteSpørsmål(self):
        print("")
        print("Brian: Yo kiz æ har et viktig spørsmål te dæ")
        print(f"{spillerNavn}: Ait bet ka e det? ")
        print("Brian: Trump eller Biden")
        presValg = input()
        if presValg == "Trump" or presValg == "trump":
            self.valg4 = True
            print("Brian: Jeg visste visste du ikke var en  ")
        elif presValg == "Biden" or presValg == "bide":
            self.valg4 = False
            print("Brian: Din jævla kommunist faan ")
        else:
            self.valg4 = False
            print(f"Virkelig??")

    def braEnding(self):
        print("")
        print("(Du tenker til deg selv at Brian var en snillere elev enn du trodde.)")
        print("(Brian kommer senere under oppsyn av politiet for drap.)")
        print("(Du tenker. Han var jo så snill det er jo umulig at han kunne gjort noe sånt)")
        print("(Han flytter og kommer aldri tilbake.)")
        print("")
        print("Du fikk ending 5, den brae endingen til Brian, gratulerer! Det er totalt 6 forskjellige endings i spillet.")

    def dårligEnding(self):
        print("")
        print("(Brian virket fortsatt ganske hyggelig etter deres tidligere møte og innviterte deg ut å drikke)")
        print("(Dere drakk ekstremt mye så du klarer ikke komme deg hjem.)")
        print("Brian: Du kan overnatte hos meg jeg har en ekstra sofa og bor rett borti her.")
        print("(Du går inn og ser at hele leiligheten er dekt i plastfolie. Du tenker ikke mye over det og han ber deg ta en plass på sofaen.)")
        print("(Brian går på badet og kommer ut noen minutter senere i full regndrakt og en øks.)")
        print(f"Brian: {spillerNavn} din jævla kommunist du fortjene å dø")
        print("(Han løper mot deg og dreper deg med øksen)")
        print("")
        print("Du fikk ending 6, den dårlige endingen til Brian. Det er totalt 6 forskjellige endings i spillet.")

def gyldigSvar(valg):
    while valg!="Olivia":
        valg=input()
        if valg=="Brian":
            break
        elif valg=="Kat":
            break
        elif valg != "Olivia":
            print("Navnet er ikke gyldig, prøv på nytt.")
    return valg

Olivia = Olivia("Olivia", 18, "å bake", "trening", "studiespesialisering")
Brian = Brian("Brian", 20, "film", "edderkopper", "MK")
Kat = Kat("Kat", 19, "videospill", "skole", "Esport")

list = ["Olivia", "Brian", "Kat"]
listcopy = list


print("")
print("Hei, velkommen til charlottenlund videregående skole. Det er din første dag på denne skolen etter at du flyttet fra gokk(Malvik). Nå er det lunsj, men du fant ingen å spise lunsj med i klassen din. Du ser tre vennlige fjes som du kanskje vil bli kjent med bedre.")
print("Hva heter du?")
spillerNavn = input()
print("")

print("Først har vi ", end="")
Olivia.introduksjon()
print("Så har vi ", end="")
Brian.introduksjon()
print("Til slutt har vi ", end="")
Kat.introduksjon()
print("")


print(f"Hvem vil du snakke med? {list[0]}, {list[1]} eller {list[2]}? ")
valg1 = ""
valg1 = gyldigSvar(valg1)
i=0

if valg1 == "Olivia": 
    Olivia.førsteSpørsmål()
    list.remove("Olivia")
    print(f"Hvem vil du snakke med nå? {list[0]} eller {list[1]}? ")
    nestValg1=""
    while i==0:
        nesteValg1=input()
        if nesteValg1==list[0]:
            break
        elif nesteValg1==list[1]:
            break
        else:
            print("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Brian":
        Brian.førsteSpørsmål()
        list.remove("Brian")
    elif nesteValg1 == "Kat":
        Kat.førsteSpørsmål()
        list.remove("Kat")        

elif valg1 == "Brian": 
    Brian.førsteSpørsmål()
    list.remove("Brian")
    print(f"Hvem vil du snakke med nå? {list[0]} eller {list[1]}? ")
    nesteValg1 = ""
    while i==0:
        nesteValg1=input()
        if nesteValg1==list[1]:
            break
        elif nesteValg1 == list[0]:
            break
        else:
            print("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Olivia":
        Olivia.førsteSpørsmål()
        list.remove("Olivia")
    elif nesteValg1 == "Kat":
        Kat.førsteSpørsmål()        
        list.remove("Kat")

elif valg1 == "Kat": 
    Kat.førsteSpørsmål()
    list.remove("Kat")
    print(f"Hvem vil du snakke med nå? {list[0]} eller {list[1]}? ")
    nesteValg1 = ""
    while nesteValg1!=list[0]:
        nesteValg1=input()
        if nesteValg1==list[1]:
            break
        elif nesteValg1 == list[0]:
            break
        else:
            print("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Brian":
        Brian.førsteSpørsmål()
        list.remove("Brian")
    elif nesteValg1 == "Olivia":
        Olivia.førsteSpørsmål()
        list.remove("Olivia")

if list[0] == "Olivia":
    Olivia.førsteSpørsmål()
elif list[0] == "Brian":
    Brian.førsteSpørsmål()
elif list[0] == "Kat":
    Kat.førsteSpørsmål()

print("")
print("Timen starter, så du har ikke tid til å snakke med flere. I timen sitter du og reflekterer over de tre ny personene du har møtt i lunsjpausen.")
print("")   
print("Du føler deg spesielt tiltrukket til en av dem, og tenker at du vil bli ekstra godt kjent med de. Hvem er det?")
personValg = ""
personValg = gyldigSvar(personValg)

if personValg == "Olivia":
    personValg = Olivia
elif personValg == "Brian":
    personValg = Brian
elif personValg == "Kat":
    personValg = Kat

personValg.andreSpørsmål()

personValg.sisteSpørsmål()

antallpositiv = 0
if personValg.valg2 == True:
    antallpositiv+=1
if personValg.valg3 == True:
    antallpositiv+=1
if personValg.valg4 == True:
    antallpositiv+=1

if (antallpositiv >=2):
    personValg.braEnding()
else:
    personValg.dårligEnding()