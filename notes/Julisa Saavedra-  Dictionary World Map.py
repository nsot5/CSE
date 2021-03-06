world_map = {
    'JOHN_INCREDIBLE_PIZZA': {
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
            'SOUTH': "JOHNS_INCREDIBLE_BOWLING'"
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
                       "and you guys will have fun. To the up"
                       "direction you are all the way to the "
                       "main entrance of John Incredible Pizza",
        'PATHS': {
            'UP'
        }
    },
    'JOHN_INCREDIBLE_ENTRANCE': {
        'NAME': "John's Incredible Entrance",
        'DESCRIPTION': "You are are back at the main entrance of"
                       "John Incredible Pizza",
        'PATHS': {
            "NORTH"
            "WEST"
            "SOUTH"
            "EAST"
            "UP"
            "DOWN"
            "SOUTHWEST"
        }
    },
}

# Other variables
current_node = world_map["Cedar Ave & N 11th Street"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", "SOUTHWEST"]
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'sw']
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")
