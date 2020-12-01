pattern = "A B A B A"
splitters=pattern.split(" ")
print(splitters)
count=0
for j in range(0,len(splitters)):
    for i in range(j+1,len(splitters)):
        if(splitters[j]==splitters[i]):
            count+=1
            if count == 1:
                print("first recursive :", splitters[i])
                break

