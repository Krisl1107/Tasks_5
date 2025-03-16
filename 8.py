n=int(input())
gl=n//(17*29)
sk=(n-17*29*gl)//17
kn=(n-17*29*gl)%17
if sk==0:
    print(gl,"галлеонов",kn, "кнатов")
elif gl==0:
    print(sk, "скилей", kn, "кнатов")
elif kn==0:
    print(gl, "галлеонов", sk, "скилей")
else:
    print(gl, "галлеонов", sk, "скилей", kn, "кнатов")
