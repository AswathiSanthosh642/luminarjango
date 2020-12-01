lst=[0,1,2,3,4,5]
check=1
for num in lst:
    if num>0 :
        if num == check:
    if lst.index(num) ==5 :
         print(num +1)
         break
    check += 1
    elif num<check:
 print(num+(check-num))
 break
 elif num>check:
 print(num-(num-check))
 break
