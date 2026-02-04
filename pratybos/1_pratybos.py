##i = 0
##while i < 10:
##    print(i)
####    if i == 5:
####        break
##    i += 1
##else:
##    print("Ciklas baigėsi")

#import random
#a = [random.randint(1,10) for i in range(10)]
#print(a)
#
#b = []
#for i in range(10):
#    b.append(random.randint(1, 10))
#print(b)
#
# import random
# c = [random.randint(1,10) for i in range(10) if i%3==0]
# print(c)
# #
# #print(a[::2])
# #
# c[1:2] = [0, 0, 0]
# print(c)
#
# print(c[2:969])


# def f(x, y = 5, *args, **kwargs):
#    print(x)
#    print(y)
#    print(args)
#    print(kwargs)
#
# print(f(1, 2, 3, 4, 5, 6))
# print(f(1, 2, [3, 4, 5, 6]))
# print(f(1, 2, *[3, 4, 5, 6]))
# print(f(1, 2, z=7, q=8))
# print(f(1, 2, **{'z':7, 'q':8}))

x = 5
# def f():
#    a = x
#    print(a)
# def f():
#    x = x
#    print(x)
# def f():
#    global x
#    x = 9
#
# f()
# print(x)

##import math
####print(dir(math))
##print(math.pi)

##from math import *
##print(pi)
##sin = 5
##print(sin(pi))

f = open('data.txt', 'w')
f.write('Šiandien graži diena')
f.close()
f = open('data.txt', 'rb')
for e in f:
   print(e)
print(f.tell())
f.close()
