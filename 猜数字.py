import random
a = random.randint(1,10000)
#n=False
f = 25
while f:
    b=int(input())
    if b==a:
        print("正确")
        #n=True
        break
    elif b>a:
        print("偏大")
    else:
        print("偏小")
        f=f-1
        if f==0:
            print("次数已用完")