class Beans: 

    def __init__(self, bean_name:str, region:str, notes:list, roast_level:str,price_per_kg:float, is_available: bool = True, stock_grams: float = 0):
        self.set_name(bean_name)
        self.set_region(region)
        self.set_notes(notes)        
        self.set_roast(roast_level)
        self.set_price_per_kg(price_per_kg)
        self.is_available = is_available
        self.set_stock_grams(stock_grams)

    def __str__(self):
        return  f"bean_name = {self.__bean_name}, region = {self.__region}, note = {self.__notes}"

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

    def get_stock_grams(self):
        return self.__stock_grams

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

    def set_stock_grams(self, grams):
        if isinstance(grams, (int, float)) and grams >= 0:
            self.__stock_grams = grams
        else:
            raise ValueError("stock_grams must be non-negative number")



    def use_grams(self, grams_used: float):
        if not isinstance(grams_used, (int, float)) or grams_used <= 0:
            raise ValueError("Used grams must be positive number")


        self.__stock_grams -= grams_used

        if self.__stock_grams <= 0:
            self.__stock_grams = 0
            self.is_available = False
            print( "Stock depleted. Marked as unavailable." )
        else:
            print(f"{grams_used}g used. Remaining stock: {self.__stock_grams}g")



    def change_availability(self, availability: bool):
        if not isinstance(availability, bool):
            raise ValueError("availability must be boolean")

        if self.is_available == availability:
            print("no change")
        else:
            self.is_available = availability
            print("availability updated")

    def get_bean_info(self):
        return f"Bean: {self.__bean_name}, Region: {self.__region}, Roast: {self.__roast}, Price/kg: {self.__price_per_kg} SR, Stock in grams: {self.__stock_grams}"




    def to_dict(self):
        return {
            "bean_name": self.__bean_name,
            "region": self.__region,
            "notes": self.__notes,
            "roast_level": self.__roast,
            "price_per_kg": self.__price_per_kg,
            "is_available": self.is_available,
            "stock_grams": self.__stock_grams
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["bean_name"],
            data["region"],
            data["notes"],
            data["roast_level"],
            data["price_per_kg"],
            data["is_available"],
            data.get("stock_grams", 0)  # default to 0 if missing
        )
