class type:
    def __init__(self, type, attaque, defense):
        self.type = type
        self.attaque = attaque
        self.defense = defense

    def comparaison(self, opposant):
        if self.type == "normal":
            if opposant.type == "normal":
                return 1
            else:
                return 0.75
        elif self.type == "eau":
            if opposant.type == "feu":
                return 2
            elif opposant.type == "terre":
                return 0.5
            else:
                return 1
        elif self.type == "feu":
            if opposant.type == "terre":
                return 2
            elif opposant.type == "eau":
                return 0.5
            else:
                return 1
        elif self.type == "terre":
            if opposant.type == "eau":
                return 2
            elif opposant.type == "feu":
                return 0.5
            else:
                return 1