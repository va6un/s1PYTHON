#Find the sum of digits of a number.
num = int(input("enter the digit: "))
sum=0
while(num!=0):
    sum = sum+(num%10)
    num//=10
print("sum of digit ",sum)