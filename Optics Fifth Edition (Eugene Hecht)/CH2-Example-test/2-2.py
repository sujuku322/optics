import sympy as sp
import numpy as np
from main_verify import verify_wave_equation
from main_fig import plot_wave_function

x, t, v, a, b = sp.symbols('x t v a b', real=True, positive=True)

psi = sp.exp(-4*a*x**2 - b*t**2 + 4*sp.sqrt(a*b)*x*t)
verify_wave_equation(psi, x, t, v)

def psi(x, t, a=1, b=1):

    return np.exp(-4*a*x**2 - b*t**2 + 4*np.sqrt(a*b)*x*t)
plot_wave_function(psi, x)
