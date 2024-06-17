# 15. To print Prime numbers in an interval
a, z=map(int,input("Enter the Range ").split())
for num in range(a, z+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            