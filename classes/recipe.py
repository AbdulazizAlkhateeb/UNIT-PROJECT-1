from classes.beans import Beans


class Recipe:
    GRIND_SIZE_MAX = 30
    GRIND_SIZE_MIN = 1

    def __init__(self, bean: Beans, grind_coffee_grams:int , milk_ml: int, ratio: str, grind_size: int, steps:list):
        self.set_bean(bean)
        self.set_milk_ml(milk_ml)
        self.set_ratio(ratio)
        self.set_grind_size(grind_size)
        self.set_steps(steps)
        self.set_grind_coffee_grams(grind_coffee_grams)

    def __str__(self):
        return f"ratio = {self.__ratio}, grind_size = {self.__grind_size}, steps = {self.__steps}, \n(bean = {self.__bean})"

    #Getters

    def get_bean(self) -> Beans:
        return self.__bean

    def get_milk_ml(self):
        return self.__milk_ml

    def get_ratio(self):
        return self.__ratio

    def get_grind_size(self):
        return self.__grind_size
    
    def get_steps(self):
        return self.__steps
    
    def get_grind_coffee_grams(self):
        return self.__grind_coffee_grams



#Setters
    def set_bean(self, bean):
        if isinstance(bean, Beans):
            self.__bean = bean
        else:
            raise ValueError("bean must be a Bean object")



    def set_milk_ml(self, milk_ml):
        if isinstance(milk_ml, int) and milk_ml >= 0:
            self.__milk_ml = milk_ml
        else:
            raise ValueError("milk_ml must be a non-negative int")
        




    def set_ratio(self, ratio):
        if isinstance(ratio, str) and ":" in ratio:
            self.__ratio = ratio
        else:
            raise ValueError("ratio must be a string like \"1:15\"")
        

    def set_grind_coffee_grams(self, grams):
        if isinstance(grams, int) and grams>0:
            self.__grind_coffee_grams=grams
        else:
            raise ValueError("grind coffee in grams must be int")





    def set_grind_size(self, grind_size):
        if isinstance(grind_size, int)and self.GRIND_SIZE_MIN <= grind_size <= self.GRIND_SIZE_MAX:
            self.__grind_size = grind_size
        else:
            raise ValueError(f"grind_size must be int between {self.GRIND_SIZE_MIN} and {self.GRIND_SIZE_MAX}")


    def set_steps(self, steps: list):
        if isinstance(steps, list):
            self.__steps = steps
        else:
            raise ValueError("steps must be a list")



        


#-----
    def get_water_needed(self):
        grind= self.__grind_coffee_grams
        ratio_parts = self.__ratio.split(":")
        ratio = float(ratio_parts[1])
        return round(grind * ratio, 2)





    def to_dict(self):
        return {
            "bean": self.__bean.to_dict(),
            "grind_coffee_grams": self.__grind_coffee_grams,
            "milk_ml": self.__milk_ml,
            "ratio": self.__ratio,
            "grind_size": self.__grind_size,
            "steps": self.__steps
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            bean=Beans.from_dict(data["bean"]),
            grind_coffee_grams=data["grind_coffee_grams"],
            milk_ml=data["milk_ml"],
            ratio=data["ratio"],
            grind_size=data["grind_size"],
            steps=data["steps"]
        )