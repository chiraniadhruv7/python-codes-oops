n = int(input("enter no.:"))
l = n
sum = 0

while n>0:
    
    remainder = n%10
    n = n//10
    sum = sum + remainder
    
if(l%sum == 0):
    print("no. is harshad number")
else:
    print("not a harshad number")
