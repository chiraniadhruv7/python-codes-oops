n = int(input("enter no.:"))
l = n
sum = 0
a = len(str(n))
while n>0:
    
    remainder = n%10
    n = n//10
    sum = sum + remainder**a
    a=a-1
if(sum == l):
    print("no. is disarium number")
else:
    print("not a disarium number")
