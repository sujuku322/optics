import sympy as sp
import numpy as np
from main_verify import verify_wave_equation
from main_fig import plot_wave_function

x, t, v, a, b = sp.symbols('x t v a b', real=True, positive=True)
psi = sp.exp(-4*a*x**2 - b*t**2 + 4*sp.sqrt(a*b)*x*t)
#psi = sp.sin(x - v * t )
#psi = 3 / (10 * (x - v*t)**2 + 1)
#psi = 0.03*sp.cos(3.14159*)
#verify_wave_equation(psi, x, t, v, a, b)
verify_wave_equation(psi, x, t, v, a, b)

#def psi(x, t, a=0.05, b=1):
#    return np.exp(-4*a*x**2 - b*t**2 + 4*np.sqrt(a*b)*x*t)  # 高斯脈衝波
def psi(x, t, a=0.05, b=1, v=1):
    #return np.sin( x - v * t)
    #return 3 / (10 * (x - v*t)**2 + 1)
    return np.exp(-4*a*x**2 - b*t**2 + 4*np.sqrt(a*b)*x*t)
plot_wave_function(psi, x)


'''
def psi3(x, t, v=1):
    return np.sin(x - v * t )  # 高斯脈衝波
plot_wave_function(psi3)
'''
