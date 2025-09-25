num = int(input("eenter the noof elements: "))
li=[]
print("enter the value: ")
for i in range(num):
    x=int(input())
    li.append(x)
pos=0
for ele in li:
    pos+=1
    count=0
    for j in range(pos,len(li)):
        if ele < li[j]:
            count+=1
    print("no nof elements after ",ele," is ",count)