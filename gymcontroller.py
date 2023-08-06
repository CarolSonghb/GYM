from GroupExercise import GroupExercise
from Member import Member
from Trainer import Trainer

if __name__ == "__main__":


    # Create 2 GroupExercise objects
    class1 = GroupExercise("Zumba", 2, 10)
    class2 = GroupExercise("Pilates", 4, 20)
    print("")
    print("========== Class Overview ==========")
    print("")
    print(f"{'':<5}Name{'':<8}Slots{'':<5}Fee")
    print("------------------------------------")
    # Access the class_list using the class name
    for aClass in GroupExercise._GroupExercise__class_list:
        print(aClass)
    print("")
    print("====================================")
    print("")

    #Create 5 Member objects
    member1 = Member.new_member("Alice Wonderland")
    member2 = Member.new_member("Kenneth Duncan")
    member3 = Member.new_member("Barbie Brown")
    member4 = Member.new_member("Adam Curtin")
    member5 = Member.new_member("Carol Song")
    
    
    print(member1)
    print(member2)

    #Create 2 Trainer objects
    trainer1 = Trainer("Jane Doe", "Aerobic Exercise")
    trainer2 = Trainer("Will Smith", "Injury Prevention")
    print(trainer1)
    print(trainer2)

    enrollment_result = class1.enrol_member(member1)
    print(enrollment_result)
    enrollment_result = class1.enrol_member(member2)
    print(enrollment_result)
    enrollment_result = class1.enrol_member(member3)
    print(enrollment_result)

    

