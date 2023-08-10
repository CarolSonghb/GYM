class Member:
    __member_list = []
    member_id = 100

    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__classes_enrolled = []
        Member.__member_list.append(self)
    
    @property
    def member_name(self):
        return self.__name
    
    @property
    def memberId(self):
        return self.__member_id
    
    # when adding a new member, increase their member ID by 1
    @classmethod
    def new_member(cls, name):
        new_memberID = cls.member_id
        cls.member_id += 1
        return cls(name, new_memberID)
    
    # add a new enrolled class to the enrolled list
    def add_enrolled_class(self, class_name):
        self.__classes_enrolled.append(class_name)
    
    # get all booked class of the member
    def get_enrolled_class(self):
        enrolled_classes = "\n".join(self.__classes_enrolled)
        return enrolled_classes
    
    # when checking in, return a list of enrolled classes of the member
    def get_enrolled_check(self):
        return self.__classes_enrolled
    
    # cancels enrolment in a group exercise class
    def cancel_class(self, class_name):
        if class_name in self.__classes_enrolled:
            self.__classes_enrolled.remove(class_name)
            return f"'{self.__name}' has canceled Class '{class_name.class_name}'"
        else:
            return f"You are not enrolled in the class"

    # return a string that includs member ID and name
    def __str__(self):
        return f"{self.__member_id:>5}\t\t{self.__name}"
        
    