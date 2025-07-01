from art import text2art
from colorama import Fore, Back, Style
from classes.drinks import Drink
from classes.recipe import Recipe
# from classes.rating import Rating
from classes.beans import Beans
import json
import os



if __name__ == '__main__':

    listOfDrink = []
    bean = Beans('arabic', 'Saudi Arabia', ['bitter', 'soar'], 'dark', 100)
    recipe = Recipe(bean, 18, 0, '1:15', 15, ['step 1', 'step 2', 'step 3'])
    drink = Drink('black coffie', 10.0,  recipe, [])
    listOfDrink.append(drink)

    for i in listOfDrink:
        print(i)

    print("hello")