class Pokemon:
    def __init__(self, nom, type_pokemon, niveau=1, pv=100, attaque=0, defense=0):
        self.__nom = nom
        self.type = type_pokemon
        self.niveau = niveau
        self.pv = pv
        self.attaque = attaque
        self.defense = defense

    def afficher_infos(self):
        print(f"{self.__nom}, niveau {self.niveau}")
        print(f"Type: {self.type}")
        print(f"PV: {self.pv}")
        print(f"Attaque: {self.attaque}")
        print(f"Défense: {self.defense}")
