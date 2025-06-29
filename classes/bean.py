class Bean: 

    def __init__(self, bean_name:str, region:str, notes:list, roast:str, is_available: bool = True):
        self.set_name(bean_name)
        self.set_region(region)
        self.set_notes(notes)        
        self.set_roast(roast)
        self.is_available = is_available



#Getters
    def get_name(self):
        return self.__bean_name


    def get_region(self):
        return self.__region


    def get_notes(self):
        return self.__notes


    def get_roast(self):
        return self.__roast

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


    def set_roast(self, roast):
        if roast in ["light", "medium", "dark"]:
            self.__roast = roast
        else:
            raise ValueError("roast must be one of: light, medium, dark")



def change_availablty(self, change_available: bool):
    if self.is_available == True and change_available ==True or self.is_available== False and change_available== False:
        print("Nothing is change")

    else: 
        self.is_available == change_available
        print("Changeded successfully")





