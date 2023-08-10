# Student Name: Carol (Haibei) Song
# Student ID: 1154836

# A driver program that simulates the management of group exercise classes in a gym
from GroupExercise import *
from Member import *
from Trainer import *

# Required functionalities are as follows:

# 1. Create 2 GroupExercise objects, 5 Member objects and 2 Trainer objects.
class1 = GroupExercise("Zumba", 2, 0.0)
class2 = GroupExercise("Pilates", 4, 0.0)
print("\nNew classes have been created!")
print("")
print(f"{'':<3}ClassName{'':<5}Slots{'':<5}Fee")
print("------------------------------------")
print(class1)
print(class2)
print("")

member1 = Member.new_member("Alice Wonderland")
member2 = Member.new_member("Kenneth Duncan")
member3 = Member.new_member("Barbie Brown")
member4 = Member.new_member("Adam Curtin")
member5 = Member.new_member("Carol Song")
print("\nNew members have been created!")
print("")
print(f"MemberID{'':<8}MemberName")
print("------------------------------------")
print(member1)
print(member2)
print(member3)
print(member4)
print(member5)
print("")

trainer1 = Trainer("Jane Doe", "Aerobic Exercise")
trainer2 = Trainer("Will Smith", "Injury Prevention")
print("\nNew trainer have been created!")
print("")
print(f"TrainerName{'':<8}Expertise")
print("------------------------------------")
print(trainer1)
print(trainer2)
print("")

# 2. Assign a trainer to each group exercise class.
assignClass1 = class1.assign_trainer(trainer1)
assignClass2 = class2.assign_trainer(trainer2)
trainer1Class = trainer1.assign_class(class1)
trainer2Class = trainer2.assign_class(class2)
print(assignClass1)
print(assignClass2)
print(trainer1Class)
print(trainer2Class)
print("")

# 3. Set the class fee for each group exercise class.
class1Fee = class1.update_fee(10.0)
class2Fee = class2.update_fee(20.0)
print(class1Fee)
print(class2Fee)
print("")

# 4. Set up specific member booking for a group exercise class.
enrolResult1 = class1.enrol_member(member1)
member1.add_enrolled_class(class1)
enrolResult2 = class1.enrol_member(member2)
member2.add_enrolled_class(class1)
enrolResult3 = class1.enrol_member(member3)
member3.add_enrolled_class(class1)
enrolResult4 = class2.enrol_member(member4)
member4.add_enrolled_class(class2)
enrolResult5 = class2.enrol_member(member5)
member5.add_enrolled_class(class2)
print(enrolResult1)
print(enrolResult2)
print(enrolResult3)
print(enrolResult4)
print(enrolResult5)
print("")


# 5. Cancelling a specific member’s group exercise class.

cancelResult = class2.member_cancel(member5)
memberCancel = member5.cancel_class(class2)
print(cancelResult)
print(memberCancel)
print("")

# 6. Record a specific member checking in to a group exercise class.
checkInResult = class1.check_in_member(member2)
print(checkInResult)
print("")

# 7. Display the list of enrolled participants for a group exercise class.
enrollList = class1.get_enrolled_member()
print(f"Enrolled Members in Class '{class1.class_name}':")
for member in enrollList:
    print(member)
print("")

# 8. Display the waiting list for a group exercise class.
waitList = class1.get_waitlist()
print(f"Waitlist Members in Class '{class1.class_name}':")
for member in waitList:
    print(member)
print("")

# 9. Display the available slots for a group exercise class.
availableClass1 = class1.get_available_slot()
availableClass2 = class2.get_available_slot()
print(f"Available slots for Class '{class1.class_name}': {availableClass1}")
print(f"Available slots for Class '{class2.class_name}': {availableClass2}")
print("")

# 10. Display the number of participants enrolled in a group exercise class.
countClass1 = class1.get_enrolled_number()
countClass2 = class2.get_enrolled_number()
print(f"Number of participants enrolled in Class '{class1.class_name}': {countClass1}")
print(f"Number of participants enrolled in Class '{class2.class_name}': {countClass2}")
print("")

# 11. Display the number of wait list participants in a group exercise class.
waitlist_count1 = class1.get_waitlist_number()
waitlist_count2 = class2.get_waitlist_number()
print(
    f"Number of waitlist participants in Class '{class1.class_name}': {waitlist_count1}"
)
print(
    f"Number of waitlist participants in Class '{class2.class_name}': {waitlist_count2}"
)
print("")

# 12. Display the number of attendees for a group exercise class.
attendees_count = class1.get_attendees_number()
print(f"Number of attendees in Class '{class1.class_name}': {attendees_count}")

# 13. Display the attendance percentage for a group exercise class.
attendance_percentage = class1.get_attendance_percentage()
print(
    f"Attendance percentage for Class '{class1.class_name}': {attendance_percentage:.2f}%"
)

# 14. Display the total payment collected for a group exercise class.
total_payment = class1.total_payment()
print(f"Total payment collected for Class '{class1.class_name}': ${total_payment:.2f}")

# 15. Display the list of group exercise classes for which a specific member is enrolled.
enrolled_classes = member1.get_enrolled_check()

if enrolled_classes:
    print(f"\nClasses enrolled by {member1.member_name}:")
    for aClass in enrolled_classes:
        print(aClass.class_name)
else:
    print(f"{member1.member_name} is not enrolled in any classes.")

# 16. Display the list of classes offered by a particular trainer.
trainer_classes = trainer1.get_trainer_classes()

if not trainer_classes:
    print(f"\nTrainer {trainer1.trainer_name} is not assigned to any classes.")
else:
    print(f"\nClasses assigned to Trainer '{trainer1.trainer_name}':")
    for group_class in trainer_classes:
        print(group_class.class_name)

print("\nThe end. Thank you.")
