#Check whether a string is a palindrome.

string = input("enter the string: ")
if string == string[::-1]:
    print("palindrome  ")
else:
    print("not palindrome !!")