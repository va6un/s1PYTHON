li=[1,2,6,5,77,4,88,96,12,33,61,35,64]
found= 0
count =0
key=int(input("enter the elment to search: "))
for el in li:
    count+=1
    if key == el:
        print("element found!! at ",count)
        found=1
if found==0:
    print("element not in the list!!")
print(li)