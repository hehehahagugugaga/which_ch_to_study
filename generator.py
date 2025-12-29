import random

print("----------YOUR CODE IS HERE----------")
l = int(input("Enter lower number : "))
u = int(input("Enter upper number : "))
n = int(input("Enter number of chapters you want = "))
op = []
i=0
while i<n:
    j= random.randint(l,u)
    if j not in op:
        op.append(j)
        i+=1
    

print("\nYour chapters are : ",op,"\n")
