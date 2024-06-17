# 12. TO CHECK THE LEAP YEAR
y=int(input("Enter the year: "))
if y%4==0:
    print("Leap year")
elif y%4!=0:
    print("Normal year")