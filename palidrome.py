a = input("enter the no.:")
for i in range(len(a)):
    if(a[i]!=a[len(a)-1-i]):
        print("not a palindrome!")
        break
else:
    print("palindrome")
    
