number=int(input())
n_1=number%10
n_2=(number%100-n_1)/10
n_3=(number%1000-n_1-n_2*10)/100
n_4=number//1000
n_rvrs=n_1*1000+n_2*100+n_3*10+n_4
if number==n_rvrs:
    print("Настоящее")
else:
    print("Кривое")
