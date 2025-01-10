class employee : 
    def __init__(self,name,age,empId,salary):
        self.name = name
        self.age = age
        self.empId = empId
        self.salary = salary

    def out(self):
       print(f"Employee created with name : {self.name}, age {self.age}, ID : {self.empId} and salary {self.salary} \n")

    def detail(self):
        print("Employee Details:")
        print(f"name : {self.name}")
        print(f"age {self.age}")
        print(f"ID : {self.empId}")
        print(f"salary {self.salary}")

class manager(employee) : 
    def __init__(self,name,age,empId,salary,dep):
        self.name = name
        self.age = age
        self.empId = empId
        self.salary = salary
        self.dep = dep

    def out(self):
        print(f"Manager created with name : {self.name}, age {self.age}, ID : {self.empId}, salary {self.salary} and department {self.dep} \n")

    def detail(self):
        print("Manager Details:")
        print(f"name : {self.name}")
        print(f"age {self.age}")
        print(f"ID : {self.empId}")
        print(f"salary {self.salary}")
        print(f"department {self.dep}")


class person(employee) : 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def out(self):
        print(f"Person created with name : {self.name} and age {self.age}\n")

    def detail(self):
        print("Person Details:")
        print(f"name : {self.name}")
        print(f"age {self.age}")


em=None
pr=None
man=None


while True : 
    print("---Employee management system--- \n")
    print("choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit \n")

    choice = int(input("Enter your choice : "))

    if choice == 1 : 
        name = input("Enter Name : ")
        age = input("Enter Age :")

        pr = person(name,age)
        pr.out()
    
    elif choice == 2 :
        name = input("Enter Name : ")
        age = input("Enter Age :")
        empId = input("Enter your EmployeeId(E123) : ")
        salary = input("Enter Salary : ")

        em = employee(name,age,empId,salary)
        em.out()

    elif choice == 3 :
        name = input("Enter Name : ")
        age = input("Enter Age :")
        empId = input("Enter your EmployeeId(E123) : ")
        salary = input("Enter Salary : ")
        department = input("Enter Department : ")

        man = employee(name,age,empId,salary,department)
        man.out()
    
    elif choice == 4:
        print("choose details to show :")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        choose = int(input("Enter your choice : "))

        if choose == 1 :
            if pr is not None :
                pr.detail()
            else:
                print("There is no Person")
        elif choose ==2:
            if em is not None : 
                em.detail()
            else:
                print("There is no Employee")
        elif choose == 3:
            if man is not None :
                man.detail()
            else:
                print("There is no Manager")

    elif choice == 5:
        print("you successfully logged out !")
        break