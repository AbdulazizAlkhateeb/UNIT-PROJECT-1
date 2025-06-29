from bean import Bean


class User:

    def __init__(self, user_name: str, machines: list, beans: list):
        self.set_name(user_name)
        self.set_machines(machines)
        self.set_beans(beans)

#Getters
    def get_name(self):
        return self.__user_name

    def get_machines(self):
        return self.__machines

    def get_beans(self):
        return self.__beans

#Setters
    def set_name(self, user_name):
        if isinstance(user_name, str):
            self.__user_name = user_name
        else:
            raise ValueError("user name must be a string")

    def set_machines(self, machines):
        if isinstance(machines, list):
            self.__machines = machines
        else:
            raise ValueError("machines must be a list of strings")

    def set_beans(self, beans):
        if isinstance(beans, list) and all(isinstance(bean, Bean) for bean in beans):
            self.__beans = beans
        else:
            raise ValueError("beans must be a list of Bean objects")




