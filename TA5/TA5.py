class operations:
    def divide(num1,num2):
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Second Number must not be equal to 0!")
            
    def exponentiation(num1,num2):
        print(pow(num1,num2))
    
    def remainder(num1,num2):
        if num2 != 0:
            print(num1 % num2)
        else:
            print("Second Number must not be equal to 0!")
    
    def summation(num1,num2):
    
     if num1 > num2:
        print("Num1 must be less than Num2.")
     else:
        total = 0
        while num1 <= num2:
            total += num1
            num1 += 1
        print(total)
            
        

print("==== MAIN MENU ====")
print("Operations Available:")
print()
print("1. Division")
print("2. Exponent")
print("3. Remainder")
print("4. Summation")
print()
print("== Press 5 to Exit ==")

opt = 0 
while opt != 5:
 opt = int(input("Choose an Option [1-5]: "))


 if opt == 1:
    print("You have chosen division.")
    n1 = int(input("Input first number: "))
    n2 = int(input("Input second number: "))
    operations.divide(n1,n2)
 elif opt == 2:
    print("You have chosen exponentiation.")
    n1 = int(input("Input first number: "))
    n2 = int(input("Input second number: "))
    operations.exponentiation(n1,n2)
 elif opt == 3:
    print("You have chosen remainder.")
    n1 = int(input("Input first number: "))
    n2 = int(input("Input second number: "))
    operations.remainder(n1,n2)
 elif opt == 4:
    print("You have chosen summation.")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    operations.summation(n1,n2)
else:
    print("Exiting program...")




        
        
