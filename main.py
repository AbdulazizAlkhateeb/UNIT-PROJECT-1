from art import text2art
from colorama import Fore, Style
from classes.drinks import Drink
from classes.recipe import Recipe
from classes.beans import Beans
from utils.file_handler import load_json, save_json

DRINKS_FILE = "./data/drinks.json"
BEANS_FILE = "./data/beans.json"

drinks = [Drink.from_dict(d) for d in load_json(DRINKS_FILE)]
beans = [Beans.from_dict(b) for b in load_json(BEANS_FILE)]






def add_bean_or_drink():
    print(Fore.GREEN + "\nAdd Bean or Drink?" + Style.RESET_ALL)
    choice = input("[1] Bean  [2] Drink: ")

    if choice == "1":
        name = input("Bean name: ")
        region = input("Region: ")
        notes = input("Notes (comma separated): ").split(",")
        roast = input("Roast level (light/medium/dark): ")
        price = float(input("Price per kg: "))
        beans.append(Beans(name, region, notes, roast, price))
        print(Fore.GREEN + "Bean added.\n" + Style.RESET_ALL)

    elif choice == "2":
        name = input("Drink name: ")
        price = float(input("Price: "))

        for index, bean in enumerate(beans):
            print(f"-{index+1} {bean.get_name()} ({bean.get_region()})")
        bean_index = int(input("Select bean: "))
        bean = beans[bean_index-1]

        grind = int(input("Grind coffe needed for 1 Drink in g: "))
        milk = int(input("Milk in ml, if none enter 0: "))
        ratio = input("Ratio (e.g., 1:2.5): ")
        size = int(input("Grind size (1-30) \"1\" is fine \"30\" is coarse: "))
        steps = []
        print("Enter steps. Type 'done' to finish:")
        while True:
            step = input("Step: ")
            if step.lower() == 'done': break
            steps.append(step)

        recipe = Recipe(bean, grind, milk, ratio, size, steps)
        drinks.append(Drink(name, price, recipe, []))
        print(Fore.GREEN + "Drink added.\n" + Style.RESET_ALL)







def make_drink():
    for drink in drinks:
        print(Fore.CYAN + drink.get_name() + Style.RESET_ALL)
    name = input("Enter drink name: ")
    match = [drink for drink in drinks if name.lower() in drink.get_name().lower()]
    if not match:
        print(Fore.RED + "Drink not found.\n" + Style.RESET_ALL)
        return

    drink = match[0]
    recipe = drink.get_recipe()
    bean = recipe.get_bean()
    grind_needed = recipe.get_grind_coffee_grams()

    # Check coffee availability
    if bean.get_stock_grams() < grind_needed:
        print(Fore.RED + f"Not enough beans available for {bean.get_name()}.\n" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"\nRequired ingredients for: {drink.get_name()}")
    print(Fore.CYAN + f"- Coffee grams: {recipe.get_grind_coffee_grams()}g")
    print(f"- Water needed: {recipe.get_water_needed()}ml")
    if not recipe.get_milk_ml() ==0 :
        print(f"- Milk amount: {recipe.get_milk_ml()}ml")
    print(f"- Grind size: {recipe.get_grind_size()}")
    print(f"- Bean: {recipe.get_bean().get_name()} ")


    print(Fore.YELLOW + "\nFollow the steps below. Press Enter to continue after each step:" + Style.RESET_ALL)
    for index, step in enumerate(recipe.get_steps(), 1):
        print(Fore.BLUE + f"Step {index}: {step}" + Style.RESET_ALL)
        input(Fore.RED + ">> Press Enter to continue...\n" + Style.RESET_ALL)

    bean.use_beans(grind_needed)


    user_choice = input("Would you like to add a rating? (y/n): ")
    if user_choice.lower() == "y":
        rate_drink(drink)




def rate_drink(drink: Drink):
    score = int(input("Score (1-5): "))
    desc = input("Description: ")
    drink.add_rating(score, desc)
    print(Fore.GREEN + "Rating added.\n" + Style.RESET_ALL)




def show_all_drinks():
    if not drinks:
        print(Fore.RED + "No drinks available.\n" + Style.RESET_ALL)
        return
    for index, drink in enumerate(drinks, 1):
        print(Fore.BLUE + f"[{index}] {drink.get_drink_info()}" + Style.RESET_ALL)

    input(Fore.RED + ">> Press Enter to continue...\n" + Style.RESET_ALL)





def delete_drink():
    show_all_drinks()
    name = input("Enter drink name to delete: ")
    match = [drink for drink in drinks if name.lower() in drink.get_name().lower()]
    if not match:
        print(Fore.RED + "Drink not found.\n" + Style.RESET_ALL)
        return
    drinks.remove(match[0])
    print(Fore.GREEN + "Drink deleted.\n" + Style.RESET_ALL)


def show_all_beans():
    if not beans:
        print(Fore.RED + "No beans available.\n" + Style.RESET_ALL)
        return
    for index, b in enumerate(beans, 1):
        print(Fore.CYAN + f"[{index}] {b.get_bean_info()}" + Style.RESET_ALL)
    input(Fore.RED + ">> Press Enter to continue...\n" + Style.RESET_ALL)

def show_all_ratings():
    if not drinks:
        print(Fore.RED + "No drinks available.\n" + Style.RESET_ALL)
        return

    for drink in drinks:
        print(Fore.YELLOW + f"\n{drink.get_name()}:" + Style.RESET_ALL)

        ratings = drink.get_ratings()
        if not ratings:
            print(Fore.RED + "  No ratings yet." + Style.RESET_ALL)
            continue

        for i, rate in enumerate(ratings, 1):
            print(Fore.CYAN + f"  -{i} {rate.get_rating_info()}" + Style.RESET_ALL)

    input(Fore.RED + "\n>> Press Enter to continue..." + Style.RESET_ALL)




def save_all():
    save_json(DRINKS_FILE, [drink.to_dict() for drink in drinks])
    save_json(BEANS_FILE, [bean.to_dict() for bean in beans])




def main():
    print(Fore.MAGENTA + text2art("Coffee System") + Style.RESET_ALL)
    while True:
        print(Fore.YELLOW + '''
Main Menu:
1. Add Bean or Drink
2. Make a Drink
3. Show All Drinks
4. Show All Beans
5. Show All Ratings
6. Delete a Drink
7. Exit
''' + Style.RESET_ALL)


        choice = input("Select option: ")

        if choice == "1":
            add_bean_or_drink()
        elif choice == "2":
            make_drink()
        elif choice == "3":
            show_all_drinks()
        elif choice == "4":
            show_all_beans()
        elif choice == "5":
            show_all_ratings()
        elif choice == "6":
            delete_drink()
        elif choice == "7":

            save_all()
            print(Fore.GREEN + "Data saved. Goodbye." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option.\n" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
