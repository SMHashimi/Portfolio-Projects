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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

prompt_user = input("What would you like? (espresso/latte/cappuccino): ").lower()

def remaining_resources(type):
    if type == "espresso":
        water = resources['water'] - MENU[type]["ingredients"]["water"]
        coffee = resources["coffee"] - MENU[type]["ingredients"]["coffee"]
        cost = MENU[type]["cost"]
        return f"Water: {water}ml\nCoffee: {coffee}g\nMoney: {money + cost}"
    elif type == "cappuccino":
        water = resources['water'] - MENU[type]["ingredients"]["water"]
        milk = resources["milk"] - MENU[type]["ingredients"]["milk"]
        coffee = resources["coffee"] - MENU[type]["ingredients"]["coffee"]
        cost = MENU[type]["cost"]
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money + cost}"
    elif type == "latte":
        water = resources["water"] - MENU[type]["ingredients"]["water"]
        milk = resources["milk"] - MENU[type]["ingredients"]["milk"]
        coffee = resources["coffee"] - MENU[type]["ingredients"]["coffee"]
        cost = MENU[type]["cost"]
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money + cost}"
# remaining_resources(type=prompt_user)

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01

def report(reports):
    if reports == "Report".lower():
        return f'Water:  {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}'

def coins():
    quarters = int(input(f"How many quarter?: "))
    quarters_amount = quarters * quarter_value
    dimes = int(input(f"How many dime?: "))
    dimes_amount = dimes * dime_value
    nickels = int(input(f"How many nickel?: "))
    nickles_amount = nickels * nickel_value
    pennies = int(input(f"How many penny?: "))
    pennies_amount = pennies * penny_value
    return quarters_amount + dimes_amount + nickles_amount + pennies_amount
# coins_added = coins()

def coffee_machine():
    print(report(reports = prompt_user))
    if prompt_user == "latte":
        coints_total = coins()

coffee_machine()