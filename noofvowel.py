#Count the number of vowels in a string.
string = input("enter the string  ")
count =0
li = ['a','A','e','E','I','i','o','O','u','U']
for ch in string:
     if ch in li:
          count+=1
print(count)
if count == 0:
     print("There is no vowel")