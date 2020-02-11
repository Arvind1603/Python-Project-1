import cmath
from sympy import *
from fractions import Fraction


'''-------------------------------------------------------
-------------  All functions listed below  ---------------
----------------------------------------------------------'''

#########################################
def my_quad_equation(coefa,coefb,coefc):
    a = coefa
    b = coefb
    c = coefc 
    f1 = "%.1f * x * * 2 + %.1f * x + %f" %(a,b,c)
    f2 = "x * * 2 + %.1f * x + %f" %(b,c)
    f3 = "%.1f * x * * 2 + x + %f" %(a,c)
    f4 = "x * * 2 + x + %f" %(c)
    f5 = "%.1f * x * * 2 + %f" %(a,c)
    f6 = "%.1f * x * * 2 + %f * x" %(a,b)
    if (a == 1 and b == 1 and c != 0) :
        return str(f4)
    elif (a == 1 and b != 0 and c != 0) :
        return str(f2)
    elif (b == 1 and c != 0) :
        return str(f3)
    elif (b == 0 and c != 0) :
        return str(f5)
    elif (c == 0) :
        return str(f6)
    else :
        return str(f1)

##########################################


#########################################

x = Symbol('x')
def my_quad_equation_derivative(coefa,coefb):
    a = coefa
    b = coefb   
    f = a*x**2+b*x
    df = f.diff(x)
    if (a*2 == 1):
        return str(x+b)
    elif (a*2 != 1):
        return str(df)    
##########################################


############################################
def evaluate_quad_equation(coefa,coefb,coefc,x):
    a = coefa
    b = coefb
    c = coefc
    result = (a*x**2+b*x+c)
    return str("f(%.1f) = %f" %(x, result))
###########################################


##########################################
def info_extremum(coefa):
    a =  coefa
    if (a > 0) :
        return ("Minimum")
    elif (a < 0) :
        return ("Maximum")
###########################################



#############################################
def compute_discriminant(coefa,coefb,coefc):
    a = coefa
    b = coefb
    c = coefc
    delta = b**2 - 4*a*c
    return str(Fraction(delta))
############################################


############################################
def print_info_solution_quad(coefa,coefb,coefc,dis):
    a = coefa
    b = coefb
    c = coefc
    dis = b**2 - 4*a*c
    x0 = -b/(2*a)
    x1 = (-b + cmath.sqrt(dis))/(2*a)
    x2 = (-b - cmath.sqrt(dis))/(2*a)
    if (dis > 0) :
        print ("Two Solution: %s and %s" %(x1,x2))
        print ("Factorize form: f(x)=", a*((x - x1)*(x - x2)))
    if (dis < 0) :
        print ("Two complex Solution: %s and %s" %(x1,x2))
    elif (dis == 0) :
        print ("One Solution: %s"%(x0))
        print ("Factorize form: f(x)=", a*((x - x0)**2))
##############################################

