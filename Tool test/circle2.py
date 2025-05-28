'''
我需要顯示圓及每個點到 x 軸的垂直距離，然後我可以在圓周上有一個點，用滑動的方式更改點到 x 軸的垂直距離
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

def interactive_circle_distance(diameter):
    r = diameter / 2
    theta_vals = np.linspace(0, 2 * np.pi, 360)

    # 初始化圖形
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)
    ax.set_aspect('equal')
    ax.set_title("Interactive Circle with Distance to X-axis")
    ax.set_xlim(-r - 1, r + 1)
    ax.set_ylim(-r - 1, r + 1)
    ax.axhline(0, color='gray', linestyle='--')

    # 畫圓
    x_circle = r * np.cos(theta_vals)
    y_circle = r * np.sin(theta_vals)
    ax.plot(x_circle, y_circle, label="Circle")

    # 初始角度與點
    initial_theta = 0
    x_point = r * np.cos(initial_theta)
    y_point = r * np.sin(initial_theta)

    # 點與垂直距離線
    point_dot, = ax.plot([x_point], [y_point], 'ro', label="Selected Point")
    distance_line, = ax.plot([x_point, x_point], [y_point, 0], 'r--', linewidth=1)

    # 縮小並移動距離文字
    distance_text = ax.text(0.05, 0.95, f"Distance to X-axis: {abs(y_point):.2f}",
                            transform=ax.transAxes,
                            fontsize=9, color='blue',
                            verticalalignment='top', horizontalalignment='left',
                            bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

    # 滑動條區域
    ax_theta = plt.axes([0.15, 0.2, 0.7, 0.03])
    theta_slider = Slider(ax_theta, 'Angle (deg)', 0, 360, valinit=np.degrees(initial_theta))

    # 文字輸入框
    ax_box = plt.axes([0.15, 0.1, 0.2, 0.05])
    text_box = TextBox(ax_box, 'Input Angle', initial=str(int(np.degrees(initial_theta))))

    # 更新畫面函數
    def update_by_theta_deg(theta_deg):
        theta = np.radians(theta_deg)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        point_dot.set_data([x], [y])
        distance_line.set_data([x, x], [y, 0])
        distance_text.set_text(f"Distance to X-axis: {abs(y):.2f}")
        fig.canvas.draw_idle()

    # 滑動時觸發
    def on_slider_change(val):
        theta_deg = val
        text_box.set_val(f"{theta_deg:.1f}")  # 同步更新輸入框
        update_by_theta_deg(theta_deg)

    # 輸入框提交時觸發
    def on_text_submit(text):
        try:
            theta_deg = float(text)
            theta_deg = theta_deg % 360  # 正規化
            theta_slider.set_val(theta_deg)  # 同步更新滑動條
            update_by_theta_deg(theta_deg)
        except ValueError:
            pass  # 忽略無效輸入

    theta_slider.on_changed(on_slider_change)
    text_box.on_submit(on_text_submit)

    plt.show()

# 呼叫函式：輸入直徑
interactive_circle_distance(diameter=130)
