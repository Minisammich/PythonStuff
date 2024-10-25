int_1 = int(input('Input first integer: '))
int_2 = int(input('Input second integer: '))

def find_gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < b:
        m = b
        n = a
    else:
        m = a
        n = b
    

    r = m%n

    if r != 0:
        return find_gcd(n,r)
    else:
        return n

print(f"The GCD of {int_1} and {int_2} is",find_gcd(int_1,int_2))