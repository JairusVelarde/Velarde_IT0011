#input user information
firstName = input("Enter Your First Name: ")
lastName = input("Enter Your Last Name: ")
age = input("Enter Your Age: ")
contactNumber = input("Enter Your Contact Number: ")
course = input("Enter Course: ")
print("Student Information has been saved to 'students.txt'")

#create file
f = open("D:\TA2\students.txt", "a+")
f.write(f"Reading Student Information...\n\n")
f.write(f"Last Name: {lastName}\n")
f.write(f"First Name: {firstName}\n")
f.write(f"Age: {age}\n")
f.write(f"Contact #: {contactNumber}\n")
f.write(f"Course: {course}\n")
f.close()

#read file
f = open("D:/TA2/students.txt", "r")
info = f.read()
f.close()
