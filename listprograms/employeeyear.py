employees=[[1001,"ajay","qa",1981,2003],
 [1002,"vijay","developer",1992,2008],
 [1003,"arun","ba",1989,2010],
 [1004,"amal","developer",2009,2014],
 [1005,"vimal","developer",1987,1989]]

# print all employee designation
print("---------all employee designation----------")
for emplo in employees:
    print(emplo[2])
# print all employe whose designation =developer
print("---------all employee details whose designation = developer----------")
for emplo in employees:
    if emplo[2]=="developer":
        print(emplo)

# print all employees those who are working in 1980's
print("---------all employee details who are worked in 1980's----------")
for emplo in employees:
    if ((emplo[3]>=1980)&(emplo[4]<1990)):
        print(emplo)

# print all employee details whose experience >9years
print("---------all employee details whose experience >9 years----------")
for emplo in employees:
    if (emplo[4]-emplo[3]) > 9:
        print(emplo)
