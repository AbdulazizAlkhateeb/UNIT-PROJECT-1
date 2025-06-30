from bean import Bean



class Recipe:
    GRIND_SIZE_MAX = 30
    GRIND_SIZE_MIN = 1

    def __init__(self, bean: Bean, milk_ml: int, ratio: str, grind_size: int, steps:list):
        self.set_bean(bean)
        self.set_milk_ml(milk_ml)
        self.set_ratio(ratio)
        self.set_grind_size(grind_size)
        self.set_steps()

#Getters

    def get_bean(self) -> Bean:
        return self.__bean

    def get_milk_ml(self):
        return self.__milk_ml

    def get_ratio(self):
        return self.__ratio

    def get_grind_size(self):
        return self.__grind_size
    
    def get_steps(self):
        return self.steps




#Setters
    def set_bean(self, bean):
        if isinstance(bean, Bean):
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





    def set_grind_size(self, grind_size):
        if isinstance(grind_size, int)and self.GRIND_SIZE_MIN <= grind_size <= self.GRIND_SIZE_MAX:
            self.__grind_size = grind_size
        else:
            raise ValueError(f"grind_size must be int between {self.GRIND_SIZE_MIN} and {self.GRIND_SIZE_MAX}")


    def set_steps(self, steps:list):
        if isinstance(steps, list):
            self.__steps= self
        else:
            raise ValueError("steps must be a list ")