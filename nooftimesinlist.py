li=[1,2,3,4,14,1,3,2,3,5,9,7,12,3,12]
count = 0
read=[]
for el in li:
    if el not in read:
        count = li.count(el)
        print(el," in the list is ",count," times")
        read.append(el)