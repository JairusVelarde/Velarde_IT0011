#for letter a
#set number of rows
rows = 5

#for loop to loop each row
print("FOR LETTER A")
for i in range(1, rows + 1):
    #print spaces
    for j in range(rows - i):
        print(" ", end= "")
        
    #print numbers   
    for k in range(1, i + 1):
        print(k, end= "")
        
    print()

