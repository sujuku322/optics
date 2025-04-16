# fig.py
import numpy as np
import matplotlib.pyplot as plt

def plot_wave_function(psi, x, times=[0, 1, 2, 3]):
    """
    繪製波形函數 psi(x, t)

    參數：
    - psi_func: 你要繪圖的函數 (例如 psi(x, t))
    - v: 波速
    - x_range: 要畫圖的 x 範圍
    - times: 要畫的時間點列表
    """
    x = np.linspace(-10, 10, 400)

    plt.figure(figsize=(10, 6))
    for t in times:
        plt.plot(x, psi(x, t), label=f't = {t}')

    plt.title("Wave profile ψ(x, t) over time")
    plt.xlabel("x")
    plt.ylabel("ψ(x, t)")
    plt.legend()
    plt.grid(True)
    plt.show()
