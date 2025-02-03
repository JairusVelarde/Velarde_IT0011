#scans the input of the user
scan = input("Enter a Phrase: ")
vowel = 0
consonant = 0
space = 0
other = 0
number = 0
#for look to iterate every character in the user input
for char in scan:
    
    #if else to add to corresponding parts
    if char in 'aeiouAEIOU':
        vowel += 1
    elif char == ' ':
        space += 1
    elif char.isalpha():
        consonant += 1
    elif char in '1234567890':
        number += 1
    else:
        other += 1
        
#output
print("Number of Vowels: ",vowel)
print("Number of Consonants: ",consonant)
print("Number of Numbers: ",number)
print("Number of Spaces: ",space)
print("Number of Special Characters: ",other)