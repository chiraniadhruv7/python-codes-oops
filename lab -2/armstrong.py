for i in range(1,1000):
    sum = 0
    l=i
    while l>0:
        remainder = l%10
        sum = sum + remainder**len(str(i))
        l = l//10
        
    if sum == i:
        print(i)
    
