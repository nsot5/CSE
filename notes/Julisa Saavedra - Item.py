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


class honjo_masamune_sword(Sword):
    def __init__(self):
        super(honjo_masamune_sword, self).__init__("honjo masamune sword")


class Item(object):
    def __init__(self, name):
        self.name = name


class Axes(Item):
    def __init__(self, name):
        super(Axes, self).__init__(name)
        self.name = name
        self.axe_damage = True


class axes_name(Axes):
    def __init__(self):
        super(axes_name, self).__init__("axes name")


class viking_danish_axe(Axes):
    def __init__(self):
        super(viking_danish_axe, self).__init__("viking danish axe")


class the_double_bit_axe(Axes):
    def __init__(self):
        super(the_double_bit_axe, self).__init__("the double bit axe")


class splitting_maul_axe(Axes):
    def __init__(self):
        super(splitting_maul_axe, self).__init__("spitting maul axe")


class felling_hatchet_axe(Axes):
    def __init__(self):
        super(felling_hatchet_axe, self).__init__("felling hatchet axe")


class tomahawk_axe(Axes):
    def __init__(self):
        super(tomahawk_axe, self).__init__("tomahawk axe")