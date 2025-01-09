students = []

while True:
    print("Welcome to student data organiser!")
    print("Select an option:")
    print("1. Add a Student")
    print("2. Display all Students")
    print("3. Update Student information")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Enter student details:")
        singleStudent = {
            "id": input("Student Id: "),
            "name": input("Name: "),
            "age": int(input("Age: ")),
            "grade": input("Grade: "),
            "date of birth": input("DOB: "),
            "subject": set(input("Subjects (comma-separated): ").split(","))
        }
        students.append(singleStudent)
        print("Student added successfully!")
        print("*" * 20)

    elif choice == "2":
        if not students:
            print("No students available!")
        else:
            for student in students:
                print("*" * 30)
                print(f"Student Id: {student['id']} || Name: {student['name']} || Age: {student['age']} || Grade: {student['grade']} || Subjects: {', '.join(student['subject'])}")
                print("*" * 30)

    elif choice == "3":
        id = input("Enter student id: ")
        for user in students:
            if user["id"] == id:
                print(f"Student found, name: {user['name']}")
                user['age'] = int(input("Enter new age: "))
                user['subject'] = set(input("Enter new subjects (comma-separated): ").split(","))
                print("Student updated successfully!")
                break
        else:
            print("Student ID not found!")

    elif choice == "4":
        id = input("Enter student id: ")
        for user in students:
            if user["id"] == id:
                print(f"Student found, name: {user['name']}")
                students.remove(user)
                print("Student deleted successfully!")
                break
        else:
            print("Student ID not found!")

    elif choice == "5":
        print("*" * 30)
        print("Thank you! Visit again.")
        print("*" * 30)
        break

    else:
        print("Invalid choice! Please try again.")
