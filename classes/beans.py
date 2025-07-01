class Beans: 

    def __init__(self, bean_name:str, region:str, notes:list, roast_level:str,price_per_kg:float, is_available: bool = True):
        self.set_name(bean_name)
        self.set_region(region)
        self.set_notes(notes)        
        self.set_roast(roast_level)
        self.set_price_per_kg(price_per_kg)
        self.is_available = is_available

    def __str__(self):
        return  f"bean_name = {self.__bean_name}, region = {self.__region}, note = {self.__notes}"
        #return f"bean_name = {self.__bean_name}, region = {self.__region}, note"

    #Getters
    def get_name(self):
        return self.__bean_name


    def get_region(self):
        return self.__region


    def get_notes(self):
        return self.__notes


    def get_roast(self):
        return self.__roast
    
    def get_price_per_kg(self):
        return self.__price_per_kg

#Setters

    def set_name(self, bean_name):
        if isinstance(bean_name, str):
            self.__bean_name = bean_name
        else:
            raise ValueError("name must be a string")


    def set_region(self, region):
        if isinstance(region, str):
            self.__region = region
        else:
            raise ValueError("region must be a string")


    def set_notes(self, notes):
        if isinstance(notes, list):
            self.__notes = notes
        else:
            raise ValueError("notes must be a list")
        

    def set_price_per_kg(self, price_per_kg):
        if isinstance(price_per_kg, (float, int)) and price_per_kg>0:
            self.__price_per_kg=price_per_kg
        else:
            raise ValueError("The price must be float")


    def set_roast(self, roast):
        if roast in ["light", "medium", "dark"]:
            self.__roast = roast
        else:
            raise ValueError("roast must be one of: light, medium, dark")



    def change_availability(self, availability: bool):
        if not isinstance(availability, bool):
            raise ValueError("availability must be boolean")

        if self.is_available == availability:
            print("no change")
        else:
            self.is_available = availability
            print("availability updated")


    def to_dict(self):
        return {
            "bean_name": self.__bean_name,
            "region": self.__region,
            "notes": self.__notes,
            "roast_level": self.__roast,
            "price_per_kg": self.__price_per_kg,
            "is_available": self.is_available
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            data["bean_name"],
            data["region"],
            data["notes"],
            data["roast_level"],
            data["price_per_kg"],
            data["is_available"]
            )



