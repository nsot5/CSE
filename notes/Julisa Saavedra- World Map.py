world_map = {
    'Cedar Ave & N 11th Street': {
        'NAME': "John's Incredible Pizza ",
        'DESCRIPTION': "This is a place were kids and adult's could go to eat and play with games."
                       " Also, to the South exit there is the parking lot, and to they North exit"
                       "there is a Starbucks Coffee store.",
        'PATHS':{
            'South': "PARKING_LOT"
         }

    },
    'PARKING_LOT':{
        'NAME':"The John's Incredible Pizza Parking Lot ",
        'DESCRIPTION':"There are cars park there."
                      "To the North exit there's"
                      "is a Starbucks Coffee store.",
        'PATHS':{
            "South": "STARBUCKS_COFFEE_STORE"
        }
    },
    'STARBUCKS_COFFEE_STORE': {
        'NAME':"Starbucks Coffee Store",
    }
