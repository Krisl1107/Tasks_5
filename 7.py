N,K,M=map(int,input().split())
if K<M:
    print(M-K-1)
else:
    print(N-(K-M)-1)
