import sys
import mymodule as mm
# 最大公因數與最小公倍數
a=int(sys.argv[1]) #M2Q9
b=int(sys.argv[2]) #M2Q9
print(mm.M2Q9(a,b))

# 反向字串
a=str(sys.argv[1]) #M3Q1
print(mm.M3Q1(a))

# 數字矩陣
a=int(sys.argv[1]) #M3Q4
b=int(sys.argv[2]) #M3Q4
print(mm.M3Q4(a,b))

#C(m,n)
a=int(sys.argv[1]) #M3Q5
b=int(sys.argv[2]) #M3Q5
print(mm.M3Q5(a,b))

#亂數選號程式
a=int(sys.argv[1]) #M3Q2
print(mm.M3Q2(a))

#數字拆解方法
a=list(sys.argv[1]) #M3Q6
print(mm.M3Q6(a))
