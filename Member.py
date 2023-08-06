class Member:
    __member_list = []
    member_id = 100

    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__classes_enrolled = []
        Member.__member_list.append(self)
        

    @classmethod
    def new_member(cls, name):
        new_memberID = cls.member_id
        cls.member_id += 1
        return cls(name, new_memberID)
    
    def add_enrolled_class(self, class_name):
        self.__classes_enrolled.append(class_name)

    def get_enrolled_class(self):
        enrolled_classes = "\n".join(self.__classes_enrolled)
        return enrolled_classes
    
    def get_enrolled_check(self):
        return self.__classes_enrolled
    
    def cancel_class(self, class_name):
        if class_name in self.__classes_enrolled:
            self.__classes_enrolled.remove(class_name)


    def __str__(self):
        return f"{self.__member_id:>5}\t\t{self.__name}"
        
    