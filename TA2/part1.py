#input user information
firstName = input("Enter Your First Name: ")
lastName = input("Enter Your Last Name: ")
fullName = firstName + ' ' + lastName
age = input("Enter Your Age: ")
print(' ')
#slices the first name to 3 characters only
slicedName = firstName[0:3]

print('Full Name: ', fullName, sep = '')
print("Sliced Name: ", slicedName, sep = '')
print('Greeting Message: Hello ',slicedName, ', Welcome! You are ', age, ' years old.', sep='')

