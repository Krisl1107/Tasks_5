year=int(input())
if year%4==0 and year%400!=0:
    print(366)
elif year%400==0:
    print(366)
else:
    print(365)
