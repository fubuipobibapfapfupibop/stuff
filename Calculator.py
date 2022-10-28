import math
from numba import jit
import warnings
import numpy
warnings.filterwarnings('ignore')
#--- to do ---:
#add inverse hyperbolic functions like arcsetch, arcsinh etc
#add fourier and laplace transform
#add matrix calculations
#add plotting ability
#add piecewise operators
#add indefinite integrals
#add summations and products
#add pi and e

#notes
#logarithm input: (log,base,val)
#sine input: (sin.val)
#cos input: (cos.val)
#root input: (root,base,val)

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679  #first 100 digits of pi
e =  2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274  #first 100 digits of e


def parse(somefunction):
    somefunction = str(somefunction)
    somefunction = somefunction.split('.')
    value = (somefunction[1:len(somefunction)])
    value = ''.join(value)
    if not 'j' in str(somefunction):
        return float(value)
    else:
        try:
            value = complex(value)
            return complex(value)
        except Exception as e:
            print('invalid input')


def hyperbolic_arccosine(function):
    x = parse(function)
    if x > 1:
        root1 = root(f'root,2,{x**2-1}')
        return natural_logarithm(f'ln.{x+root1}')
    else: 
        return 'err1'

def hyperbolic_arcsecant(function):
    return 'err2'

def hyperbolic_arccotangent(function):
    x = parse(function)
    if x > 1 or x < -1:
        return hyperbolic_arctangent(f'arctanh.{1/x}')
    else:
        return 'err1'

def hyperbolic_arctangent(function):
    x = parse(function)
    if x < 1 and x > -1:
        return 0.5*(natural_logarithm(f'ln.{(1+x)/(1-x)}'))
    else:
        return 'err1'


def hyperbolic_arcosecant(function):
    x = parse(function)
    root1 = root(f'root,2,{(1/(x**2))+1}')
    return natural_logarithm(f'ln.{(1/x)+root1}')

def hyperbolic_arcsine(function):
    x = parse(function)
    root1 = root(f'root,2,{x**2+1}')
    return natural_logarithm(f'ln.{x+root1}')

def hyperbolic_cosecant(function):
    x = parse(function)
    return 1/(hyperbolic_sine(f'sinh.{x}'))

def hyperbolic_secant(function):
    x = parse(function)
    return 1/(hyperbolic_cosine(f'coth.{x}'))

def hyperbolic_cotangent(function):
    x = parse(function)
    return 1/(hyperbolic_tangent(f'tanh.{x}'))

def hyperbolic_tangent(function):
    x = parse(function)
    return hyperbolic_sine(f'sinh.{x}')/hyperbolic_cosine(f'cosh.{x}')

def hyperbolic_sine(function):
    x = parse(function)
    return ((e**x)-(e**-x))/2

def hyperbolic_cosine(function):
    x = parse(function)
    return ((e**x)+(e**-x))/2

def arccotangent(function):
    x = parse(function)
    return (pi/2)-(arctangent(f'arctan.{x}'))

def arccosecant(function):
    x = parse(function)
    return (pi/2)-arcsecant(f'arcsec.{x}')

def arcsecant(function):
    x = parse(function)
    return arccosine(f'arccos.{1/x}')

def arctangent(function):
    x = parse(function)
    exactness = 500
    x2 = x**2
    d = exactness * 2 + 1
    for k in range(exactness, 0, -1):
        f = k * 2 - 1
        d = f + k*k*x2/d
    return x / d

def arccosine(function):
    x = parse(function)
    root1 = root(f'root,2,{1-(x**2)}')
    return arctangent(f'arctan.{root1/x}')

def arcsine(function):
    x = float(parse(function))
    root1 = root(f'root,2,{1-(x**2)}')
    return arctangent(f'arctan.{x/root1}')

def cotangent(function):
    x = parse(function)
    return (cosine(f'cos.{x}'))/(sine(f'sin.{x}'))

def cosecant(function):
    x = parse(function)
    return 1/(sine(f'sin.{x}'))

def secant(function):
    x = parse(function)
    return 1/(cosine(f'cos.{x}'))

def tangent(function):
    x = parse(function)
    return (sine(f'sin.{x}'))/(cosine(f'cos.{x}'))

def root(function):
    function = str(function)
    function = function.split(',')
    base = float(function[1])
    value = float(function[2])
    res = value**(1/base)
    if res.real < 1e-15:
        return res.imag
    elif res.imag < 1e-15:
        return res.real
    else:
        return res

def natural_logarithm(function):
    x = parse(function)
    return logarithm(f'log,{e},{x}')

def logarithm(function):
    #i had to use the math module for logarithms because they are very complicated to solve
    function = str(function)
    function = function.split(',')
    base = function[1]
    value = function[2]
    return math.log(float(value),float(base))

def sine(function):
    x = parse(function)
    return (-e**((-x)*1j)+(e**(x*1j)))/2j

def cosine(function):
    x = parse(function)
    return sine(f'sin.{(pi/2)-x}')

def definite_integral(function):
    function = str(function)
    function = function.split(',')
    a = function[1]
    b = function[2]
    calculationbase = function[3]
    exactness = 30000
    a = int(a)*exactness
    b = int(b)*exactness
    ans = 0
    while a != b:
        calculation = calculationbase.replace('x',str(a/exactness))
        value = evaluate(calculation)
        ans+=value
        if a>b:
            a-=1
        elif a<b:
            a+=1
    return ans/exactness

def exponentiation(a,b):
    return float(a)**float(b)

def division(a,b):
    return float(a)/float(b)

def multiplication(a,b):
    return float(a)*float(b)

def substraction(a,b):
    return float(a)-float(b)

def addition(a,b):
    return float(a)+float(b)

def calculate(expression):
    result2 = expression
    values = []
    #splitting expression
    expression = str(expression)
    values = expression.split(' ')
    stoploop = False
    #calculate expression
    while not stoploop:
        for i in range(len(values)):
            updatevalues = True
            char = str(values[i])
            #find numbers
            try:
                n1 = values[i-1]
                n2 = values[i+1]
            except:
                pass
            if char == '^':
                result2 = exponentiation(n1,n2)
            elif char == '/':
                result2 = division(n1,n2)
            elif char == '*':
                result2 = multiplication(n1,n2)
            elif char == '-':
                result2 = substraction(n1,n2)
            elif char == '+':
                result2 = addition(n1,n2)
            elif char[0:2] == 'di':
                result2 = definite_integral(char)
            elif char[0:3] == 'log':
                result2 = logarithm(char)
            elif char[0:2] == 'ln':
                result2 = natural_logarithm(char)
            elif char[0:3] == 'cos' and char[3] != 'h':
                result2 = cosine(char)
            elif char[0:3] == 'sin' and char[3] != 'h':
                result2 = sine(char)
            elif char[0:4] == 'root':
                result2 = root(char)
            elif char[0:3] == 'tan' and char[3] != 'h':
                result2 = tangent(char)
            elif char[0:3] == 'sec' and char[3] != 'h':
                result2 = secant(char)
            elif char[0:3] == 'csc' and char[3] != 'h':
                result2 = cosecant(char)
            elif char[0:3] == 'cot' and char[3] != 'h':
                result2 = cotangent(char)
            elif char[0:6] == 'arcsin' and char[6] != 'h':
                result2 = arcsine(char)
            elif char[0:6] == 'arccos'and char[6] != 'h':
                result2 = arccosine(char)
            elif char[0:6] == 'arctan'and char[6] != 'h':
                result2 = arctangent(char)
            elif char[0:6] == 'arcsec'and char[6] != 'h':
                result2 = arcsecant(char)
            elif char[0:6] == 'arccsc'and char[6] != 'h':
                result2 = arccosecant(char)
            elif char[0:6] == 'arccot'and char[6] != 'h':
                result2 = arccotangent(char)
            elif char[0:4] == 'sinh':
                result2 = hyperbolic_sine(char)
            elif char[0:4] == 'cosh':
                result2 = hyperbolic_cosine(char)
            elif char[0:4] == 'tanh':
                result2 = hyperbolic_tangent(char)
            elif char[0:4] == 'coth':
                result2 = hyperbolic_cotangent(char)
            elif char[0:4] == 'sech':
                result2 = hyperbolic_secant(char)
            elif char[0:4] == 'csch':
                result2 = hyperbolic_cosecant(char)
            elif char[0:7] == 'arcsinh':
                result2 = hyperbolic_arcsine(char)
            elif char[0:7] == 'arccsch':
                result2 = hyperbolic_arcosecant(char)
            elif char[0:7] == 'arctanh':
                result2 = hyperbolic_arctangent(char)
            elif char[0:7] == 'arccoth':
                result2 = hyperbolic_arccotangent(char)
            elif char[0:7] == 'arccosh':
                result2 = hyperbolic_arccosine(char)
            elif char[0:7] == 'arcsech':
                result2 = hyperbolic_arcsecant(char)
            else:
                updatevalues = False
            #update expression
            if updatevalues:
                del values[i-1:i+2]
                values.insert(i-1,result2)
                break
            if len(values) == 1 or len(values) < 1:
                stoploop = True
    return result2


            
def evaluate(inpt):
    inpt = str(inpt)
    opening_bracket_count = 0
    closing_bracket_count = 0
    index = []
    tte = 0
    while True: 
        if '(' in inpt:
            for i in range(len(inpt)):
                char = inpt[i]
                if char == '(':
                    if opening_bracket_count == closing_bracket_count:
                        index.append(i)
                    opening_bracket_count+=1
                elif char == ')':
                    closing_bracket_count+=1
                    if opening_bracket_count == closing_bracket_count:
                        index.append(i)
            tte = inpt[index[0]+1:index[1]] #thing to evaluate
            ebtte = inpt[0:index[0]] #everything before tte
            eatte = inpt[index[1]+1:len(inpt)] #everything after tte
            if eatte == ')':
                eatte = ''
            evaluation = evaluate(tte)
            inpt = f'{ebtte}{evaluation}{eatte}'
            inpt = str(inpt)
        else:
            result = calculate(inpt)
            break
    if result == 'err1':
        result = 'result does not exist (nullity / infinity)'
    elif result == 'err2':
        result = 'result is complex'
    return result
while True:
    input2 = input('>>>   ')
    #input2 = 'di,1,10,x;*;2'
    res = evaluate(input2)
    print(res)