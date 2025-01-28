class Vault:
    def __init__(self, gold, silver, copper):
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def __str__(self):
        return(f"{self.gold} gold, {self.silver} silver, {self.copper} copper")

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        copper = self.copper + other.copper
        return Vault(gold, silver, copper)

vault = Vault(100, 50, 25)
vault2 = Vault(50, 20, 10)
print(vault + vault2)
