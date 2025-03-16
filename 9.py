b_1,b_2,b_3=map(int,input().split())
if b_1>b_2>b_3:
    print(b_1,b_2,b_3)
elif b_1>b_3>b_2:
    print(b_1,b_3,b_2)
elif b_2>b_3>b_1:
    print(b_2,b_3,b_1)
elif b_2>b_1>b_3:
    print(b_2,b_1,b_3)
elif b_3 > b_1>b_2:
    print(b_3, b_1, b_2)
else:
    print(b_3,b_2,b_1)
