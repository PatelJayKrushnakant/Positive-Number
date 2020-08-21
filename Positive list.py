def positive_number(n):
    return n>0
    

list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]

Posnum=list(filter(positive_number,list1))
print(Posnum)
Posnum1=list(filter(positive_number,list2))
print(Posnum1)
