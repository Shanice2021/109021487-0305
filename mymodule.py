def M2Q9(a,b):
    x=min(a,b)
    while x>0:
        if a%x==0 and b%x==0:    
            print(x)
            break
        else:
            x-=1
    print(int(a*b/x))