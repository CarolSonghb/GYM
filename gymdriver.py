from GroupExercise import *
from Member import *
from Trainer import *


class1 = GroupExercise("Zumba", 2, 10.0)
class2 = GroupExercise("Pilates", 4, 20.0)

member1 = Member.new_member("Alice Wonderland")
member2 = Member.new_member("Kenneth Duncan")
member3 = Member.new_member("Barbie Brown")
member4 = Member.new_member("Adam Curtin")
member5 = Member.new_member("Carol Song")

# Create 2 Trainer objects
trainer1 = Trainer("Jane Doe", "Aerobic Exercise")
trainer2 = Trainer("Will Smith", "Injury Prevention")


# check if the class name that users input exist in the system
def checkClass(class_name):
    for aClass in GroupExercise._GroupExercise__class_list:
        if aClass.class_name == class_name:
            return aClass
    return None


# View a list of current group classes
def viewClass():
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

def viewEnrolledList():
    class_name = input("Enter the class name to check its enrolled list: ")

    selected_class = checkClass(class_name)

    if selected_class:
        enrolled_members = selected_class.get_enrolled_member()

        if enrolled_members:
            print(f"\nEnrolled members for class '{class_name}' are:")
            for aMember in enrolled_members:
                print(aMember)
        else:
            print("No member has enrolled in this class.")
    else:
        print(f"Class '{class_name}' not found. Please try again.")
        viewClass()
        viewEnrolledList()

def viewWaitlist():
    class_name = input("Enter the class name to check its waitlist: ")

    selected_class = checkClass(class_name)

    if selected_class:
        waitlist_members = selected_class.get_wailist()
        if waitlist_members:
            print(f"\nWaitlisted members for class '{class_name}' are:")
            for aMember in waitlist_members:
                print(aMember)
        else:
            print("No member has enrolled in this class.")
    else:
        print(f"Class '{class_name}' not found. Please try again.")
        viewClass()

def viewAllClass():
    viewClass()
    print("\n1. Check Enrolled List")
    print("2. Check Wait List")
    chosen = input("Please select a number from the menu: ")
    if chosen == "1":
        viewEnrolledList()
    elif chosen == "2":
        viewWaitlist()
    else:
        print("Invalid response, please try again.")
        viewAllClass()

# Add a new group class
def addClass():
    print("\nAdding a New Class")
    name = input("Enter class name: ")
    max_capacity = int(input("Enter max capacity: "))
    fee = float(input("Enter class fee: "))

    new_class = GroupExercise(name, max_capacity, fee)
    print("========================================")
    print(
        f"Class '{new_class.class_name}' has been added with a maximum capacity of {new_class.class_capacity} and a fee of ${new_class.class_fee}."
    )
    print("========================================")


# Add a new member
def addMember():
    print("\nAdding a New Member")
    firstName = input("Enter member's first name: ")
    lastName = input("Enter member's last name: ")
    name = firstName + " " + lastName
    new_member = Member.new_member(name)
    print(
        f"Member '{new_member._Member__name}' has been added with a member ID of {new_member._Member__member_id}."
    )


# View a list of current members
def viewMember():
    print("")
    print("========== Member List ==========")
    print("")
    print(f"MemberID{'':<8}Name")
    # Access the member_list using the class name
    for aMember in Member._Member__member_list:
        print(aMember)


def bookClass():
    viewClass()
    book_class = input("Enter the name of the class you want to book: ")

    selected_class = checkClass(book_class)

    if selected_class:
        member_id = input("Enter your member ID: ")
        selected_member = None
        for aMember in Member._Member__member_list:
            if str(aMember._Member__member_id) == member_id:
                selected_member = aMember
                break

        if selected_member:
            result = selected_class.enrol_member(selected_member)
            if "enrolled" in result:
                selected_member.add_enrolled_class(selected_class.class_name)
            print(result)
        else:
            print(f"Member {member_id} doesn't exist. Please try again.")
            bookClass()
    else:
        print(f"Group Class '{book_class} not found. Please try again.'")
        book_class()


def cancelClass():
    member_id = input("Enter your member ID: ")
    selected_member = None
    for aMember in Member._Member__member_list:
        if str(aMember._Member__member_id) == member_id:
            selected_member = aMember
            print(selected_member)
            break
    if selected_member:
        enrolled_classes = selected_member.get_enrolled_class()
        if enrolled_classes:
            print(
                f"Member ID {member_id} {selected_member._Member__name}'s enrolled group classes are: "
            )
            print(enrolled_classes)
            class_to_cancel = input("Enter the name of the class to cancel: ")
            selected_member.cancel_class(class_to_cancel)
            print(
                f"Class '{class_to_cancel}' has been removed from {selected_member._Member__name}'s booking."
            )
        else:
            print("No enrolled classes found for the member.")
            dispMainMenu()
    else:
        print(f"This Member ID {member_id} is not found in the system")


def updateFee():
    viewClass()
    class_name = input("Enter the name of the class to update the fee: ")
    selected_class = checkClass(class_name)

    if selected_class:
        new_fee = float(input("What will the new fee be: "))
        selected_class.update_fee(new_fee)
        print(f"'{class_name}'s fee has been updated to ${new_fee}")
    else:
        print(
            f"The class name you entered is not found in the system.\nPlease try again."
        )
        updateFee()


def viewTrainers():
    print("\n========== List of Trainers ==========")
    print(f"\n{'Trainer Name':<20}Expertise")
    print("---------------------------------------")

    for aTrainer in Trainer._Trainer__trainer_list:
        print(f"{aTrainer._Trainer__name:<20}{aTrainer._Trainer__expertise}")

    print("\n=======================================")


def assignTrainer():
    viewClass()
    class_name = input("Enter the name of the class to assign a trainer to: ")

    selected_class = checkClass(class_name)

    if selected_class:
        viewTrainers()
        trainer_name = input("Enter the name of the trainer for the class: ")

        selected_trainer = None
        for aTrainer in Trainer._Trainer__trainer_list:
            if aTrainer._Trainer__name == trainer_name:
                selected_trainer = aTrainer
                break

        if selected_trainer:
            selected_trainer.assign_class(selected_class)
            selected_class.assign_trainer(selected_trainer)
            print(
                f"Trainer '{selected_trainer._Trainer__name}' has been assigned to '{selected_class.class_name}'."
            )
        else:
            print(f"Trainer '{trainer_name}' not found. Please try again.")
            assignTrainer()
    else:
        print(f"Class '{class_name}' not found. Please try again.")
        assignTrainer()

def manageClass():
    print("\n Manage Group Classes")
    print("1 - Update Class Fee")
    print("2 - Assign a Trainer to a Class ")
    manageChosen = input("\nPlease select a number from the menu: ")
    if manageChosen == "1":
        updateFee()
    elif manageChosen == "2":
        assignTrainer()
    else:
        print("Invalid response, please try again.")
        manageClass()


# Dsiplay menu items for gym management
def dispMainMenu():
    print("\n==== WELCOME TO GYM MANAGEMENT SYSTEM ====")
    print("\n1 - View All Group Classes")
    print("  • Check Enrolled List")
    print("  • Check Wait List")
    print("2 - Add a Class")
    print("3 - Add a Member")
    print("4 - Add a Trainer")
    print("5 - Book a Class")
    print("6 - Cancel a Booking")
    print("7 - Manage Group Classes (update fee/ assign trainer)")
    print("8 - View Member Enrollment")
    print("9 - View Trainer Classes")
    print("10 - View All Members")
    print("11 - Member Check In")
    print("Q - Quit")
    response = input("\nPlease select a number from the menu: ")
    response = response.upper()
    return response


response = dispMainMenu()

while response != "Q":
    if response == "1":
        viewAllClass()
    if response == "2":
        addClass()
    if response == "3":
        addMember()
    if response == "5":
        bookClass()
    if response == "6":
        cancelClass()
    if response == "7":
        manageClass()
    if response == "10":
        viewMember()

    else:
        print("\nInvalid response, please try again.")

    print("")
    input("Press Enter to continue.")
    response = dispMainMenu()

print("Thank you for using the system.")
