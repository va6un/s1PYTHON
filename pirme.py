#Write a function to check whether a given number is prime or not.
import math
def isPrime(val):
    if(val <= 1):
        print("not prime !")
        return False
    for i in range(2 , int(math.sqrt(val))+1):
        if val % i==0:
            return False
    return True

num =int(input("enter the number: "))
if(isPrime(num)):
    print("prime number!! ")
else:
    print("not prime number!!")
