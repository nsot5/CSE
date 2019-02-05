states = {
    "CA": "California",
    "VA": "Virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"

}
print(states["CA"])
print(states["NV"])

nested_dictionary = {
    "CA": {
        "Name": "California",
        "Population": 39557045  # 39,557,045
    },
    "VA": {
        "Name": "Virginia",
        "Population": 817685  # 8,517,685
    },
    "MD": {
        "Name": "Maryland",
        "Population": 6042718  # 6,042,718
    },
    "RI": {
        "Name": "Rhode Island",
        "Population": 1057315  # 1,057,315
    },
    "NV": {
        "Name": "Nevada",
        "Population": 3034392  # 3,023,392
    }
}

print(nested_dictionary["NV"]["Population"])
print(nested_dictionary["RI"]["Name"])

complex_dictionary = {
    "CA": {
        "Name": "California",
        "Population": 39557045,  # 39,557,045
        "Cities": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "Name": "Virginia",
        "Population": 8517685,  # 8,517,685
        "Cities": [
            "Richmond",
            "Norfolk",
            "Alexandria"
        ]
    },
    "MD": {
        "Name": "Maryland",
        "Population": 6042718, # 6,042,718
        "Cities": [
            "Bethesda",
            "Baltimore",
            "Annapolis"
        ]
    },
    "RI": {
        "Name": "Rhode Island",
        "Population": 1057315,  # 1,057,315
        "Cities": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "Name": "Nevada",
        "Population": 3023392,  # 3,023,392
        "Cities": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}

print(complex_dictionary["RI"]["Cities"][2])


print(complex_dictionary["VA"]["Name"])
print(complex_dictionary["MD"]["Cities"][0])



print(complex_dictionary.keys())
print(nested_dictionary.items())

print()
















