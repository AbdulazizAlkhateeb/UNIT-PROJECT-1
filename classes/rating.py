from datetime import datetime



class Rating:

    def __init__(self, drink: str, score: int, reviewed_at: datetime = None):
        self.set_drink(drink)
        self.set_score(score)
        self.set_reviewed_at(reviewed_at)




#Getters
    def get_drink(self):
        return self.__drink

    def get_score(self):
        return self.__score

    def get_reviewed_at(self):
        return self.__reviewed_at




#Setters
    def set_drink(self, drink):
        if isinstance(drink, str):
            self.__drink = drink
        else:
            raise ValueError("drink must be a string")

    def set_score(self, score):
        if isinstance(score, int) and 1 <= score <= 5:
            self.__score = score
        else:
            raise ValueError("score must be an int between 1 and 5")

    def set_reviewed_at(self, reviewed_at):
        if isinstance(reviewed_at, datetime):
            self.__reviewed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        else:
            raise ValueError("reviewed_at must be a datetime object")
