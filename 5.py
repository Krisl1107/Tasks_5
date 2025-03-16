weight=int(input())
height=int(input())
height_1=(height**2)
i=(weight/height_1)*703
i_1=round(i,2)
if i_1<16:
    print("Выраженный дефицит массы тела")
elif i_1>16 and i_1<18.5:
    print("Недостаточность массы тела")
elif i_1 >=18.5  and i_1 < 25:
    print("Норма")
elif i_1 in range(25,30):
    print("Избыточная масса тела")
elif i_1 in range(30,35):
    print("Ожирение первой степени")
elif i_1 in range(35,40):
    print("Ожирение 2 степени")
else:
    print("Ожирение 3 степени")
