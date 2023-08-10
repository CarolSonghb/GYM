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
    
    # get capacity of a group class
    @property
    def class_capacity(self):
        return self.__max_capacity
    
    # set the fee amount for the class
    def update_fee(self, new_fee):
        self.__fee = new_fee
        return f"The fee for Class '{self.__name}' has been set to ${self.__fee}."
    
    # assign a trainer to conduct the group exercise class
    def assign_trainer(self, trainer):
        self.__trainer = trainer
        return f"Trainer '{self.__trainer.trainer_name}' has been assigned to the Class '{self.__name}'"
    
    def member_cancel(self, member):
        if member in self.__enrolled_member:
            self.__enrolled_member.remove(member)
            return f"Enrollment for Member{member.memberId} '{member.member_name}' in Class '{self.__name}' has been cancelled."
        else:
            return f"Member{member.memberId} '{member.member_name}' is not enrolled in Class '{self.__name}'."
    
    # get trainer's info
    def get_trainer(self):
        if self.__trainer is not None:
            return self.__trainer.trainer_name
        else:
            return str("None")
    
    # get all gym members currently enrolled in the group exercise class
    def get_enrolled_member(self):
        return self.__enrolled_member
    
    # return the number of gym members currently enrolled in the class
    def get_enrolled_number(self):
        return len(self.__enrolled_member)
    
    # get the waiting list for a group exercise class
    def get_waitlist(self):
        return self.__waitlisted_member
    
    # return the number of waitlist participants in a group exercise class
    def get_waitlist_number(self):
        return len(self.__waitlisted_member)
    
    # return the number of avaliable slots for enrolment in the class
    def get_available_slot(self):
        return self.__max_capacity - len(self.__enrolled_member)
    
    # return a list of attendees for a class
    def get_checked_in_member(self):
        return self.__checked_in_member
    
    # get the number of attendees for a class
    def get_attendees_number(self):
        return len(self.__checked_in_member)
    
    # get the attendance percentage for a group exercise class
    def get_attendance_percentage(self):
        if len(self.__enrolled_member) == 0:
            return 0
        return (len(self.__checked_in_member) / len(self.__enrolled_member)) * 100
    
    # mark a gym member's attendance for the class by adding them to the check-in list
    def check_in_member(self, member):
        if member in self.__enrolled_member:
            self.__checked_in_member.append(member)
            return f"'{member.member_name}' has successfully checked in to Class '{self.__name}'."
        else:
            return f"{member.member_name} is not enrolled in this class."
    
    # calculate and return the total payment received
    def total_payment(self):
        return len(self.__enrolled_member) * self.__fee

    # Enrols a gym member into the group exercise class.
    # If the class is full, the member will be added to the waitlist.
    def enrol_member(self, member):
        if len(self.__enrolled_member) < self.__max_capacity:
            # add the member to the enrolled_member list
            self.__enrolled_member.append(member)
            return f"Member{member.memberId} '{member.member_name}' is succesfully enrolled in Class '{self.__name}'."
        else:
            # add the member to the waitlist
            self.__waitlisted_member.append(member)
            return f"Class '{self.__name}' is full. Member{member.memberId} '{member.member_name}' has been added to the waitlist.."
    
    
    
    # returns a string that includes class name, max capacity and fee
    def __str__(self):
        return f"{self.__name:>10} {self.__max_capacity:>8} {self.__fee:>10}"
