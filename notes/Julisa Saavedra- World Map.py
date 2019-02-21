world_map = {
    'Cedar Ave & N 11th Street': {
        'NAME': "John's Incredible Pizza ",
        'DESCRIPTION': "This is a place were kids and adult's could go to eat and play with games."
                       " Also, to the South exit there is the parking lot, and to they North exit"
                       "there is a Starbucks Coffee store.",
        'PATHS':{
            'SOUTH': "PARKING_LOT"
         }
    },
    'PARKING_LOT':{
        'NAME':"The John's Incredible Pizza Parking Lot ",
        'DESCRIPTION':"There are cars park there."
                      "To the North exit there's"
                      "is a Starbucks Coffee store.",
        'PATHS':{
            "NORTH": "STARBUCKS_COFFEE_STORE"
        }
    },
    'STARBUCKS_COFFEE_STORE': {
        'NAME':"Starbucks Coffee Store ",
        'DESCRIPTION':"This place is where you could get Coffee"
                      "to drink. Also, at this stores you could"
                      "to there and drink your Coffee and do"
                      "some work or just to hang out there with"
                      "your friends.",
        'PATHS':{
            "SOUTH":"JOHNS_INCREDIBLE_PIZZA_ARCADE"
        }
    },
    'JOHNS_INCREDIBLE_PIZZA_ARCADE':{
        'NAME':"John's Incredible Pizza Arcade",
        'DESCRIPTION':"This place is a arcade where you could play."
                      "In the arcade there is a laser tag place "
                      "where you get to play with your friends tag "
                      "but you tag the by shooting them with a laser"
                      " gun.",
        'PATHS':{
            "UP":"JOHNS_INCREDIBLE_PIZZA_BUFFET"
        }
    },
    'JOHNS_INCREDIBLE_PIZZA_BUFFET':{
        'NAME': "Johns Incredible Pizza Buffet",
        'DESCRIPTION':"In John's Incredible Pizza they have a buffet"
                      "where you could get whatever you want, they"
                      "also have drink's to drink. Also, you could"
                      " have party's inthere you just have to reserve "
                      "it.",

},