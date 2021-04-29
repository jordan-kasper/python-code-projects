# This program prints Hello, world!

# variables

water = 100
milk = 50
coffee = 76
money = 0.0
is_on = True


def coffee_report():
    print(f'{water}ml \n {milk}ml \n {coffee}g \n $ {money} \n')


def refill_machine():
    global water
    global milk
    global coffee
    water = 100
    milk = 50
    coffee = 76

    coffee_report()


def latte_order():
    global water
    global milk
    global coffee

    if water >= 50 and milk >= 25 and coffee >= 22:
        print(f'Making your {coffee_order}')
        print("Here is your Latte, have a nice day!")
        water -= 50
        milk -= 25
        coffee -= 23
        coffee_report()


def mocha_order():
    if water >= 50 and milk >= 25 and coffee >= 22:
        print(f'Making your {coffee_order}')
        print("Here is your mocha, have a nice day!")


while is_on:

    coffee_order = input("What would you like: \n")

    if coffee_order == "report":
        coffee_report()
    elif coffee_order == 'latte':
        latte_order()
    elif coffee_order == 'mocha':
        mocha_order()
    elif coffee_order == 'refill':
        refill_machine()
