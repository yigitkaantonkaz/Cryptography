import random
import requests

API_URL = 'http://harpoon1.sabanciuniv.edu:9999/'

# Change your id here
my_id = 29154   

def getQ1():
  endpoint = '{}/{}/{}'.format(API_URL, "Q1", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    print(res)
    n, t = res['n'], res['t']
    return n,t
  else: print(response.json())

def checkQ1a(order):   #check your answer for Question 1 part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1a", my_id, order)
  response = requests.put(endpoint) 	
  print(response.json())

def checkQ1b(g):  #check your answer for Question 1 part b
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())

def checkQ1c(gH):  #check your answer for Question 1 part c
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())

import math
import random
import warnings

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def find_generator(t):
    generators = []
    for k in range(1, t + 1):
        if math.gcd(t, k) == 1:
            if k < t:
                generators.append(k)
    return generators

getQ1()
amount = phi(359)
print(amount)
checkQ1a(amount)
generators = find_generator(179)
print(generators)
checkQ1b(178)

def is_coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

def find_generator2(n, t):
    for g in range(2, n):
        if is_coprime(g, n):
            if pow(g, t, n) == 1:
                return g
            
generator = find_generator2(359, 179)
print(generator)
checkQ1c(generator)