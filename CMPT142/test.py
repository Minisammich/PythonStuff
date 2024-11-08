def f(x):
    return((x**3)-(2*x)-5)

def fp(x):
    return(3*(x**2)-2)

x1 = 2
for i in range(5):
    print(f(x1))
    x2 = x1-(f(x1)/fp(x1))
    x1 = x2