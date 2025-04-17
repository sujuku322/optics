import sympy as sp

def verify_wave_equation(psi, x, t):
    
    """
    驗證給定的 ψ(x, t) 是否符合一維波動方程
    :param psi: 需要驗證的波函數 ψ(x, t)
    :param x: 空間變數
    :param t: 時間變數
    :param v: 波速
    """
    
    # 計算二階偏導數
    d2psi_dx2 = sp.diff(psi, x, 2)
    d2psi_dt2 = sp.diff(psi, t, 2)

    # 波動方程左邊和右邊
    lhs = d2psi_dx2
    rhs = (1 / v**2) * d2psi_dt2

    # 簡化差異項
    difference = sp.simplify(lhs - rhs)
    
    print("\n左邊 - 右邊 的結果（應該為 0）:")
    print(sp.latex(sp.simplify(difference)))

    print('\n','D_to_x\n',sp.latex(sp.simplify(d2psi_dx2)))
    print('\n','D_to_t\n',sp.latex(sp.simplify(d2psi_dt2)))
    if difference == 0:
        print("\n✅ ψ(x, t) 滿足一維波動方程")
    else:
        print("\n❌ ψ(x, t) 不符合波動方程")


#x, t, v, a, b = sp.symbols('x t v a b', real=True, positive=True)

'''
psi = sp.exp(-4*a*x**2 - b*t**2 + 4*sp.sqrt(a*b)*x*t)
verify_wave_equation(psi, x, t, v, a, b)
'''

''' 3 / (10 * (x - v*t)**2 + 1)
psi = 3 / (10 * (x - v*t)**2 + 1)
verify_wave_equation(psi, x, t, v)
'''

''' x * t
# 更改為不同的波函數
psi_new = x *t
verify_wave_equation(psi_new, x, t, v)
'''

'''exp(x * t)
psi = sp.exp(x * t)       # 混合型式
verify_wave_equation(psi, x, t, v)
'''

'''x**2 + sp.sin(x)
psi = x**2 + sp.sin(x)    # 測試靜態函數
verify_wave_equation(psi, x, t, v)
'''

