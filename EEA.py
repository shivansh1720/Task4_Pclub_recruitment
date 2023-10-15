import sys


def gcd(x,y):
    if x>y:
        if x%y==0:
            return y
        else:
            return gcd(y,x%y)
    else:
        return gcd(y,x)
    
def multiplicative_inverse(x,y,t0,t1):
    r=x%y
    q=int(x/y)
    t=t0-q*t1 
#    if(t<0):
 #       t=t+y
    if(r==0):
        return(t1)
    else: return multiplicative_inverse(y,r,t1,t)

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Multiplicative inverse does not exist")
    else:
        return x % m

n = 5  # Replace with your modulus 'n'
a = 187

inverse = mod_inverse(a, n)
print(f"The multiplicative inverse of {a} modulo {n} is {inverse}")

    
x=26513
y=32321

print(multiplicative_inverse(13,3,0,1))