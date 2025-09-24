#Implement a menu driven program to accept two integers and do a logical operation. Menu should have minimum of 4 logical operations
print("1.AND\n2.OR\n4.NOT")

choice= int(input("enter the choice: "))
while(choice!=0):
    if(choice==1):
        print("enter two numbers: ")
        a=int(input())
        b=int(input())
        c=a and b
        print(c)
        break