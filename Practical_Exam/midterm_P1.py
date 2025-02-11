f = open(r"D:/numbers.txt", "r+")   #opens numbers.txt file
lineNum = 0                         #tracks line num.


for line in f:                                                  #iterate each line
    line = line.strip()                                         #removes unneccesary spaces
    nums = [int(num) for num in line.split(",") if num]         #makes the list int data type
    numSum = sum(nums)                                          #adds each line
    
    if not line:                                                #check if the line is empty
        continue
    
    if str(numSum) == str(numSum)[:: -1]:
        print(f"Line {lineNum+1}: {nums} with sum {numSum} is a Palindrome")
        lineNum += 1
    else:
        print(f"Line {lineNum+1}: {nums} with sum {numSum} is not a Palindrome")
        lineNum += 1
f.close()  
