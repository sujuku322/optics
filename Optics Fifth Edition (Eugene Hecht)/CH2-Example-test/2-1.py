import sympy as sp
import numpy as np
from main_verify import verify_wave_equation
from main_fig import plot_wave_function

x, t, v= sp.symbols('x t v', real=True, positive=True)

psi = 3 / (10 * (x - v*t)**2 + 1)
verify_wave_equation(psi, x, t)

def psi(x, t, v=1):
    return 3 / (10 * (x - v*t)**2 + 1) 
plot_wave_function(psi, x)
