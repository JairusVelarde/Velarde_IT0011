date = input("Enter a Date (mm/dd/yy): ")        #inputs a date in number format

date = date.replace(" ", "/")                    #prevent error whether the user inputs date using " " or /

month, day, year = date.split("/")               #puts the data in dates as its own variable

months = ["January", "February" , "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #array list of all months

monthName = months[int(month) - 1]               #translates the month number into month name

print(f"Date Input: {monthName} {int(day)}, {int(year)}")