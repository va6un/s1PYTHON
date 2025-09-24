sen= input("enter the sentence: ")
sen= sen.lower().replace(" ","")
if(sen == sen[::-1]):
    print("palindrome  ")
else:
    print("not palindrome!")