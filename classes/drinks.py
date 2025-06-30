from recipe import Recipe


class Drink:
    def __init__(self, drink_name: str,price:float, recipe:Recipe , sizes:list, ratings):
        self.set_name(drink_name)
        self.set_price(price)
        self.set_recipe(recipe)
        self.set_sizes(sizes)
        self.set_ratings(ratings if ratings is not None else [])





#Getters
    def get_name(self):
        return self.__drink_name

    def get_price(self):
        return self.__price

    def get_recipe(self):
        return self.__recipe

    def get_sizes(self) -> list:
        return self.__sizes

    def get_ratings(self) -> list:
        return self.__ratings     





#Setters
    def set_name(self, drink_name):
        if isinstance(drink_name, str):
            self.__drink_name = drink_name
        else:
            raise ValueError("name must be a string")




    def set_price(self, price):
        if isinstance(price, float) and price > 0:
            self.__price = price
        else:
            raise ValueError("price must be a positive number")



    def set_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.__recipe = recipe
        else:
            raise ValueError("recipe must be a Recipe object")




    # def set_sizes(self, sizes):





    # def set_ratings(self, ratings):






    # def add_rating(self, score: int):

    # def get_avg_rating(self):

