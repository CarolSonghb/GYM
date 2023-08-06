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


def viewEnrollment():
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
        else:
            print("No enrolled classes found for the member.")
    else:
        print(
            f"This Member ID {member_id} is not found in the system. Please try again."
        )
        viewEnrollment()


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
        trainer_name = input(
            f"Enter full name of the trainer you want to assign '{class_name}' to: "
        )

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
    print("2 - Assign Trainer")
    manageChosen = input("\nPlease select a number from the menu: ")
    if manageChosen == "1":
        updateFee()
    elif manageChosen == "2":
        assignTrainer()
    else:
        print("Invalid response, please try again.")
        manageClass()


def viewTrainerClass():
    trainer_name = input(
        "Enter the trainer's full name to view their assigned classes: "
    )

    selected_trainer = None

    for aTrainer in Trainer._Trainer__trainer_list:
        if aTrainer._Trainer__name == trainer_name:
            selected_trainer = aTrainer
            break
    if selected_trainer:
        trainer_classes = selected_trainer.get_trainer_classes()
        if trainer_classes:
            print(f"The classes assigned to {trainer_name} are: ")
            for aClass in trainer_classes:
                print(aClass.class_name)
        else:
            print("No classes have been assigned to the trainer yet.")
    else:
        print(f"Trainer '{trainer_name}' not found. Please try again.")
        viewTrainerClass()


def memberCheckIn():
    member_id = input("Enter your member ID: ")
    selected_member = None
    for aMember in Member._Member__member_list:
        if str(aMember._Member__member_id) == member_id:
            selected_member = aMember
            break

    if selected_member:
        enrolled_classes = selected_member.get_enrolled_check()
        if enrolled_classes:
            print("You are enrolled in the following classes:")
            for idx, class_name in enumerate(enrolled_classes, start=1):
                print(f"{idx}. {class_name}")

            while True:
                try:
                    choice = int(input("\nEnter the number of the class to check in: "))

                    if choice == 0:
                        break

                    elif 1 <= choice <= len(enrolled_classes):
                        selected_class_name = enrolled_classes[choice - 1]
                        selected_class = checkClass(selected_class_name)

                        if selected_class:
                            result = selected_class.check_in_member(selected_member)
                            print(result)
                            break
                        else:
                            print("Selected class not found.")
                            break
                    else:
                        print("Invalid choice. Please choose from the number below.")
                except ValueError:
                    print("Invalid input. Please enter a number from the list.")
        else:
            print("You are not enrolled in any classes.")
    else:
        print(f"This Member ID {member_id} is not found in the system.")


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
    print("7 - Manage Group Classes")
    print("  • Update Class Fee")
    print("  • Assign Trainer")
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
    if response == "8":
        viewEnrollment()
    if response == "9":
        viewTrainerClass()
    if response == "10":
        viewMember()
    if response == "11":
        memberCheckIn()

    else:
        print("\nInvalid response, please try again.")

    print("")
    input("Press Enter to continue.")
    response = dispMainMenu()

print("\nThank you for using the system.")
print("")
