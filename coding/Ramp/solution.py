localJson = """[
    {
        "id": "1",
        "agent": "Radulf Katlego",
        "unit": "#3",
        "description": "This luxurious studio apartment is in the heart of downtown.",
        "num_bedrooms": 1
    },
    {
        "id": "2",
        "agent": "Kelemen Konrad",
        "unit": "#36",
        "description": "We have a 1-bedroom available on the third floor.",
        "num_bedrooms": 1
    },
    {
        "id": "3",
        "agent": "Ton Jett",
        "unit": "#12",
        "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
        "num_bedrooms": 1
    },
    {
        "id": "4",
        "agent": "Fishel Salman",
        "unit": "#13",
        "description": "Beautiful studio with a nearby art studio.",
        "num_bedrooms": 1
    }
]"""


test2_json="""[
    {
        "id": "1",
        "agent": "John Smith",
        "unit": "#39",
        "description": "[The apartment] is in the heart of downtown!!!",
        "num_bedrooms": 0
    }
]"""


test3_json="""[
    {
        "id": "0",
        "agent": "Katie Mill",
        "unit": "#267",
        "description": "studio has pink walls and it is perfect for a small family!",
        "num_bedrooms": 0
    },
    {
        "id": "1",
        "agent": "Kate Woods",
        "unit": "#207",
        "description": "small art is not that far from the apartment!",
        "num_bedrooms": 1
    }
]
"""

test4_json = """[
    {
        "id": "2",
        "agent": "Kelemen Konrad",
        "unit": "#36",
        "description": "We have art 1-bedroom available on the third floor.",
        "num_bedrooms": 0
    }
]"""


test5_json = """[
    {
        "id": "0",
        "agent": "Derek Jordan",
        "unit": "#931",
        "description": "ornate, ornate and gorgeous studio in the heart of midtown!",
        "num_bedrooms": 1
    },
    {
        "id": "1",
        "agent": "John Smith",
        "unit": "#184",
        "description": "This small studio is located on the second of a nice building in midtown!",
        "num_bedrooms": 1
    },
    {
        "id": "2",
        "agent": "Paul Martinez",
        "unit": "#596",
        "description": "cheap art is close by the 1-bedroom!",
        "num_bedrooms": 1
    },
    {
        "id": "3",
        "agent": "Nicholas North",
        "unit": "#544",
        "description": "studio has big fridge and it is perfect for a man.",
        "num_bedrooms": 1
    },
    {
        "id": "4",
        "agent": "Fred Shawler",
        "unit": "#917",
        "description": "comfortable, small and renovated apartment in the heart of midtown!",
        "num_bedrooms": 0
    },
    {
        "id": "5",
        "agent": "Evan Williams",
        "unit": "#348",
        "description": "What a good deal for this ornate and cheap studio!",
        "num_bedrooms": 1
    },
    {
        "id": "6",
        "agent": "Evan Williams",
        "unit": "#467",
        "description": "The studio is 15 min walking distance to yoga studio.",
        "num_bedrooms": 1
    }
]"""

import re
import json

def solution(jsonData):
    data = json.loads(jsonData)
    return [extract_bedrooms(i['description'], i['num_bedrooms']) for i in data]

def is_studio(description):
    description = re.sub(r'[.!?]', '', description)
    description = description.lower().split()
    studios = [i for i, el in enumerate(description) if el == 'studio']
    for studio in studios:
        if studio > 0:
            if not description[studio - 1] in ['yoga', 'art', 'dance']:
               return True
        else:
            return True
    return False

def is_bedroom(description):
    description = re.sub(r'[.!?]', '', description)
    description = description.lower().split()
    bedrooms = [i for i, el in enumerate(description) if el == '1-bedroom']
    for bedroom in bedrooms:
        if bedroom > 0:
            if not description[bedroom - 1] in ['yoga', 'art', 'dance']:
               return True
        else:
            return True
    return False

def extract_bedrooms(description, original):
    if not "studio" in description and not "1-bedroom" in description:
        return original
    if is_studio(description):
        return 0
    if is_bedroom(description):
        return 1
    return original


assert solution(localJson) == [0, 1, 1, 0]
assert solution(test2_json) == [0]
assert solution(test3_json) == [0, 1]
assert solution(test4_json) == [0]
assert solution(test5_json) == [0, 0, 1, 0, 0, 0, 0]
