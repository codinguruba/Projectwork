from Student import StudentManager

s1 = StudentManager()

print("|----------------------------------------|")
print("|Welcome to my student management project|")
print("|       Press a to add student           |")
print("|       Press r to read student          |")
print("|       Press d to delete student        |")
print("|       Press q to quit the program      |")
print("|----------------------------------------|")

running = True

while(running):

    choice = input("Enter a choice:")

    if(choice == "a"):
        id = int(input("Enter id:"))
        name = input("Enter a name:")
        age = int(input("Enter age:"))
        s1.add_student(id,name,age)

    elif(choice == "r"):
        s1.read_student()

    elif(choice == "d"):
        id = int(input("Enter the student id you want to delete?:"))
        s1.delete_student(id)

    elif(choice == "q"):
        break

    else:
        print("Invalid choice")
        




