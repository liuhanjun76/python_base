
from math import sqrt
for i in range(2,10):
    flag=1
    k=int(sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            flag=0
        break
        if(flag):
            print(i)
    print(k)
            
