# Student Name: Carol (Haibei) Song
# Student ID: 1154836

# Notes:
# A menu will be displayed in the terminal when you run the programm
# Please select the numbers to test the functions
# *******************************************************
# This programm has used prettytable library for better display
# Please install using "pip install prettytable" 
# ********************************************************

# What you can do:
# You can create a new class, a new member and a new trainer
# and so much more
from GroupExercise import *
from Member import *
from Trainer import *
# pip install prettytable  (if need to)
from prettytable import PrettyTable

# The required functionalities are as follows:
# 1. Create 2 GroupExercise objects
class1 = GroupExercise("Zumba", 2, 0.0)
class2 = GroupExercise("Pilates", 4, 0.0)

# Create 5 Member objects
member1 = Member.new_member("Alice Wonderland")
member2 = Member.new_member("Kenneth Duncan")
member3 = Member.new_member("Barbie Brown")
member4 = Member.new_member("Adam Curtin")
member5 = Member.new_member("Carol Song")

# Create 2 Trainer objects
trainer1 = Trainer("Jane Doe", "Aerobic Exercise")
trainer2 = Trainer("Will Smith", "Injury Prevention")

# Assign a trainer to each group exercise class

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

# Displays all gym members currently enrolled in the class
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

# Display the waiting list for a class
def viewWaitlist():
    class_name = input("Enter the class name to check its waitlist: ")

    selected_class = checkClass(class_name)

    if selected_class:
        waitlist_members = selected_class.get_waitist()
        if waitlist_members:
            print(f"\nWaitlisted members for class '{class_name}' are:")
            for aMember in waitlist_members:
                print(aMember)
        else:
            print("No member has enrolled in this class.")
    else:
        print(f"Class '{class_name}' not found. Please try again.")
        viewClass()

# Display all classes, then you can choose to view the enrolled list or the waitlist
# for the class that you choose
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

def addTrainer():
    print("\nAdding a New Trainer")
    firstName = input("Enter trainer's first name: ")
    lastName = input("Enter trainer's last name: ")
    expertise = input("Enter trainer's expertise: ")
    name = firstName + " " + lastName
    new_trainer = Trainer(name, expertise)
    print(f"A new trainer '{new_trainer.trainer_name}' with expertise '{new_trainer.expertise}' has been added.")

# View a list of current members
def viewMember():
    print("")
    print("========== Member List ==========")
    print("")
    print(f"MemberID{'':<8}Name")
    # Access the member_list using the class name
    for aMember in Member._Member__member_list:
        print(aMember)

# Enrols a gym member into the group exercise class.
# If the class is full, the member will be added to the waitlist.
def bookClass():
    viewClass()
    book_class = input("Enter the name of the class you want to book: ")

    selected_class = checkClass(book_class)

    if selected_class:
        member_id = input("Enter your member ID: ")
        # check if the member ID exists in the system
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

# Display the list of enrolled participants for a class
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

# Cancelling a specific member's group class
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
            selected_class = None
            for aClass in GroupExercise._GroupExercise__class_list:
                if aClass.class_name == class_to_cancel:
                    selected_class = aClass
                    break
            if selected_class:
                cancel_result = selected_class.member_cancel(selected_member)
                print(cancel_result)
            else:
                print(f"Class '{class_to_cancel}' not found.")
        else:
            print("No enrolled classes found for the member.")
    else:
        print(f"This Member ID {member_id} is not found in the system")

# set a new fee to a class and update it
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

# View all trainers
def viewTrainers():
    print("\n========== List of Trainers ==========")
    print(f"\n{'Trainer Name':<20}Expertise")
    print("---------------------------------------")

    for aTrainer in Trainer._Trainer__trainer_list:
        print(f"{aTrainer._Trainer__name:<20}{aTrainer._Trainer__expertise}")

    print("\n=======================================")

# Assign a trainer to a class
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

# Display a sub menu
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

# Display the list of classes offered by a particular trainer
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

# Mark a gym member's attendance for the class
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

# Class report includes the following information:
# class name, max capacity, fee and avaliable spots
# enrolled number, waitlisted number, number of attendees and attendance percentage
# and total payment received for a group class
def classReport():
    print("\n*** Class Report ***")
    # Create the table with the desired column headers
    table = PrettyTable()
    table.field_names = [
        "Class_Name",
        "Max_Capacity",
        "Fee",
        "Avai_Slots",
        "Trainer",
        "Enrolled",
        "Waitlist",
        "Total_Payment",
        "Attended",
        "Attendance",
    ]

    # Access the class_list using the class name
    for aClass in GroupExercise._GroupExercise__class_list:
        table.add_row(
            [
                aClass.class_name,
                aClass.class_capacity,
                f"${aClass.class_fee:.2f}",  # Format the fee with 2 decimal places
                aClass.get_available_slot(),
                aClass.get_trainer(),
                aClass.get_enrolled_number(),
                aClass.get_waitlist_number(),
                aClass.total_payment(),
                aClass.get_attendees_number(),
                f"{aClass.get_attendance_percentage():.2f}%",  # Format percentage with 2 decimal places
            ]
        )


    print(table)


# Dsiplay menu items for gym management
def dispMainMenu():
    print("\n==== WELCOME TO GYM MANAGEMENT SYSTEM ====")
    print("\n1 - View All Group Classes")
    print("    • Check Enrolled List")
    print("    • Check Wait List")
    print("2 - Add a Class")
    print("3 - Add a Member")
    print("4 - Add a Trainer")
    print("5 - Book a Class")
    print("6 - Cancel a Booking")
    print("7 - Manage Group Classes")
    print("    • Update Class Fee")
    print("    • Assign Trainer")
    print("8 - View Member Enrollment")
    print("9 - View Trainer Classes")
    print("10 - View All Members")
    print("11 - Member Check In")
    print("12 - View Class Report")
    print("Q - Quit")
    response = input("\nPlease select a number from the menu: ")
    response = response.upper()
    return response

if __name__ == "__main__":
response = dispMainMenu()

while response != "Q":
    if response == "1":
        viewAllClass()
    elif response == "2":
        addClass()
    elif response == "3":
        addMember()
    elif response == "4":
        addTrainer()
    elif response == "5":
        bookClass()
    elif response == "6":
        cancelClass()
    elif response == "7":
        manageClass()
    elif response == "8":
        viewEnrollment()
    elif response == "9":
        viewTrainerClass()
    elif response == "10":
        viewMember()
    elif response == "11":
        memberCheckIn()
    elif response == "12":
        classReport()

    else:
        print("\nInvalid response, please try again.")

    print("")
    input("Press Enter to continue.")
    response = dispMainMenu()

print("\nThank you for using the system.")
print("")
