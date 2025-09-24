while(True):
    print("1.And \n2.OR\n3.NOT\n4.NAND\n5.XOR\n6.Exit")
    ch =int(input("enter the choise "))
    if(ch==1):
      a=int(input("enter first number: "))
      b=int(input("enter the second number: "))
      c= a and b
      print(" result : ",c)
    elif (ch ==2):
      a=int(input("enter first number: "))
      b=int(input("enter the second number: "))
      c= a or b
      print(" result : ",c)
    elif ch==3:
      b=int(input("enter the  number: "))
      c= not b
      print(" result : ",c)
    elif ch==4:
      a=int(input("enter first number: "))
      b=int(input("enter the second number: "))
      c=not(a and b)
      print(c)
    elif ch ==5:
      a=int(input("enter first number: "))
      b=int(input("enter the second number: "))
      c=bool(a^b)
      print(c)
    elif ch==6:
       print("Exiting ....")
       break
    else:
      print("enter valid input!!")