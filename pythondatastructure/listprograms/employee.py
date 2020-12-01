employees=[[1001,"ajay","qa",15000],
           [1002,"vijay","developer",25000],
           [1003,"arun","ba",15000]]
for emplo in employees:
    print(emplo[0])

total=0
for emplo in employees:
    total+=emplo[3]
print(total)


count=0
for emplo in employees:
    if emplo[2]=="developer":
        count+=1
print("number of developers",count)


basal=0
devsal=0

qasal=0

for emplo in employees:
    if emplo[2]=="developer":
        devsal+=emplo[3]
    if emplo[2]=="qa":
        qasal+=emplo[3]
    if emplo[2]=="ba":
        basal+=emplo[3]
print("devsal",devsal,"qasal",qasal,"basal",basal)