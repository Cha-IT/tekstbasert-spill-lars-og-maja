class Person():
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0) -> None:
        self.navn = navn
        self.alder = alder
        self.liker = liker
        self.likerIkke = likerIkke
        self.linje = linje
        self.valg2 = valg2
    
    def introduksjon(self):
        print(f"{self.navn}, hun er {self.alder} år gammel. Hun liker {self.liker}, men liker ikke {self.likerIkke}. Hun går {self.linje}.")
    
    def førsteSpørsmål(self):
        print(f"Du går bort til {self.navn} og introduserer deg selv. Vil du være vennlig eller frekk?")
        valg2 = ""
        while valg2!="Vennlig":
            valg2=input()
            if valg2=="Frekk":
                break
            else:
                print("Svaret er ikke gyldig, prøv på nytt.")
        if self.navn == "Olivia":
            if valg2 == "Vennlig":
                print("")
            elif valg2 == "Frekk":
                print("")
        elif self.navn == "Brian":
            if valg2 == "Vennlig":
                print("")
            elif valg2 == "Frekk":
                print("")
        elif self.navn == "Kat":
            if valg2 == "Vennlig":
                print("")
            elif valg2 == "Frekk":
                print("")

class Mann(Person):
    def __init__(self, navn, alder, liker, likerIkke, linje, valg2=0) -> None:
        super().__init__(navn, alder, liker, likerIkke, linje, valg2)
    
    def introduksjon(self):
        print(f"{self.navn}, han er {self.alder} år gammel. Han liker {self.liker}, men liker ikke {self.likerIkke}. Han går {self.linje}.")

Olivia = Person("Olivia", 18, "å bake", "trening", "studiespesialisering")
Brian = Mann("Brian", 20, "film", "edderkopper", "MK")
Kat = Person("Kat", 19, "videospill", "skole", "Esport")

spørsmål = {
    "Hvem vil du snakke med?" : ["Olivia", "Brian", "Kat"]
}

print("")
print("Hei, velkommen til charlottenlund videregående skole. Det er din første dag på denne skolen etter at du flyttet fra gokk(Malvik). Nå er det lunsj, men du fant ingen å spise lunsj med i klassen din. Du ser tre vennlige fjes som du kanskje vil bli kjent med bedre.")
print("")

print("Først har vi ", end="")
Olivia.introduksjon()
print("Så har vi ", end="")
Brian.introduksjon()
print("Til slutt har vi ", end="")
Kat.introduksjon()
print("")

print(f"Hvem vil du snakke med? {spørsmål['Hvem vil du snakke med?'][0]}, {spørsmål['Hvem vil du snakke med?'][1]} eller {spørsmål['Hvem vil du snakke med?'][2]}? ")
valg1 = ""

while valg1!="Olivia":
    valg1=input()
    if valg1=="Brian":
        break
    elif valg1=="Kat":
        break
    else:
        print("Navnet er ikke gyldig, prøv på nytt.")

if valg1 == "Olivia": 
    Olivia.førsteSpørsmål()
elif valg1 == "Brian": 
    Brian.førsteSpørsmål()
elif valg1 == "Kat": 
    Kat.førsteSpørsmål()