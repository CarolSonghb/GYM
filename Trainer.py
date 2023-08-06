class Trainer:
    __trainer_list = []

    def __init__(self, name, expertise):
        self.__name = name
        self.__expertise = expertise
        self.__assigned_classes = []
        Trainer.__trainer_list.append(self)

    @property
    def trainer_name(self):
        return self.__name
    
    def assign_class(self, group_exercise):
        self.__assigned_classes.append(group_exercise)

    @classmethod
    def get_trainer_list(cls):
        return cls.__trainer_list
    
    def get_trainer_classes(self):
        return self.__assigned_classes

    def __str__(self):
        return f"{self.__name}'s expertise is {self.__expertise}"