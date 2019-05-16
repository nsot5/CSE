class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west= None, up=None, down=None, southwest=None, description=""):
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


CEDAR_AVE_& N_11_TH_STREET = Room("John's Incredible Pizza", None, "Parking_lot", None, None, None, None, None,
                                  "This is a place were kids and adult's could go to eat and play with games."
                                  " Also, to the South exit there is the parking lot, and to the North exit"
                                  "there is a Starbucks Coffee store.")

PARKING_LOT = Room("The John's Incredible Pizza Parking Lot", None, None, "STARBUCKS_COFFEE_STORE", None, None, None, None,
                   "There are cars park there."
                   "To the East exit there's"
                   "is a Starbucks Coffee store.")

STARBUCKS_COFFEE_STORE = Room("Starbucks Coffee Store",None, "JOHNS_INCREDIBLE_ARCADE", None, None, None, None, None,
                              "This place is where you could get Coffee"
                              "to drink. Also, at this stores you could"
                              "to there and drink your Coffee and do"
                              "some work or just to hang out there with"
                              "your friends.")

JOHNS_INCREDIBLE_ARCADE = Room("John's Incredible  Arcade", None, None, None, None, "JOHNS_INCREDIBLE_PIZZA_BUFFET", None, None,
                               "This place is a arcade where you could play."
                               "In the arcade there is a laser tag place "
                               "where you get to play with your friends tag "
                               "but you tag the by shooting them with a laser"
                               "gun.")

JOHNS_INCREDIBLE_PIZZA_BUFFET = Room("Johns Incredible Pizza Buffet", None, None, None, None, None, "JOHNS_INCREDIBLE_BUMPER_CARS", None,  "In John's Incredible Pizza they have a buffet"
                       "where you could get whatever you want, they"
                       "also have drink's to drink. Also, you could"
                       " have party's in there you just have to reserve "
                       "it.")

JOHNS_INCREDIBLE_BUMPER_CARS = Room("John Incredible Bumper Cars", None, None, None, None, None, None, "JOHNS_INCREDIBLE_BASKETBALL_GAMES", "In John's Incredible they have Bumper Cars where"
                       "you could play with your friends and bump into"
                       "them with the cars. Also, you could bump into "
                       "other people and you're have lot's of fun.")


#  Put them in quotes
R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking Lot', None, "R19A")

# Item
sword = Weapon("Sword", 15)
sword2 = Weapon("Orc Sword", 5)

# Players
player = Player(R19A)

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
