a = int(input("enter the no.:"))
for i in range(2,a):
    if(a%i==0):
        print("the no. is not prime")
        break
else:
        print("prime")