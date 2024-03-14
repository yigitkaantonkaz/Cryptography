# use "pip install sympy" if pyprimes is not installed
# use "pip install pycryptodome" if pycryptodome is not installed
import random
import sympy
import warnings
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHAKE128

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    if a < 0:
        a = a+m
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def random_prime(bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        p = random.randrange(2**(bitsize-1), 2**bitsize-1)
        chck = sympy.isprime(p)
    warnings.simplefilter('default')    
    return p

def large_DL_Prime(q, bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        k = random.randrange(2**(bitsize-1), 2**bitsize-1)
        p = k*q+1
        chck = sympy.isprime(p)
    warnings.simplefilter('default')    
    return p

def Param_Generator(qsize, psize):
    q = random_prime(qsize)
    p = large_DL_Prime(q, psize-qsize)
    tmp = (p-1)//q
    g = 1
    while g == 1:
        alpha = random.randrange(1, p)
        g = pow(alpha, tmp, p)
    return q, p, g

# Generating private-public key pair
def Key_Gen(q, p, g):
    s = random.randint(1, q) # private key
    h = pow(g, s, p)         # public key
    return s, h

# Signature generation
def Sig_Gen(message, a, k, q, p, g):
    shake = SHAKE128.new(message)
    h = int.from_bytes(shake.read(q.bit_length()//8), byteorder='big')
    r = pow(g, k, p)%q
    s = (modinv(k, q)*(h+a*r))%q
    return r, s

# Signature verification
def Sig_Ver(message, r, s, beta, q, p, g):
    shake = SHAKE128.new(message)
    h = int.from_bytes(shake.read(q.bit_length()//8), byteorder='big')
    u1 = (modinv(s, q)*h)%q
    u2 = (modinv(s, q)*r)%q
    v1 = (pow(g, u1, p)*pow(beta, u2, p)%p)%q

    if v1 == r:
        return True
    else:
        return False

"""
# Test
print("Testing the DSA signature generation and verification")
# Generate domain parameters (q, p, g)
q, p, g = Param_Generator(224, 2048)
print("q =", q)
print("p =", p)
print("g =", g)

# Generate private-public key pairs for a user
a, beta = Key_Gen(q, p, g)
print("secret key (a):", a)
print("public key (beta):", beta)

message = b'Hello World!'
k = random.randint(0, q-1)
r, s = Sig_Gen(message, a, k, q, p, g)

if Sig_Ver(message, r, s, beta, q, p, g):
    print("signature verifies:) ")
else:
    print("invalid signature:( ")    
"""

q = 18055003138821854609936213355788036599433881018536150254303463583193
p = 17695224245226022262215550436146815259393962370271749288321196346958913355063757122216400038699125897137338245645654623180907445775397476914326454182331200843039828753210051963838673399537750764519381124074022003533048362953579747694997421932628050174768037008419023891955638333683910783296320068313502467953549845629364328685168055331330378439460107262672207911384029916731040428600795952248385683448339051326373879623024586381484917048530867998300839452185045027743182645996068845915287513974737094311071485279830178802332884322953485032954055698263286829168380561154757985319675247125962424242568733265799534941009
g = 4789073941777232663925946116548512236454007195930716545844255515671921902088454647562920559586402554819251607533026386568443177012595965432651516494873094284671880587043080168709792729580864399522070440013588701427100770785527321717784068531253489015313171638446034805847845720567691412760307220603939165634874434595948570583948951567783902643539632274510317008676675644324152107083325484901562104857644621121348409411557653041824973063215599539520882871449851513387270613400464314879652836352363637833225350963794362275261801894957372518031031893668151623517523940210995342229628030114190419396207343174070379971035
p_b = 1831408160533218510686903726138665932536518466931856989835941853268730468186911958415037229987343935227988816813155415974234360530276380966386586121747340348158553225363319918657949382937198455018294836381584550181800201868806694527418279797492758151769276850910944244395645572497766748854242598561659704665374023326770662512666613356092618904914953512155804252127648818534285831773370510453137952688543495010103660892413395901461238209725480737625047159275781922088076720717434062444236969393756880954396658965471745598003472511293882525516878617801436300794663357187223445935638034452125753926695866508095018852433

m1 = b'The grass is greener where you water it.'
r1 = 16472915699323317294511590995572362079752105364898027834238409547851
s1 = 959205426763570175260878135902895476834517438518783120550400260096

m2 = b'Sometimes you win, sometimes you learn.'
r2 = 14333708891393318283285930560430357966366571869986693261749924458661
s2 = 9968837339052130339793911929029326353764385041005751577854495398266

shake1 = SHAKE128.new(m1)
h1 = int.from_bytes(shake1.read(q.bit_length()//8), byteorder='big')

shake2 = SHAKE128.new(m2)
h2 = int.from_bytes(shake2.read(q.bit_length()//8), byteorder='big')


c_ = 1
while True:
    abs_ = abs(s2 * r1 * c_ - s1 * r2)
    t_ = modinv(abs_, q)
    k_ = (s1 * h2 - s2 * h1 * c_)
    a = (k_ * t_) % q
    if pow(g,a,p) == p_b:
        print("c_: ", c_)
        print("a: ", a)
        break
    else:
        c_ += 1

#Test
s2_inv = modinv(s2, q)
k = (s2_inv * (h2 + a * r1)) % q
print("k: ", k)

r, s = Sig_Gen(m1, a, k, q, p, g)

if Sig_Ver(m1, r, s, p_b, q, p, g):
    print("signature verifies:) ")
else:
    print("invalid signature:( ")  