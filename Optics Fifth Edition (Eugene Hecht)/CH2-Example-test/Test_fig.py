import numpy as np
import matplotlib.pyplot as plt

# 定義參數
v = 1  # 波速
x = np.linspace(-10, 10, 400)  # x 範圍

# 計算 ψ(x, t) 對不同 t
def psi(x, t, a=0.05, b=1, v=1 ):
    #return np.exp(-4*a*x**2 - b*t**2 + 4*np.sqrt(a*b)*x*t)
    return 0.03*np.cos((3.14159*x)/2)
# 時間點列表
#times = [0, 1, 2, 3]

# 畫圖
plt.figure(figsize=(10, 6))
#for t in times:
plt.plot(x, psi(x,t=6))
#, label=f't = {t}'
plt.title("Wave profile ψ(x, t) over time")
plt.xlabel("x")
plt.ylabel("ψ(x, t)")
plt.legend()
plt.grid(True)
plt.show()
