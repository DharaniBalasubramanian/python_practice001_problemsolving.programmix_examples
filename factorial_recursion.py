# TO FIND FACTORIAL USING RECURSION
def recursion_factorial(x):
    if x<0:
        return "wrong data"
    elif x==0 or x==1:
        return 1
    else:
        return x*recursion_factorial(x-1)


x=int(input("Enter a number: "))
print(recursion_factorial(x))

