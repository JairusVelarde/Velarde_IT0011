students = []

#create menu
opt = 0
while opt !=9:
    print("=== MAIN MENU ===")
    print("1. Open File")
    print("2. Save File")
    print("3. Save as File")
    print("4. Show All Student Records")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")
    
    opt = int(input("Enter Option: "))
    if opt == 1:
        print("=== Open File ===")
        file = open("students.txt", "w+")
        data = file.readlines()
        students = [eval(line.strip()) for line in data]
        print("File opened successfully.")
        for student in students:
            print(f"Name: {student[1][0]} {student[1][1]}")
            print(f"Student ID: {student[0]}")
            print(f"Class Standing: {student[2]}")
            print(f"Major Exam: {student[3]}")
            print(f"Final Grade: {student[4]:.2f}")
        file.close()

    elif opt == 2:
        with open("students.txt", "w") as file:
            for s in students:
                file.write(str(s) + "\n")
        print("File saved successfully")
    elif opt == 3:
        filename = input("Enter filename to save as: ")
        with open(filename, "w") as file:
            for s in students:
                file.write(str(s) + "\n")
        print(f"File saved as {filename} successfully.")
    elif opt == 4:
        print("=== Student Records ===")
        sorted_students = sorted(students, key=lambda x: x[4], reverse=True)
        for student in sorted_students:
            print(f"Name: {student[1][0]} {student[1][1]}")
            print(f"Student ID: {student[0]}")
            print(f"Class Standing: {student[2]}")
            print(f"Major Exam: {student[3]}")
            print(f"Final Grade: {student[4]:.2f}")
            print("")
    elif opt == 5:
        print("=== Student Record ===")
        searchID = input("Enter ID Number of Student: ")
        
        for student in students:                                            # for loop that searches if the ID number exists in the records                  
            if student[0] == searchID:                 
                print(f"Name: {student[1][0]} {student[1][1]}")
                print(f"Student ID: {student[0]}")
                print(f"Class Standing: {student[2]}")
                print(f"Major Exam: {student[3]}")
                print(f"Final Grade: {student[4]:.2f}")
                print("")
                break
            else:
                print("Student not found.")
    elif opt == 6:
        print("=== Add Student Record ===")
        idNum = input("Enter 6 Digit ID Number: ")
        idCount = len(idNum)
        if idCount != 6:                                                     #checks if id number has 6 digits
            print("ID number should have 6 Digits. Please try again.")
        else:
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            classStanding = int(input("Enter Class Standing: "))
            majorExam = int(input("Enter Major Exam Grade: "))
            studGrade = ((classStanding * 0.60) + (majorExam * 0.40))
            
            students.append((idNum, (firstName, lastName), classStanding, majorExam,studGrade))
            print("Student record successfully added.")
    elif opt == 7:
        print("=== Edit Student Record ===") 
        searchID = input("Enter ID Number of Student: ")
        
        # for loop that searches if the ID number exists in the records
        for i in range(len(students)):
            if students[i][0] == searchID:
                firstName = input("Enter First Name: ")
                lastName = input("Enter Last Name: ")
                classStanding = int(input("Enter Class Standing: "))
                majorExam = int(input("Enter Major Exam Grade: "))
                studGrade = ((classStanding * 0.60) + (majorExam * 0.40))
            
                students[i]=(searchID, (firstName, lastName), classStanding, majorExam, studGrade)
                print("Student record successfully updated.")
                break
            else:
                print("Student not Found.")
    
    elif opt == 8:
        print("=== Delete Record ===")
        searchID = input("Enter ID Number of Student: ")
        # for loop that searches if the ID number exists in the records
        for i in range(len(students)):
             if students[i][0] == searchID:
                 del students[i]
                 print("Student record deleted successfully.")
                 break
             else:
                 print("Student not Found.")
    else:
        print("Exiting Program...")