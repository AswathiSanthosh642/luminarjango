lst = [1,2,3,4,6,7]
i=0
for num in lst:
    for i in range(0,6):
        if((num+lst[i]) == 6):
            print(num,",",lst[i])