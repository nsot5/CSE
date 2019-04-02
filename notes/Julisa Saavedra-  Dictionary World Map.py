world_map = {
    'Cedar Ave & N 11th Street': {
        'NAME': "John's Incredible Pizza ",
        'DESCRIPTION': "This is a place were kids and adult's"
                       " could go to eat and play with games."
                       " Also, to the South exit there is the "
                       "parking lot, and to the North exit"
                       "there is a Starbucks Coffee store.",
        'PATHS': {
            'SOUTH': "PARKING_LOT"
         }
    },
    'PARKING_LOT': {
        'NAME': "The John's Incredible Pizza Parking Lot ",
        'DESCRIPTION': "There are cars park there."
                       "To the East exit there's"
                       "is a Starbucks Coffee store.",
        'PATHS': {
            "EAST": "STARBUCKS_COFFEE_STORE"
        }
    },
    'STARBUCKS_COFFEE_STORE': {
        'NAME': "Starbucks Coffee Store ",
        'DESCRIPTION': "This place is where you could get Coffee"
                       "to drink. Also, at this stores you could"
                       "to there and drink your Coffee and do"
                       "some work or just to hang out there with"
                       "your friends.",
        'PATHS': {
            "SOUTH": "JOHNS_INCREDIBLE_ARCADE"
        }
    },
    'JOHNS_INCREDIBLE_ARCADE': {
        'NAME': "John's Incredible  Arcade",
        'DESCRIPTION': "This place is a arcade where you could play."
                       "In the arcade there is a laser tag place "
                       "where you get to play with your friends tag "
                       "but you tag the by shooting them with a laser"
                       " gun.",
        'PATHS': {
            "UP": "JOHNS_INCREDIBLE_PIZZA_BUFFET"
        }
    },
    'JOHNS_INCREDIBLE_PIZZA_BUFFET': {
        'NAME': "Johns Incredible Pizza Buffet",
        'DESCRIPTION': "In John's Incredible Pizza they have a buffet"
                       "where you could get whatever you want, they"
                       "also have drink's to drink. Also, you could"
                       " have party's in there you just have to reserve "
                       "it.",
        'PATHS': {
            'DOWN': "JOHNS_INCREDIBLE_BUMPER_CARS"
        }
    },
    'JOHNS_INCREDIBLE_BUMPER_CARS': {
        'NAME': "John Incredible Bumper Cars",
        'DESCRIPTION': "In John's Incredible they have Bumper Cars where"
                       "you could play with your friends and bump into"
                       "them with the cars. Also, you could bump into "
                       "other people and you're have lot's of fun.",
        'PATHS': {
            'SOUTHWEST': "JOHNS_INCREDIBLE_BASKETBALL_GAMES"
        }
    },
    'JOHNS_INCREDIBLE_BASKETBALL_GAMES': {
        'NAME': "John's Incredible Basketball Games",
        'DESCRIPTION': "You could play basketball games with your friends.",
        'PATHS': {
            'SOUTH': "JOHNS_INCREDIBLE_ BOWLING"
        }
    },
    'JOHNS_INCREDIBLE_BOWLING': {
        'NAME': "John's Incredible Bowling",
        'DESCRIPTION': "In john's incredible they have a bowling place."
                       " In the bowling place you could play with your"
                       "friends, also you could play as how many times"
                       "you wan't to.",
        'PATHS': {
            'NORTH': "BAKERY_DELIGHTS"
        }
    },
    'BAKERY_DELIGHTS': {
        'NAME': "Bakery Delights",
        'DESCRIPTION': "If you want some desert after leaving John's "
                       "Incredible Pizza you could go to Bakery Delights."
                       "At Bakery Delights you could get some bread.",
        'PATHS': {
            'UP': "JOHNS_INCREDIBLE_TWISTER"
        }
    },
    'JOHNS_INCREDIBLE_TWISTER': {
        'NAME': "John's Incredible Twister",
        'DESCRIPTION': "In John's Incredible they have a twister were"
                       "you could go on and you spin the wheel so you"
                       "could go really fast",
        'PATHS': {
            'DOWN': "JOHNS_INCREDIBLE_FROG_HOPPER"
        }
    },
    'JOHNS_INCREDIBLE_FROG_HOPPER': {
        'NAME': "The Frog Hopper",
        'DESCRIPTION': "In the Frog Hopper you seat on the chair, then"
                       "you get ready to go up and down. It first goes"
                       "slow but after that is go really fast till you"
                       "get dizzy.",
        'PATHS': {
            'SOUTH': "JOHNS_INCREDIBLE_CROSSY_ROAD"
        }
    },
    'JOHNS_INCREDIBLE_CROSSY_ROAD': {
        'NAME': "John's Incredible Crossy Road",
        'DESCRIPTION': "In the Crossy Road game you are able to cross the"
                       "road, train tracks, and rivers without getting kill."
                       "If they get kill you will have to start all over.",
        'PATHS': {
            'EAST': "JOHNS_INCREDIBLE_PIANO_KEYS"
        }
    },
    'JOHNS_INCREDIBLE_PIANO_KEYS': {
        'NAME': "The Piano Keys",
        'DESCRIPTION': "In this game there's is one to two player. You guys"
                       "are able to play some music til you guys win your onw"
                       "high scores.",
        'PATHS': {
            'WEST': "JOHNS_INCREDIBLE_360_TOUR"
        }
    },
    'JOHNS_INCREDIBLE_360_TOUR': {
        'NAME': "John's Incredible 360 Tour ",
        'DESCRIPTION': "In the 360 Tour you take a virtual tour of their"
                       "fun world that John's Incredible Pizza have.",
        'PATHS': {
            'NORTH': "JOHNS_INCREDIBLE_AIR_HOCKEY"
        }
    },
    'JOHNS_INCREDIBLE_AIR_HOCKEY': {
        'NAME': "John's Incredible Air Hockey",
        'DESCRIPTION': "In this game you could play with two person"
                       "and you guys will have fun.",
        'PATHS': {
            "NORTH"
            "WEST"
            "SOUTH"
            "EAST"
            "UP"
            "DOWN"
        }
    },
}

# Other variables
current_node = world_map["Cedar Ave & N 11th Street"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("The key does not exits")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")


class Item(object):
    def __init__(self, name, ability_type):
        self.name = name
        self.ability_type = ability_type


class Swords(Item):
    def __init__(self, name, ability_type,  damage, attack):
        super(Swords, self).__init__(name, ability_type)
        self.name = name
        self.damage = damage
        self.attack = attack

    def swords_name(self):
        self.ability_type = -1
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

    def long_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a longsword.")

    def broad_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a broadsword.")

    def long_knife_and_short_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a Long knife and short sword.")

    def claymore_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a claymore sword.")

    def great_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a great sword.")

    def honjo_masamune_sword(self):
        self.ability_type = -1
        print("You attack your opponent with a  Honjo Masamune sword.")


class Axes(Item):
    def __init__(self, name, ability_type,  damage, attack):
        super(Axes, self).__init__(name, ability_type)
        self.name = name
        self.damage = damage
        self.attack = attack

    def axes_name(self):
        self.ability_type = -1
        print("You attack your opponent with a axe.")

    def viking_danish_axe(self):
        self.ability_type = -1
        print("You attack your opponent with a viking danish axe.")

    def the_double_bit_axe(self):
        self.ability_type = -1
        print("You attack your opponent with the double bit axe.")

    def splitting_maul_axe(self):
        self.ability_type = -1
        print("You attack your opponent with a splitting maul axe.")

    def felling_hatchet_axe(self):
        self.ability_type = -1
        print ("You attack your opponent with a felling hatchet axes.")

    def tomahawk_axe(self):
        self.ability_type = -1
        print("You attack your opponent with a tomahawk axe.")


class Room(object):
    def __init__(self, name, item):
        self.room_name = name
        self.name = name
        self.items = item


sword = Swords("one_handed_sword", "zweihander_sword", "svardstav_sword", "jian_sword", "long_sword", "broad_sword",
               "long_knife_and_short_sword", "claymore_sword", "great_sword", "honjo_masamune_sword")

axe = Axes("viking_danish_axe", "the_double_bit_axe", "splitting_maul_axe", "felling_hatchet_axe", "tomahawk_axe")

room1 = Room("John's Incredible Pizza", "one_handed_sword")
room2 = Room("The John's Incredible Pizza Parking Lot", "zweihander_sword")
room3 = Room("Starbucks Coffee Store", "svardstav_sword")
room4 = Room("John's Incredible  Arcade", "jian_sword")
room5 = Room("Johns Incredible Pizza Buffet", "long_sword")
room6 = Room("John Incredible Bumper Cars", "broad_sword")
room7 = Room("John's Incredible Basketball Games", "long_knife_and_short_sword")
room8 = Room("John's Incredible Bowling", "claymore_sword")
room9 = Room("Bakery Delights", "great_sword")
room10 = Room("John's Incredible Twister", "honjo_masamune_sword")
room11 = Room("The Frog Hopper", "viking_danish_axe")
room12 = Room("John's Incredible Crossy Road", "the_double_bit_axe")
room13 = Room("The Piano Keys", "splitting_maul_axe")
room14 = Room("John's Incredible 360 Tour", "felling_hatchet_axe")
room15 = Room("John's Incredible Air Hockey", "tomahawk_axe")


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))