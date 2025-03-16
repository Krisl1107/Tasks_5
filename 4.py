q_prt=int(input())
if q_prt>10 and q_prt//10!=1:
 last_nmbr=q_prt%10
elif q_prt==100:
 last_nmbr=0
elif q_prt//10==1:
 last_nmbr=0
else:
    last_nmbr = q_prt

if last_nmbr==0 or last_nmbr in range(5,10):
    print(q_prt, "попугаев")
elif last_nmbr==1:
    print(q_prt, "попугай")
else:
    print(q_prt, "попугая")
