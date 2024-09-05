n=int(input("enter the number" ))
sum_even=sum_odd=0
for i in range (1,n+1):
    if(i%2==0):
        sum_even+=i
    else:
        sum_odd+=i
print("sum of even number=",sum_even)
print("sum of odd number=",sum_odd)