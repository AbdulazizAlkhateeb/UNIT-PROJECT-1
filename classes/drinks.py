from classes.recipe import Recipe
from classes.rating import Rating


class Drink:
    def __init__(self, drink_name: str, price:float, recipe:Recipe , ratings:list):
        self.set_name(drink_name)
        self.set_price(price)
        self.set_recipe(recipe)
        self.set_ratings(ratings if ratings is not None else [])

    def __str__(self):
        return f"drink_name = {self.__drink_name}, price = {self.__price}, ratings = {self.get_ratings_obj()}, (recipe = {self.__recipe})"

    #Getters
    def get_name(self):
        return self.__drink_name

    def get_price(self):
        return self.__price

    def get_recipe(self):
        return self.__recipe

    def get_ratings(self) -> list:
        return self.__ratings

    def get_ratings_obj(self):
        for rating in self.__ratings:
            return rating
        return []
        # return self.__ratings







#Setters
    def set_name(self, drink_name):
        if isinstance(drink_name, str):
            self.__drink_name = drink_name
        else:
            raise ValueError("name must be string")




    def set_price(self, price):
        if isinstance(price, float) and price > 0:
            self.__price = price
        else:
            raise ValueError("price must be positive number")



    def set_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.__recipe = recipe
        else:
            raise ValueError("recipe must be a Recipe object")



    def set_ratings(self, ratings:list):
        if isinstance(ratings, list):
            self.__ratings= ratings
        else:
            raise ValueError("ratings must be list")




    def add_rating(self, score: int, description:str):
        # rating_list =[]
        new_rating=Rating(self.get_name(), score, description)
        self.__ratings.append(new_rating)
        
        
 #--

    def get_avg_rating(self) -> float:
        if not self.__ratings:
            return 0.0

        total_score = sum(rate.get_score() for rate in self.__ratings)
        avg_score = total_score / len(self.__ratings)
        return round(avg_score, 2)

    def get_drink_info(self):
        avg_rating = self.get_avg_rating()
        avg_text = "No ratings yet" if avg_rating == 0.0 else avg_rating
        last_description = self.__ratings[-1].get_description() if self.__ratings else "No ratings yet"
        return f"Drink: {self.__drink_name}, Price: {self.__price}, Average Rating: {avg_text}, Last Review: {last_description}"



    def to_dict(self):
        return {
            "drink_name": self.__drink_name,
            "price": self.__price,
            "recipe": self.__recipe.to_dict(),
            "ratings": [rate.to_dict() for rate in self.__ratings]
        }

    @classmethod
    def from_dict(cls, data):
        recipe = Recipe.from_dict(data["recipe"])
        ratings = [Rating.from_dict(rate) for rate in data["ratings"]]
        return cls(
            data["drink_name"],
            data["price"],
            recipe,
            ratings
        )