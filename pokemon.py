import type, random, json

class pokemon(type):
    def __init__(self, nom, pv, initiative, lvl, lvlEvolve, evolution, type, attaque, defense):
        self.nom = nom
        self.pv = pv
        self.initiative = initiative
        self.lvl = 1
        self.lvlEvolve = lvlEvolve
        self.evolution = evolution
        type.__init__(self, type, attaque, defense)

    def evol(self):
        with open(pokemon.json) as liste:
            data = json.load(liste)
        evolution = data[self.evolution]
        self.nom = evolution["nom"]
        self.pv = evolution["pv"]
        self.initiative = evolution["initiative"]
        self.lvlEvolve = evolution["lvlEvolve"]
        self.evolution = evolution["evolution"]
        self.attaque = evolution["attaque"]
        self.defense = evolution["defense"]
    
    def gain_lvl(self):
        self.lvl += 1
        self.pv += random.randint(1, 4)
        self.attaque += random.randint(1, 4)
        if self.lvl == self.lvlEvolve:
            self.evol()

    