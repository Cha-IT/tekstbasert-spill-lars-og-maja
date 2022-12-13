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
        while valg2!="vennlig":
            valg2=input()
            if valg2=="frekk":
                break
            elif valg2 != "vennlig":
                print("Svaret er ikke gyldig, prøv på nytt.")
        if valg2 == "vennlig":
            self.valg2 = True
            print(":)")
        elif valg2 == "frekk":
            self.valg2 = False
            print(":(")
        
    def andreSpørsmål(self):
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
        return

class Kat(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, valg2)

    def førsteSpørsmål(self):
        print(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        valg2 = ""
        while valg2!="vennlig":
            valg2=input()
            if valg2=="frekk":
                break
            elif valg2 != "vennlig":
                print("Svaret er ikke gyldig, prøv på nytt.")
                
        if valg2 == "vennlig":
            self.valg2 = True
            print(f"{spillerNavn}: Hei! Jeg er ny her og syntest du så snill ut. Jeg heter {spillerNavn}.")
            print(f"Kat: Hei {spillerNavn}. Jeg heter Kat og går esportlinja fordi jeg elsker gaming. Du må ikke tro at jeg er glad i å lese. (Hun peker på boka hun har i hånda). Jeg leser den fordi den er av Lars Larsson, han er favorittforfatteren til Olivia. Kjenner du henne? Hun er ganske trivelig.")
            print("")
        elif valg2 == "frekk":
            self.valg2 = False
            print(f"{spillerNavn}: Hvem er du da? Du ser rar ut.")
            print(f"Kat: Uh hei? Hva er problemet ditt da? Jeg vet ikke engang hvem du er?")
            print(f"{spillerNavn}: Jeg er {spillerNavn}.")
            print("Kat: Åja. Du er den nye eleven fra Malvik.")
            print("(Kat snur seg og går.)")
            print("")
        
    def andreSpørsmål(self):
        return

    def sisteSpørsmål(self):
        return

class Brian(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, valg2)
    
    def introduksjon(self):
        """Funksjonen introduserer Brian med pronomen han."""
        print(f"{self.navn}, han er {self.alder} år gammel. Han liker {self.liker}, men liker ikke {self.likerIkke}. Han går {self.linje}.")

    def førsteSpørsmål(self):
        print(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        valg2 = ""
        while valg2!="vennlig":
            valg2=input()
            if valg2=="frekk":
                break
            elif valg2 != "vennlig":
                print("Svaret er ikke gyldig, prøv på nytt.")
        if valg2 == "vennlig":
            self.valg2 = True
            print(":)")
        elif valg2 == "frekk":
            self.valg2 = False
            print(":(")
    def andreSpørsmål(self):
        return
    
    def sisteSpørsmål(self):
        return

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
        elif nesteValg1 != list[0]:
            print("Navnet er ikke gyldig, prøv på nytt.")
    if nesteValg1 == "Olivia":
        Olivia.førsteSpørsmål()
        list.remove("Olivia")
    elif nesteValg1 == "Kat":
        Kat.førsteSpørsmål()        
        list.remove("Kat")

elif i==0: 
    Kat.førsteSpørsmål()
    list.remove("Kat")
    print(f"Hvem vil du snakke med nå? {list[0]} eller {list[1]}? ")
    nesteValg1 = ""
    while nesteValg1!=list[0]:
        nesteValg1=input()
        if nesteValg1==list[1]:
            break
        elif nesteValg1 != list[0]:
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
        
print("Nå har du blitt litt bedre kjent med Olivia, Brian og Kat.")
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
