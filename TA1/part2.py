nums = input("Input Numbers: ")
total = 0

for char in nums:

 if char in '1234567890':
    total += int(char)

print("Sum of All Numbers: ", total, sep = '')