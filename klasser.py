udliste = []
udStedlist = []

class UddannelsesSted:
    def __init__(self, navn, placering, facaliteter, uddannelser):
        self.navn = navn
        self.placering = placering
        self.facaliteter = facaliteter
        self.uddannelser = uddannelser  

    def tilføjUddanelse(self, obj):
        self.uddannelser.append(obj)



class Uddannelse:
    def __init__(self, navn, grad, genrelleFag, adgangskravFag, adgangskravNiveau, antalPladser):
        self.__navn = navn #private
        self.grad = grad
        self.genrelleFag = genrelleFag
        self.adgangskravFag = adgangskravFag
        self.adgangskravNiveau = adgangskravNiveau
        self.antalPladser = antalPladser


def opretUddanelsessted(objNavn, navn, placering, facaliteter, uddannelser):
    objNavn = UddannelsesSted(navn, placering, facaliteter, uddannelser)

def opretUddanelse(objNavn, navn, grad, genrelleFag, adgangskravFag, adgangskravNiveau, antalPladser):
    objNavn = Uddannelse(navn, grad, genrelleFag, adgangskravFag, adgangskravNiveau, antalPladser)


ud1 = Uddannelse("Datalog", "bachelor", ["proggramering", "programfilosofi", "matematik"], ["MatA", "ProgB"], 4, 50)
ud2 = Uddannelse("jernforskere", "kandidat", ["geologi", "fysik", "natur-teknik"], ["geografiB", "FysikB", "KemiB"], 6, 25)

udSted1 = UddannelsesSted("AAU", "esbjerg", ["legeplads", "fadølsanlæg", "et toilet"], [ud1])

print(len(udSted1.uddannelser)) #printer 1
udSted1.tilføjUddanelse(ud2)    #tilføjer en uddanelse til listen af uddanelser på et sted.
print(len(udSted1.uddannelser)) #printer 2


