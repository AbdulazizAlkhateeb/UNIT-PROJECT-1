# # from art import text2art
# # from colorama import Fore, Back, Style
# # from classes.drinks import Drink
# # import json
# # import os
# #
# #
# # drinks = dict()
# #
# #
# # try:
# #     if not os.path.exists("data/drinks.json"):
# #         with open("data/users.json", 'w', encoding="UTF-8") as file:
# #             file.write("[]")
# #
# #     else:
# #         with open('data/drinks.json', 'r', encoding="UTF-8") as file:
# #             content = file.read()
# #             users = json.loads(content) #Decode
# # except Exception as e:
# #     print(e)
# #
# #
# #
# #
# #
# #
# # def get_user_beans(user_name = None):
# #     while True:
# #         beans_name= input("Entr beans name")
# #
# #
# #     pass
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #     # while True:
# #     #     user_type = input(Fore.BLUE + "Are you a new user? (y/n): ").strip().lower()
# #     #     if user_type in ["y", "n"]:
# #     #         break
# #     #     print(Fore.RED + "Invalid input. Please type 'y' or 'n'.")
# #
# #     # name = input(Fore.BLUE + "Enter your name: ").strip()
# #
# #     # if user_type == "y":
# #     #     machine = input(Fore.BLUE + "Enter your coffee machine (e.g., V60, Espresso): ").strip()
# #     #     beans = input(Fore.BLUE + "Enter bean type (e.g., light, medium, dark roast): ").strip()
# #     #     # TODO: Save user data
# #     #     print(Fore.GREEN + f"\nWelcome, {name}! Your profile has been created." + Style.RESET_ALL)
# #     #     return {"name": name, "machine": machine, "beans": beans}
# #     # else:
# #     #     # TODO: Load user data (for now, simulate)
# #     #     print(Fore.GREEN + f"\nWelcome back, {name}!" + Style.RESET_ALL)
# #     #     return {"name": name, "machine": "V60", "beans": "medium"}
# #
# #
# #
# #
# # # def main_menu(user):
# # #     print(Fore.YELLOW + "\nChoose an option:")
# # #     print("1. Start brewing")
# # #     print("2. View history")
# # #     print("3. Exit" + Style.RESET_ALL)
# #
# # #     return input(Fore.BLUE + "\nEnter your choice (1-3): " + Style.RESET_ALL).strip()
# #
# #
# #
# #
# #
# #
# #
# #
# #     print(Fore.CYAN + text2art("Barista Assistant", font="small") + Style.RESET_ALL)
# #     print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)
# #     print(Fore.CYAN + "Welcome to your Barista Assistant!" + Style.RESET_ALL)
# #     print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)
# #
# #     user = get_user_profile()
# #
# #     while True:
# #
# #         print(Fore.YELLOW + "\nChoose an option:")
# #         print("1. Start brewing")
# #         print("2. View history")
# #         print("3. Exit" + Style.RESET_ALL)
# #
# #         choice = input(Fore.BLUE + "\nEnter your choice (1-3): " + Style.RESET_ALL).strip()
# #
# #
# #
# #         if choice == "1":
# #             print(Fore.GREEN + f"\nStarting brew for {user['machine']} using {user['beans']} beans..." + Style.RESET_ALL)
# #             # TODO: Brew logic
# #         elif choice == "2":
# #             print(Fore.GREEN + "\nFetching brew history..." + Style.RESET_ALL)
# #             # TODO: History logic
# #         elif choice == "3":
# #             print(Fore.RED + "\nGoodbye!" + Style.RESET_ALL)
# #             break
# #         else:
# #             print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)
# #
# #         input(Fore.MAGENTA + "\nPress Enter to continue..." + Style.RESET_ALL)
# #         print("\n" + "-" * 40)
# #
# # if __name__ == "__main__":
# #     main()
# #
#
#
#
# from art import text2art
# from colorama import Fore, Back, Style
# from classes.drinks import Drink
# from classes.recipe import Recipe
# from classes.rating import Rating
# from classes.beans import Beans
# import json
# import os
#
#
#
# # if __name__ == '__main__':
# #
# #     listOfDrink = []
# #     bean = Beans('arabic', 'Saudi Arabia', ['bitter', 'soar'], 'dark', 100)
# #     recipe = Recipe(bean, 18, 0, '1:15', 15, ['step 1', 'step 2', 'step 3'])
# #     drink = Drink('black coffie', 10.0,  recipe, [])
# #     listOfDrink.append(drink)
# #
# #     for i in listOfDrink:
# #         print(i)
# #
# #     print("hello")
#
#
#
#
# if __name__ == '__main__':
#     with open('./data/drinks.json', 'r', encoding='utf-8') as file:
#         raw_data = json.load(file)
#     # print(data)
#     drinks = [Drink.from_dict(entry) for entry in raw_data]
#
#     # for drink in drinks:
#     #     print(drink.get_name())
#     # inputuser = input("Enter drink name: ")
#     # chosenDrinkList = [d for d in drinks if inputuser in d.get_name()]
#     # chosenDrink = chosenDrinkList.pop(0)
#     # print(f"Please follow the steps: ")
#     # for get_step in chosenDrink.get_recipe().get_steps():
#     #     print(get_step)
#     #
#
#
#
#     data = [drink.to_dict() for drink in drinks]
#     with open("./data/outputDrink.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2)
#
