class Item(object):
    def __init__(self, name, ability):
        self.name = name


class Sword(Item):
    def __init__(self, name, damage, attack,):
        super(Sword, self).__init__(name)
        self.name = name
        self.damage = damage
        self.attack = attack
        self.swords_damage = True


class swords_name(Sword):
    def __init__(self):
        super(swords_name, self).__init__()


class one_handed_sword(Sword):
    def __init__(self):
        super(one_handed_sword, self).__init__(one_handed_sword,)

    def zweihander_sword(self):
        self.swords_damage = -1
        print("You attack the opponent with a zweihander sword.")

    def svardstav_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a svardstav sword.")

    def jian_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a jian sword.")

    def long_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a longsword.")

    def broad_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a broadsword.")

    def long_knife_and_short_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a Long knife and short sword.")

    def claymore_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a claymore sword.")

    def great_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a great sword.")

    def honjo_masamune_sword(self):
        self.swords_damage = -1
        print("You attack your opponent with a  Honjo Masamune sword.")


class Item(object):
    def __init__(self, name, ability):
        self.name = name
        self.ability_type = ability
        self.swords_damage = True
        self.axes_damage = True


class Axes(Item):
    def __init__(self, name, ability_type, damage, attack,):
        super(Axes, self).__init__(name, ability_type)
        self.name = name
        self.damage = damage
        self.attack = attack
        self.axes_damage = True

    def axes_name(self):
        self.axes_damage = -1
        print("You attack your opponent with a axe.")

    def viking_danish_axe(self):
        self.axes_damage = -1
        print("You attack your opponent with a viking danish axe.")

    def the_double_bit_axe(self):
        self.axes_damage = -1
        print("You attack your opponent with the double bit axe.")

    def splitting_maul_axe(self):
        self.axes_damage = -1
        print("You attack your opponent with a splitting maul axe.")

    def felling_hatchet_axe(self):
        self.axes_damage = -1
        print ("You attack your opponent with a felling hatchet axes.")

    def tomahawk_axe(self):
        self.axes_damage = -1
        print("You attack your opponent with a tomahawk axe.")
