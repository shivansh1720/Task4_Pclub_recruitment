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
    
def chinese_remainder(list1,list2,list3,M):
    x=0;
    for a,b,c in zip(list1,list2,list3):
        x=x+a*M*c/b
    return x%M

list1 = [2,3,5]
list2 = [5,11,17]
M=1
for i in list2:
    M=M*i
list3=[]
for i in range(len(list1)):
    list3.append(mod_inverse(M/list2[i],list2[i]))
for i in list3:
    print(i)

print(chinese_remainder(list1,list2,list3,M))