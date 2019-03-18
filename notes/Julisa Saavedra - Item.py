class Item(object):
    def __init__(self, name, ability):
        self.name = name
        self.ability_type = ability


class Sword(Item):
    def __init__(self, name, ability_type, damage, attack,):
        super(Sword, self).__init__(name, ability_type)
        self.name = name
        self.damage = damage
        self.attack = attack
        self.swords_damage = True

    def swords_name(self):
        self.swords_damage = True
        print("You attack the attacker and you sword got damage.")

    def one_handed_sword(self):
        self.ability_type = -1
        
