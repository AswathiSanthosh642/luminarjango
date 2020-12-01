size=int(input("enter the size of stack :"))
stack=[]
top=0
flag=0
for i in range(0,size+1):
  if(top>=size):
    print("stack is full")
    flag=1
    break
  else:
     item=int(input("enter element to stack :"))
     stack.append(item)
  top+=1
print(stack)

if flag==1:
 stack.pop()

print(stack)