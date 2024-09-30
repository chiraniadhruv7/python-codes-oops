l = [2,3,4,5]
a = list(map(lambda base,index: base**index,l,range(len(l))))
print(a)