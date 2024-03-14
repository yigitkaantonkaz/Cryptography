import math
import random
import warnings

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def results(n,a,b):
    gcd_, x_0, _ = egcd(a,n)
    if b % gcd_ == 0:
        x_p = x_0 * (b // gcd_)
        sol = (x_p % (n // gcd_), n // gcd_)
        solutions = [(sol[0] + k * (n // gcd_)) % n for k in range(gcd_)]
        print(solutions)
    else:
        print("no solution")


n1 = 2163549842134198432168413248765413213216846313201654681321666 
a1 = 790561357610948121359486508174511392048190453149805781203471 
b1 = 789213546531316846789795646513847987986321321489798756453122

n2 = 3213658549865135168979651321658479846132113478463213516854666 
a2 = 789651315469879651321564984635213654984153213216584984653138 
b2 = 798796513213549846121654984652134168796513216854984321354987

n3 = 5465132165884684652134189498513211231584651321849654897498222 
a3 = 654652132165498465231321654946513216854984652132165849651312 
b3 = 987965132135498749652131684984653216587986515149879613516844

n4 = 6285867509106222295001894542787657383846562979010156750642244 
a4 = 798442746309714903987853299207137826650460450190001016593820 
b4 = 263077027284763417836483408268884721142505761791336585685868

results(n1,a1,b1)
results(n2,a2,b2)
results(n3,a3,b3)
results(n4,a4,b4)


