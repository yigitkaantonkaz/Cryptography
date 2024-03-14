import random
import requests
import BitVector

API_URL = 'http://harpoon1.sabanciuniv.edu:9999'
my_id = 29154
def get_poly():
  endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
  response = requests.get(endpoint) 	
  a = 0
  b = 0
  if response.ok:	
    res = response.json()
    print(res)
    return res['a'], res['b']
  else:
    print(response.json())

def check_mult(c):
  #check result of part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
  response = requests.put(endpoint) 	
  print(response.json())

def check_inv(a_inv):
  #check result of part b
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)) 
  print(response.json())

a, b = get_poly()
##SOLUTION  

m = BitVector(bitstring = '111000011')
n = 8
a = BitVector(bitstring = a)
b = BitVector(bitstring = b)
inv_ = a.gf_MI(m,n)
c = a.gf_multiply_modular(b, m, n)

check_inv(inv_)
check_mult(c)


