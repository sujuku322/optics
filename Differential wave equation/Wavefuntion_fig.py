import numpy as np
import matplotlib.pyplot as plt

# 定義參數
v = 1  # 波速
x = np.linspace(-10, 10, 400)  # x 範圍

# 計算 ψ(x, t) 對不同 t
def psi(x, t, v=1):
    return 3 / (10 * ( x- v * t)**2 + 1)
    #return x *t
    #return x**2 + np.sin(x)
    #return np.exp(x * t)
# 時間點列表
times = [0, 1, 2, 3]

# 畫圖
plt.figure(figsize=(10, 6))
for t in times:
    plt.plot(x, psi(x, t), label=f't = {t}')

plt.title("Wave profile ψ(x, t) over time")
plt.xlabel("x")
plt.ylabel("ψ(x, t)")
plt.legend()
plt.grid(True)
plt.show()
