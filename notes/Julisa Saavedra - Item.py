class Item(object):
    def __init__(self, name):
        self.name = name


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.name = name
        self.swords_damage = True


class swords_name(Sword):
    def __init__(self):
        super(swords_name, self).__init__("swords name")


class one_handed_sword(Sword):
    def __init__(self):
        super(one_handed_sword, self).__init__("one handed sword")


class zweihander_sword(Sword):
    def __init__(self):
        super(zweihander_sword, self).__init__("zweihander sword")


class svardstav_sword(Sword):
    def __init__(self):
        super(svardstav_sword, self).__init__("svardstav sword")


class jian_sword(Sword):
    def __init__(self):
        super(jian_sword, self).__init__("jian sword")


class long_sword(Sword):
    def __init__(self):
        super(long_sword, self).__init__("long sword")


class broad_sword(Sword):
    def __init__(self):
        super(broad_sword, self).__init__("board sword")


class long_knife_and_short_sword(Sword):
    def __init__(self):
        super(long_knife_and_short_sword, self).__init__("long knife and short sword")


class claymore_sword(Sword):
    def __init__(self):
        super(claymore_sword, self).__init__("claymore sword")


class great_sword(Sword):
    def __init__(self):
        super(great_sword, self).__init__("great sword")


class honjo_masamune_sword(self):
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
