num=int(input("enter a limit"))
lst=[]
even=[]
odd=[]
for i in range(1,(num+1)):
    lst.append(i)
for n in lst:
    if(n%2==0):
        even.append(n)
    else:
        odd.append(n)
print(lst)
print(odd)
print(even)