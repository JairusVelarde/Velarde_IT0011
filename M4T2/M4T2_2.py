
dollar = float(input("How much dollar do you have?"))

print("What currency you want to have?", end=" ")
currency = input().upper()

#opens file and reads it
with open('D:\currency.csv', 'r', encoding='latin1') as file:
    lines = file.readlines()
    
    #finding currency to convert
    for line in lines[1:]:
        data = line.strip().split(',')
        if data[0] == currency:
            rate = float(data[2])
            result = dollar * rate
            print("Dollar: $",dollar, sep='')
            print(f"{data[1]}: {result}")
            break
    else:
        print("Currency not found.")
