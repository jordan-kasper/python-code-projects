# This program prints Hello, world!

# variables

water = 100
milk = 50
coffee = 76
money = 0.0

coffee_order = input("What would you like: \n")

if coffee_order == "report":
    print(f'{water}ml \n {milk}ml \n {coffee}g \n $ {money} \n')
elif coffee_order == 'latte':
    if water >= 50 & milk >= 25 & coffee >= 22:
        print("insert $2.50")


print(f'Making your {coffee_order}')