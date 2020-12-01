lst=[120,11,12,13,14]
n=int(input("enter the number to search :"))
flag=0
for num in lst:
 if n==num:
 flag=1
print(flag)
if flag==1:
 print("element",n ,"is found")
else :
 print("element not found")