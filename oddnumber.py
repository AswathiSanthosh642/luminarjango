low = 2

upper = 10
sum =0
while(low<=upper):
    if(low%2!=0):
        odd=low
        sum+=odd
    low+=1
print(sum)