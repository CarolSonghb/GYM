class Trainer:
    __trainer_list = []

    def __init__(self, name, expertise):
        self.__name = name
        self.__expertise = expertise
        self.__assigned_classes = []
        Trainer.__trainer_list.append(self)
    
    # get trainer's name
    @property
    def trainer_name(self):
        return self.__name
    
    @property
    def expertise(self):
        return self.__expertise
    
    @property
    def assigned_class(self):
        return self.__assigned_classes
    
    @classmethod
    def trainer_list(cls):
        return cls.__trainer_list
    
    # adds a group exercise class to the list of classes assigned to the trainer
    def assign_class(self, group_exercise):
        self.assigned_class.append(group_exercise)
        return f"Class '{group_exercise.class_name}' has been assigned to Trainer '{self.trainer_name}'"
    
    # get a list of group exercise classes assigned to the trainer
    def get_trainer_classes(self):
        return self.__assigned_classes
    
    # return a string that includes trainer's name and expertise
    def __str__(self):
        return f"{self.__name:>5}\t{self.__expertise}"