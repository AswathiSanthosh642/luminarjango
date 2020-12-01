lst=[10,9,8,11,12,5,6]

deseout=[]
great=lst[0]
for i in range(0,7):
 for num in lst:
 if(great<num):
 great=num
 deseout.append(great)
 lst.remove(great)
print(deseout)