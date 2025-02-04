#input user information
firstName = input("Enter Your First Name: ")
lastName = input("Enter Your Last Name: ")
fullName = firstName + ' ' + lastName

#print out information
print('Full Name: ', fullName, sep = '')
print('Full Name (UPPER CASE): ', (fullName.upper()) , sep = '')
print('Full Name (lower case): ', (fullName.lower()) , sep = '')

print("Length of Full Name: ", len(firstName + lastName))