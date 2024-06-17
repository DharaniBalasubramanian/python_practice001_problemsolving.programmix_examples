# 16. TO FIND FACTORIAL OF A NUMBER
num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("There is no factorial existes for negative numbers")
elif num==0:
    print("The factorial of zero is 1")
elif num>0:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"The factorial of {num} is {factorial}")