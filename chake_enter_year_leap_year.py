year=int(input("enter year "))
if(year%400==0 & year%100==0):
         print(year,"is a leap year")
elif(year%4==0&year%100 ==0):
    print(year,"is a leap year")
else:
    print(year,"is a not leap year")