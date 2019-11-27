#lambda表达式
f = lambda a,b,c,:a+b+c
print(f)

print(f(2,3,4))

g = [lambda a:a*2,lambda b:b*3]
print(g[1](5))

