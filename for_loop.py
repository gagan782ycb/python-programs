# print sum and avrage of 1 to 5 number 
# i=0
# sum=0
# for sum in range(1,6,1):
#     i=i+sum
# avg=i/5
# print("averag=",avg)    

# writw a program to sum of even number and sum of odd number number is 1 to n 
n=int(input("enter the number"))
sum_evan=sum_odd=0
for i in range(1,n+1):
    if (i%2==0):
        sum_evan+=i
    else :
        sum_odd+=i

print("sum of even number is",sum_evan)
print("sum of odd number is ",sum_odd)
        

