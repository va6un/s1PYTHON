#Check whether a year is a leap year.

year = int(input("enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year !")
else:
    print("not leap year!!")