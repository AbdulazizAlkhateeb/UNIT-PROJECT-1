from art import text2art
from colorama import Fore, Style
from classes.users import User
import json
import os


users:list = []
machine_list:list= []


try:
    if not os.path.exists("data/users.json"):
        with open("data/users.json", 'w', encoding="UTF-8") as file:
            file.write("[]") 

    else:
        with open('data/users.json', 'r', encoding="UTF-8") as file:
            content = file.read()
            users = json.loads(content) #Decode
except Exception as e:
    print(e)






def get_user_beans(user_name = None):
    while True:
        beans_name= input("Entr beans name")


    pass





def get_user_profile():
    while True:
        user_type = input("Are you a new user? Enter \"y\" for Yes,or  \"n\" for No")
        if user_type == "y":
            name= input("Enter you name: ")


            while True:
                machine= input("Enter your coffee machine (e.g., V60, Espresso) or \"exite\" to exite : ")
                if machine == "exite":
                    break
                else:machine_list.append(machine)

            beans_list=get_user_beans()

            new_ueser= User(name, machine_list, beans_list)
            users.append(new_ueser)



        elif user_type == "n":
            user_name= input("Enter your name: ")


        else: print(Fore.RED + "Invalid input. Please type 'y' or 'n'.")








def main():
    print(Fore.CYAN + text2art("Barista Assistant", font="small") + Style.RESET_ALL)
    print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)
    print(Fore.CYAN + "Welcome to your Barista Assistant!" + Style.RESET_ALL)
    print(Fore.YELLOW + "-" * 40 + Style.RESET_ALL)

    user = get_user_profile()

    while True:

        print(Fore.YELLOW + "\nChoose an option:")
        print("1. Start brewing")
        print("2. View history")
        print("3. Exit" + Style.RESET_ALL)

        choice = input(Fore.BLUE + "\nEnter your choice (1-3): " + Style.RESET_ALL).strip()




if __name__ == "__main__":
    main()
