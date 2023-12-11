
def square(number):
    return number * number

def add(a,b) :
    return a+b 

def mul(a,b) :
    return a*b 

def deff(a,b) :
    return a-b 

print('''
1.square
2.adding
3.multiplication
4.differnce''')
x=int(input('choose an operator'))

if x==1:
    m=float(input('second number'))
    square(m)

if x==1:
    m=float(input('first number'))
    n=float(input('second number'))
    add(n,m)
  
if x==1:
    m=float(input('first number'))
    n=float(input('second number'))
    mul(n,m)
  
if x==1:
    m=float(input('first number'))
    n=float(input('second number'))
    deff(n,m)

