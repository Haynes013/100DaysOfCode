from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}):')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
