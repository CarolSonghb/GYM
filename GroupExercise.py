from Member import Member


class GroupExercise:
    __class_list = []

    def __init__(self, name, max_capacity, fee):
        self.__name = name
        self.__max_capacity = max_capacity
        self.__fee = fee
        self.__trainer = None
        self.__enrolled_member = []
        self.__waitlisted_member = []
        self.__checked_in_member = []
        GroupExercise.__class_list.append(self)
    
    # get name of a group class
    @property
    def class_name(self):
        return self.__name
    
    # get fee of a group class
    @property
    def class_fee(self):
        return self.__fee
    
    #get capacity of a group class
    @property
    def class_capacity(self):
        return self.__max_capacity
    
    def get_trainer(self):
        return self.__trainer
    
    def get_enrolled_member(self):
        return self.__enrolled_member
    
    def get_wailist(self):
        return self.__waitlisted_member
    
    def get_checked_in_member(self):
        return self.__checked_in_member
    
    def check_in_member(self, member):
        if member in self.__enrolled_member:
            self.__checked_in_member.append(member)
            return f"{member._Member__name} has successfully checked in to class {self.__name}."
        else:
            return f"{member._Member__name} is not enrolled in this class."
 
    
    # Enrols a gym member into the group exercise class.
    # If the class is full, the member will be added to the waitlist.
    def enrol_member(self, member):
        if not isinstance(member, Member):
            return "Invalid member object."
        
        if len(self.__enrolled_member) < self.__max_capacity:
            # add the member to the enrolled_member list
            self.__enrolled_member.append(member)
            return f"{member._Member__name} has been enrolled in {self.__name}."
        else:
            # add the member to the waitlist
            self.__waitlisted_member.append(member)
            return f"{self.__name} is full. {member._Member__name} has been added to the waitlist.."
    

    def update_fee(self, new_fee):
        self.__fee = new_fee

    def assign_trainer(self, trainer):
        self.__trainer = trainer
    

    def __str__(self):
        return f"{self.__name:>10} {self.__max_capacity:>8} {self.__fee:>10}"
