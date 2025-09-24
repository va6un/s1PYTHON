num=int(input("enter the noopf elements: "))
li=[]
for e in range(num):
    x=int(input("enter value: "))
    li.append(x)
print("the enter ed list : ",li)
print("list with no duplicate: ",list(set(li)))