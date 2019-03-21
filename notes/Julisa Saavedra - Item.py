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
        print("You attack the opponent and you sword got damage.")

    def one_handed_sword(self):
        self.ability_type = -1
        print ("You attack the opponent with a one handed sword.")

    def zweihander_sword(self):
        self.ability_type = -1
        print("You attack the opponent with a zweihander sword.")

    def svardstav_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a svardstav sword.")

    def jian_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a jian sword.")

    def longsword_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a longsword.")

    def broadsword_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a broadsword.")

    def long_knife_and_short_sword(self):
        self.ability_type= -1
        print("You attack your opponent with a Long knife and short sword.")

    def claymore_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a claymore sword.")

    def great_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a great sword.")


class Item(object):
    def __init__(self, name, ability):
        self.name = name
        self.ability_type = ability


class Axes(Item):
    def __init__(self, name, ability_type, damage, attack,):
        super(Axes, self).__init__(name, ability_type)
        self.name = name
        self.damage = damage
        self.attack = attack

    def
