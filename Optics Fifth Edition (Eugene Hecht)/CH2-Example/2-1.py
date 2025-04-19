import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 定義符號變數
x, t, v = sp.symbols('x t v')
psi = 3 / (10 * (x - v*t)**2 + 1)

# 對 x 和 t 的二階偏微分
d2_psi_dx2 = sp.diff(psi, x, 2)
d2_psi_dt2 = sp.diff(psi, t, 2)

# 驗證波動方程
wave_eq = sp.simplify(d2_psi_dx2 - (1/v**2)*d2_psi_dt2)

print("∂²ψ/∂x² =", sp.latex(d2_psi_dx2))
print("∂²ψ/∂t² =", sp.latex(d2_psi_dt2))
print("是否符合波動方程:", wave_eq == 0)
if wave_eq == 0:
        print("\n✅ ψ(x, t) 滿足一維波動方程")
else:
    print("\n❌ ψ(x, t) 不符合波動方程")
# 數值繪圖部分
# 設定參數
v_val = 1
t_val = 0
time_list = [-2, -1, 1, 2]
x_vals = np.linspace(-5, 5, 400)
psi_func = lambda x: 3 / (10 * (x - v_val * t_val)**2 + 1)


# 繪製圖形
for t_val in time_list:
    psi_vals = psi_func(x_vals)
    plt.plot(x_vals, psi_vals, label=f't={t_val}, v={v_val}')
plt.title(r'$\psi(x, t) = \frac{3}{10(x - vt)^2 + 1}$')
plt.xlabel('x')
plt.ylabel('ψ(x, t)')
plt.grid(True)
plt.legend()
plt.show()
