# use "pip install sympy" if sympy is not installed
import random
import sympy
import warnings

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

# Encryption
def Enc(message, h, q, p, g): # m is the message
    m = int.from_bytes(message, byteorder='big')
    k = random.randint(1, 2**16-1)
    r = pow(g, k, p)
    t = (pow(h, k, p)*m)%p
    return r, t

# Decryption
def Dec(r, t, s, q, p, g):
    m = (pow(r, q-s, p)*t)%p
    return m.to_bytes((m.bit_length()+7)//8, byteorder='big')

"""
# Test
print("Testing the ElGamal Encryption and Decryption")
# Generate domain parameters (q, p, g)
q, p, g = Param_Generator(160, 1024)
print("q =", q)
print("p =", p)
print("g =", g)

# Generate private-public key pairs for a user
s, h = Key_Gen(q, p, g)
print("secret key (s):", s)
print("public key (h):", h)

# Encrypt a random message
message = b'Hello World!'
r, t = Enc(message, h, q, p, g)
print("ciphertext (r, t):", r, t)

# Decrypt the ciphertext
print("\nDecrpyted message:", Dec(r, t, s, q, p, g))
"""

q = 1445431254694174381649371259143791311198736690037
p = 137248121434045436247980738953059412416367251619167172965225060439638326312552007992983578734870080149141102688002009860722627928048376753275218309927198296531391131491381377746970705292972549293385978940242862964757496679733959578043293370426396437630135799843979374589693726945392682404824784160383287430661
g = 127223641921850109909544249881449009944648689040286349526712184078921702602665543540563817762837809423359475544561229778960073396175252439333049143438367080170746166373310913545533812707513022571241268299810387846306038162098727078834162806032355796383642287190219288720676739470587659262303423658215573377024

m1 = b'Believe in the heart of the cards.'
r1 = 98112636909089823473886804230734608783665151359820285384385184926586779318832342840446756845270685151843520592521030778063107461479185584129724838500026741966009706375181200973944291377753293535599870196345794839828387911579809223830195674821079902123700459948419493000955974605340400274643934795418117953431
t1 = 76506200278870980622832162087706397184942731175881073072279653879125374026784231243082249838570209197788703418994598663770222774958590484366297473464547976157101536739056638340401709973910922952987332961258414506877745248599494701005790194262083540626575172771336888597402032923407057219028984697739294234494

r2 = 98112636909089823473886804230734608783665151359820285384385184926586779318832342840446756845270685151843520592521030778063107461479185584129724838500026741966009706375181200973944291377753293535599870196345794839828387911579809223830195674821079902123700459948419493000955974605340400274643934795418117953431
t2 = 95801086901355834240081662719865802187550109851113545620170852280638597493801662857576200633666749663318260607079963837967122188013554434395565196430708343554452720734056250267521097855586180792722796772893530089500987302933561979841152407078582329739116130182358926512269862531407749668332924957717479984854

m1_ = int.from_bytes(m1, byteorder='big') 
t1_inv = modinv(t1, p)
m2 = (m1_ * t1_inv * t2) % p
byte_ = m2.to_bytes((m2.bit_length() + 7) // 8, byteorder='big')
msg = byte_.decode("UTF-8")
print("message: ", msg)

