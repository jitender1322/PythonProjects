students = []

singleStudent = {"id":"","name":"","age":"","grade":"","date of birth":"","Subject":""}

while True:
    print("Welcome to student data organiser !")

    print("Select an option:")
    print("1. Add a Student")
    print("2. Display all Student")
    print("3. Update Student information")
    print("5. Display subject offerd")
    print("6. Exit")

    choice = input("Enter your choice : ")



    if choice=="1":
        print("Enter student Details : ")
        singleStudent["id"] = input("Student Id : ")
        singleStudent["name"] = input("Name : ")
        singleStudent["age"] = int(input("Age : "))
        singleStudent["grade"] = input("Grade : ")
        singleStudent["date of birth"] = input("DOB : ")
        singleStudent["subject"] = input("Subjects (comma seprated) : ")
        students.append(singleStudent)
        print("Student Added succesfully")
        print("*" * 20)

    elif choice=="2":
        for dict in students :
            print("*" * 30)
            print(f"Student Id : {dict["id"]} || Name : {dict["name"]} || Age : {dict["age"]} || Grade : {dict["grade"]} || Subjects : {dict["subject"]}")
            print("*" * 30)
    
    elif choice=="6":
        print("*" * 30)
        print("Thank you visit again")
        print("*" * 30)
        break
       