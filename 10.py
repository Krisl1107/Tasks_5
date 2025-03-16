number=int(input())
n_4=number%10
n_3=int((number%100-n_4)/10)
n_2=int((number%1000-n_4-n_3*10)/100)
n_1=number//1000
password_1=str(number)
password_2=list(password_1)
if (len(password_2)==4 and n_1 != n_2 and n_3 != n_4
        and n_1 != n_3 and n_2 != n_3 and n_1 != n_4 and n_4 != n_2) :
    print("OK")
elif number in range(1900,2051):
    print("ERROR")
else:
    print("ERROR")
