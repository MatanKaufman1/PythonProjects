MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}
machine_resources = resources

bank = 0


def ingredients(beverage):
    """ return formated datd, and 'cost' as float """
    ingredients = MENU[beverage]['ingredients']
    return ingredients


def cost(beverage):
    cost = MENU[beverage]['cost']
    return cost


def total_resources(beverage, resources, ingredients):
    """ Return the total resources """

    if beverage == 'espresso':

        resources['water'] = resources['water'] - ingredients['water']
        resources['coffee'] = resources['coffee'] - ingredients['coffee']
        return resources
    else:
        resources['water'] = resources['water'] - ingredients['water']
        resources['milk'] = resources['milk'] - ingredients['milk']
        resources['coffee'] = resources['coffee'] - ingredients['coffee']
        return resources


def availability(beverage, total_resources):
    """ checks if the machine can make the beverage"""
    if beverage == 'espresso':
        if MENU[beverage]['ingredients']['water'] > total_resources['water']:
            return "no enough water."
        elif MENU[beverage]['ingredients']['coffee'] > total_resources['coffee']:
            return " sorry there is no enough coffe"
        else:
            return True
    else:
        if MENU[beverage]['ingredients']['water'] > total_resources['water']:
            return "no enough water."
        elif MENU[beverage]['ingredients']['milk'] > total_resources['milk']:
            return "sorry there is no enough milk"
        elif MENU[beverage]['ingredients']['coffee'] > total_resources['coffee']:
            return " sorry there is no enough coffe"
        else:
            return True


def pyment_check(quarters, dimes, nickles, cost):
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    user_pay = (quarters * quarter) + (dimes * dime) + (nickles * nickle)
    if user_pay < cost:
        return " Sorry, no enough money "
    else:
        payment = user_pay - cost
        return f"This is your change ${round(payment, 2)}"


def coffe_maker(user_choice, machine_resources):

    if availability(user_choice, machine_resources) == True:
        beverage_cost = cost(user_choice)
        print(f"That will cost you: ${beverage_cost}")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How mant dimes?: "))
        nickles = int(input("How many nickles?: "))
        print(pyment_check(quarters, dimes, nickles, beverage_cost))
        print(f"Enjoy your {user_choice}")

    else:
        print(availability(user_choice, machine_resources))


off = False
while not off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    machine_resources = resources

    if user_choice == 'espresso':
        beverage_ingredients = ingredients(user_choice)
        coffe_maker(user_choice, machine_resources)
        beverage_price = cost(user_choice)
        bank = bank + beverage_price
        machine_resources = total_resources(user_choice, resources, beverage_ingredients)

    elif user_choice == 'latte':
        beverage_ingredients = ingredients(user_choice)
        coffe_maker(user_choice, machine_resources)
        machine_resources = total_resources(user_choice, resources, beverage_ingredients)
        beverage_price = cost(user_choice)
        bank = bank + beverage_price

    elif user_choice == 'cappuccino':
        beverage_ingredients = ingredients(user_choice)
        coffe_maker(user_choice, machine_resources)
        machine_resources = total_resources(user_choice, resources, beverage_ingredients)
        beverage_price = cost(user_choice)
        bank = bank + beverage_price

    elif user_choice == 'off':
        off = True
    elif user_choice == 'bank'.lower():
        print(f"${bank}")

    elif user_choice == "report".lower():
        print(machine_resources)
