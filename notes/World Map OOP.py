class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, southwest=None,
                 description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.southwest = southwest
        self.description = description


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Character(object):
    def __init__(self, name,  health, weapon, armor):
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
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


JOHN_INCREDIBLE_PIZZA = Room("John's Incredible Pizza", None, "Parking_lot", None, None, None, None, None,
                             "This is a place were kids and adult's could go to eat and play with games."
                             " Also, to the South exit there is the parking lot, and to the North exit"
                             "there is a Starbucks Coffee store.")

PARKING_LOT = Room("The John's Incredible Pizza Parking Lot", None, None, "STARBUCKS_COFFEE_STORE", None, None, None,
                   None,
                   "There are cars park there."
                   "To the East exit there's"
                   "is a Starbucks Coffee store.")

STARBUCKS_COFFEE_STORE = Room("Starbucks Coffee Store", None, "JOHNS_INCREDIBLE_ARCADE", None, None, None, None, None,
                              "This place is where you could get Coffee"
                              "to drink. Also, at this stores you could"
                              "to there and drink your Coffee and do"
                              "some work or just to hang out there with"
                              "your friends.")

JOHNS_INCREDIBLE_ARCADE = Room("John's Incredible  Arcade", None, None, None, None, "JOHNS_INCREDIBLE_PIZZA_BUFFET",
                               None, None,
                               "This place is a arcade where you could play."
                               "In the arcade there is a laser tag place "
                               "where you get to play with your friends tag "
                               "but you tag the by shooting them with a laser"
                               "gun.")

JOHNS_INCREDIBLE_PIZZA_BUFFET = Room("Johns Incredible Pizza Buffet", None, None, None, None, None,
                                     "JOHNS_INCREDIBLE_BUMPER_CARS", None,
                                     "In John's Incredible Pizza they have a buffet"
                                     "where you could get whatever you want, they"
                                     "also have drink's to drink. Also, you could"
                                     " have party's in there you just have to reserve "
                                     "it.")

JOHNS_INCREDIBLE_BUMPER_CARS = Room("John Incredible Bumper Cars", None, None, None, None, None, None,
                                    "JOHNS_INCREDIBLE_BASKETBALL_GAMES",
                                    "In John's Incredible they have Bumper Cars where"
                                    "you could play with your friends and bump into"
                                    "them with the cars. Also, you could bump into "
                                    "other people and you're have lot's of fun.")

JOHNS_INCREDIBLE_BASKETBALL_GAMES = Room("John's Incredible Basketball Games", None, "JOHNS_INCREDIBLE_BOWLING", None,
                                         None, None, None, None,
                                         "You could play basketball games with your friends.")

JOHNS_INCREDIBLE_BOWLING = Room("John's Incredible Bowling", "BAKERY_DELIGHTS", None, None, None, None, None, None,
                                "In john's incredible they have a bowling place."
                                "In the bowling place you could play with your"
                                "friends, also you could play as how many times"
                                "you wan't to.")

BAKERY_DELIGHTS = Room("Bakery Delights", None, None, None, None, "JOHNS_INCREDIBLE_TWISTER", None, None,
                       "If you want some desert after leaving John's "
                       "Incredible Pizza you could go to Bakery Delights."
                       "At Bakery Delights you could get some bread."
                       )

JOHNS_INCREDIBLE_TWISTER = Room("John's Incredible Twister", None, None, None, None, None,
                                "JOHNS_INCREDIBLE_FROG_HOPPER", None,
                                "In John's Incredible they have a twister were"
                                "you could go on and you spin the wheel so you"
                                "could go really fast")

JOHNS_INCREDIBLE_FROG_HOPPER = Room("The Frog Hopper", None, "JOHNS_INCREDIBLE_CROSSY_ROAD", None, None, None, None,
                                    None,
                                    "In the Frog Hopper you seat on the chair, then"
                                    "you get ready to go up and down. It first goes"
                                    "slow but after that is go really fast till you"
                                    "get dizzy.")

JOHNS_INCREDIBLE_CROSSY_ROAD = Room("John's Incredible Crossy Road", None, None, "JOHNS_INCREDIBLE_PIANO_KEYS", None,
                                    None, None, None,
                                    "In the Crossy Road game you are able to cross the"
                                    "road, train tracks, and rivers without getting kill."
                                    "If they get kill you will have to start all over."
                                    )

JOHNS_INCREDIBLE_PIANO_KEYS = Room("The Piano Keys", None, None, None, "JOHNS_INCREDIBLE_360_TOUR", None, None, None,
                                   "In this game there's is one to two player. You guys"
                                   "are able to play some music til you guys win your onw"
                                   "high scores."
                                   )

JOHNS_INCREDIBLE_360_TOUR = Room("John's Incredible 360 Tour", "JOHNS_INCREDIBLE_AIR_HOCKEY", None, None, None, None,
                                 None, None,
                                 "In the 360 Tour you take a virtual tour of their"
                                 "fun world that John's Incredible Pizza have."
                                 )

JOHNS_INCREDIBLE_AIR_HOCKEY = Room("John's Incredible Air Hockey", None, None, None, None, None, None, None,
                                   "In this game you could play with two person"
                                   "and you guys will have fun.")

# Item
sword = Weapon("Sword", 15)
sword2 = Weapon("Orc Sword", 5)

# Players
player = Player(JOHN_INCREDIBLE_PIZZA)

# Characters
c1 = Character("Orc1", 100, sword, None)
c2 = Character("Orc2", 100, sword2, None)
c1.attack(c2)
c2.attack(c1)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            #  command = 'north'
            room_object = getattr(player.current_location, command)
            room_object = globals()[room_object]
            
            player.move(room_object)
        except KeyError:
            print("This key does not exits")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")
