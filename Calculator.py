import cmath
from numba import jit
import warnings
warnings.filterwarnings('ignore')
#--- to do ---:
#fix  arcsinh and continue on trig functions
#add support for complex numbers everywhere (except integral ranges)
#add inverse hyperbolic functions like arcsetch, arcsinh etc
#add ability to view values on the complex plane
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
#https://www.digitec.ch/de/s1/product/philips-ph805-anc-30-h-kopfhoerer-12388306
#https://www.reichelt.com/ch/de/axialluefter-50x50x15mm-24v-22-1m-h-29dba-sun-mf50152v2-1-p260672.html?&trstct=pos_4&nbc=1

pi =     3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679  #first 100 digits of pi
e =      2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274  #first 100 digits of e
root15 = 3.8729833462074168851792653997823996108329217052915908265875737661134830919369790335192873768586735179  #first 100 digits or root15

def parse(somefunction):
    somefunction = str(somefunction)
    somefunction = somefunction.split('.')
    value = (somefunction[1:len(somefunction)])
    value = '.'.join(value)
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
    if x.imag == 0 and x.real > 1:
        root1 = x+root(f'root,2,{(x**2)-1}')
        return natural_logarithm(f'ln.{root1}')

def hyperbolic_arcsecant(function):
    x = parse(function)
    root1 = root(f'root,2,{(1-x)/(2*x)}')
    print(hyperbolic_arcsine(f'arcsinh.{root1}'))
    return  2*hyperbolic_arcsine(f'arcsinh.{root1}')
#
def hyperbolic_arccotangent(function):
    x = parse(function)
    root1 = hyperbolic_arctangent(f'arctanh.{1/x}')
    if x.real > 1 and x.real > -1:
        return root1
    else:
        if x.imag > 0:
            return (-root1.real)+(root1.imag*1j)
        else:
            return (-root1.real)-(root1.imag*1j)

def hyperbolic_arctangent(function):
    x = parse(function)
    if x.real < 1 and x.real > -1:
        return 0.5*(natural_logarithm(f'ln.{(1 + x) / (1 - x)}'))
    else:
        root1 = 1 / (x * 1j)
        return -(arccotangent(f'arccot.{-root1}')*1j)


def hyperbolic_arcosecant(function):
    x = parse(function)
    root1 = root(f'root,2,{(1/(x**2))+1}')
    return natural_logarithm(f'ln.{(1/x)+root1}')

def hyperbolic_arcsine(function):
    x = parse(function)
    if x.real == 0 and x.imag != 0 or x.real != 0 and x.imag == 0:
        root1 = root(f'root,2,{x**2+1}')
        return natural_logarithm(f'ln.{x+root1}')
    else:
        root1 = 1+(x**2)
        return natural_logarithm(f'ln.{root1}')

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
    return arctangent(f'arctan.{1/x}')

def arccosecant(function):
    x = parse(function)
    if x.imag == 0:
        return arcsine(f'arcsin.{1/x}').real
    else:
        return -(arcsine(f'arcsin.{1/x}'))

def arcsecant(function):
    x = parse(function)
    return arccosine(f'arccos.{1/x}')


def arctangent(function):
    x = parse(function)
    root1 = 0.5*(natural_logarithm(f'ln.{1+(x*1j)}')*1j)
    root2 = 0.5*(natural_logarithm(f'ln.{1-(x*1j)}')*1j)
    return root2-root1

def arccosine(function):
    x = parse(function)
    if x.imag == 0:
        if x.real < 1 and x.real > -1:
            return pi / 2 + (hyperbolic_arcsine(f'arcsinh.{x*1j}')*1j)
        else:
            return (pi / 2 - (-arcsine(f'arcsin.{x}')))-pi
    else:
        return pi / 2 + (hyperbolic_arcsine(f'arcsinh.{x*1j}')*1j)

def arcsine(function):
    x =parse(function)
    if x.imag == 0:
        root1 = (x+root(f'root,2,{1-(x**2)}'))*1j
        return natural_logarithm(f'ln.{root1}')
    else:
        if x.real == 0 and x.imag != 0:
            return (hyperbolic_arcsine(f'arcsinh.{x*1j}'))*1j
        else:
            root1 = hyperbolic_arcsine(f'arcsinh.{-(x*1j)}')

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
    base = complex(function[1])
    value = complex(function[2])
    if value.real == 0 and value.imag != 0 or value.real != 0 and value.imag == 0:
        res = value**(1/base)
        if value.real < 0:
            return res
        else:
            return res*1j
    else:
        if base == 2:
            return cmath.sqrt(value)
        else:
            return 'err2'

def natural_logarithm(function):
    x = parse(function)
    return logarithm(f'log,{e},{x}')

def logarithm(function):
    #i had to use the math module for logarithms because they are very complicated to solve
    function = str(function)
    function = function.split(',')
    base = complex(function[1])
    value = complex(function[2])
    return cmath.log(value,base)

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
    exactness = 5000
    a = int(a)*exactness
    b = int(b)*exactness
    ans = 0
    while a != b:
        calculation = calculationbase.replace('x',str(a/exactness))
        calculation = calculation.replace(';',' ')
        value = evaluate(calculation)
        ans+=complex(value)
        if a>b:
            a-=1
        elif a<b:
            a+=1
    return ans/exactness

def exponentiation(a,b):
    return complex(a)**complex(b)

def division(a,b):
    return complex(a)/complex(b)

def multiplication(a,b):
    return complex(a)*complex(b)

def substraction(a,b):
    return complex(a)-complex(b)

def addition(a,b):
    return complex(a)+complex(b)

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
                n1 = complex(n1)
                n2 = complex(n2)
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
    result= ''
    inpt = str(inpt)
    startindex = 0
    endindex = 0
    inparenthesis = ''
    while True:
        if '(' and ')' in inpt:
            for i in range(len(inpt)):
                char = inpt[i]
                if char == '(' :
                    startindex = i
                elif char == ')':
                    endindex = i
                    break
            inparenthesis = inpt[startindex+1:endindex]
            ebp = inpt[0:startindex]
            eap = inpt[endindex+1:len(inpt)]
            evaluation = str(evaluate(inparenthesis))
            inpt = ebp+evaluation+eap
        else:
            result = calculate(inpt)
            break
    if result == 'err1':
        result = 'result does not exist (nullity / infinity)'
    elif result == 'err2':
        result = 'result is complex'
    return result
checkresults =True
if checkresults:
    results = []
    checklist = [
        '1 + 8','5 - 3','3 * 3','10 / 5','3 ^ 3', '1 + (2 - (3 * (2 ^ (1 + 2))))',
        'di,1,10,x;*;2','log,4,5','root,2,256','sin.6','cos.4','tan.67','sec.5',
        'cot.5','csc.5','sinh.4','cosh.4','tanh.4','sech.4','coth.4','csch.5',
        'arcsin.4','arccos.4','arctan.0.2','arcsec.0.4','arccot.0.5'
    ]
    for item in checklist:
        results.append(evaluate(item))

while True:
    input2 = input('>>>   ')
    #input2 = 'di,1,10,x;*;2'
    res = complex(evaluate(input2))
    if res.imag < 0.00000000000001 and res.imag > -0.00000000000001:
        res = res.real + 0j
    elif res.real < 0.00000000000001 and res.real > -0.00000000000001:
        res = 0 + (res.imag*1j)
    print(f'real part:      {res.real}')
    print(f'imaginary part: {res.imag}')
