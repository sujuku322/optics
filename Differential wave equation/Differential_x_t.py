import sympy as sp

# 符號定義
x, t, v = sp.symbols('x t v')

# 函數定義
psi = 3 / (10 * (x - v*t)**2 + 1)

# 對 t 微分
dpsi_dt = sp.diff(psi, t)
d2psi_dt2 = sp.diff(psi, t, 2)

# 顯示
sp.pretty_print(sp.simplify(dpsi_dt))
print("\n∂²ψ/∂t² =")
sp.pretty_print(sp.simplify(d2psi_dt2))
print("∂²ψ/∂t² = ", sp.latex(sp.simplify(d2psi_dt2)))