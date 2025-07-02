from datetime import datetime


class Rating:

    def __init__(self, drink: str, score: int, description: str, reviewed_at: datetime = None):
        self.set_drink(drink)
        self.set_score(score)
        self.set_reviewed_at(reviewed_at)
        self.set_description(description)

    def __str__(self):
        return f"drink = {self.__drink}, score = {self.__score}, reviewed_at = {self.__reviewed_at}"

    # Getters
    def get_drink(self):
        return self.__drink

    def get_score(self):
        return self.__score

    def get_reviewed_at(self):
        return self.__reviewed_at

    def get_description(self):
        return self.__description

    def get_rating_info(self):
        return f"Score 5/{self.__score} \nReviewed at:({self.__reviewed_at} \nDescription:{self.__description} )"

    # Setters
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

    def set_description(self, description: str):
        if isinstance(description, str):
            self.__description = description

        else:
            raise ValueError("description must be a string")


    def set_reviewed_at(self, reviewed_at):
        if reviewed_at is None:
            self.__reviewed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(reviewed_at, datetime):
            self.__reviewed_at = reviewed_at.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(reviewed_at, str):
            self.__reviewed_at = reviewed_at
        else:
            raise ValueError("reviewed_at must be a datetime object, a string, or None")




    def to_dict(self):
        return {
            "drink": self.__drink,
            "score": self.__score,
            "description": self.__description,
            "reviewed_at": self.__reviewed_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["drink"],
            data["score"],
            data["description"],
            datetime.strptime(data["reviewed_at"], "%Y-%m-%d %H:%M:%S")
        )