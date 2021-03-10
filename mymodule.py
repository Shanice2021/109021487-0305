#最大公因數與最小公倍數
def M2Q9(a,b):
    x=min(a,b)
    while x>0:
        if a%x==0 and b%x==0:    
            print(x)
            break
        else:
            x-=1
    print(int(a*b/x))

#反向字串
def M3Q1(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i],end="")
    print()

# 數字矩陣
def M3Q4(x,y):
    for y in range(1,y+1):
        for x in range(1,x+1):
            print("{}\t".format(x*y),end="")
        print()

#C(m,n)
def M3Q5(m,n):
    def f(x):
        y=1
        for i in range(x,1,-1):
            y*=i
        return y
    print(f(m)/f(n)/f(m-n))

#亂數選號程式
def M3Q2(a):
    import random
    random.seed(a)
    data=[0]*6
    i=0
    while i<6:
        x=random.randint(1,43)
        flag=True
        j=0
        while j<i and flag:
            if data[j]==x:
                flag=False
            else:
                j+=1
        if flag:
            data[i]=x
            i+=1
    for i in data:
        print(i,end="\t")
    print()

#數字拆解方法
def M3Q6(data):
    for i in data:
        print("{} ".format(i),end="")
    print()