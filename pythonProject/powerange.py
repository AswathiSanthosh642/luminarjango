nnum= 0
num = int(input("please enter a number"))
sum=0
i=1

while(i<=num): #1<=2
    nnum = (nnum*10)+num
    print("new num:",nnum)
    sum=sum+nnum
    i+=1
print("sum=",sum)