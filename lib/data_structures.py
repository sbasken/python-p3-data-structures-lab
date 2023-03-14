import operator

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [dict["name"] for dict in spicy_foods]
    return names


def get_spiciest_foods(spicy_foods):
    new_list = list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            new_list.append(food)
    return new_list


def print_spicy_foods(spicy_foods):
    for dict in spicy_foods:
        peppers = "🌶" * dict["heat_level"]
        name = dict["name"]
        cuisine = dict["cuisine"]
        print(f"{name} ({cuisine}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dict in spicy_foods:
        if dict["cuisine"] == cuisine:
            return dict

def print_spiciest_foods(spicy_foods):
    for dict in spicy_foods:
        if dict["heat_level"] > 5:
            peppers = "🌶" * dict["heat_level"]
            name = dict["name"]
            cuisine = dict["cuisine"]
            print(f"{name} ({cuisine}) | Heat Level: {peppers}")
            

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.append(spicy_food)
    return new_spicy_foods
