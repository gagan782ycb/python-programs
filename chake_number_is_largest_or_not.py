A=int(input("enter a number"))
B=int(input("enter a number"))
C=int(input("enter a number"))
if(A>B):
    if(A>C):
        print(A,"is largest number")
    else:
      print(C," is largest number")
else:
    if(B>C):
        print(B,"is largest number")
    else:
        print(C,"is largest number")