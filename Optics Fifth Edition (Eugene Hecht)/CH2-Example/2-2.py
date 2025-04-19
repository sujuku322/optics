import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 符號定義
x, t, a, b = sp.symbols('x t a b', real=True)
psi = sp.exp(-4*a*x**2 - b*t**2 + 4*sp.sqrt(a*b)*x*t)

# 計算二階偏導數
d2_psi_dx2 = sp.diff(psi, x, 2)
d2_psi_dt2 = sp.diff(psi, t, 2)

# 嘗試化簡差異：∂²ψ/∂x² - (1/v²) ∂²ψ/∂t²
# 令 v² = b/(4a)，也就是 v = sqrt(b / 4a) = 1/2 sqrt(b / a)
v_sq = b / (4*a)
wave_eq = sp.simplify(d2_psi_dx2 - (1/v_sq)*d2_psi_dt2)

print("∂²ψ/∂x² =", sp.latex(d2_psi_dx2))
print("∂²ψ/∂t² =", sp.latex(d2_psi_dt2))
print("驗證波動方程 ∂²ψ/∂x² - (1/v²)∂²ψ/∂t² =", wave_eq)
if wave_eq == 0:
        print("\n✅ ψ(x, t) 滿足一維波動方程")
else:
    print("\n❌ ψ(x, t) 不符合波動方程")

# ---- 繪圖部分 ----
# 數值參數設定
a_val = 1
b_val = 1
t_val = 0
time_list = [-2, -1, 1, 2]
x_vals = np.linspace(-3, 3, 400)

# 轉為 lambda 函數供 numpy 使用
psi_func = sp.lambdify((x, t, a, b), psi, modules='numpy')


# 繪圖
for t_val in time_list:
    psi_vals = psi_func(x_vals, t_val, a_val, b_val)
    plt.plot(x_vals, psi_vals, label=f't={t_val}')
plt.title(r'$\psi(x, t) = e^{-4a x^2 - b t^2 + 4\sqrt{ab} x t}$')
plt.xlabel('x')
plt.ylabel('ψ(x, t)')
plt.grid(True)
plt.legend()
plt.show()
