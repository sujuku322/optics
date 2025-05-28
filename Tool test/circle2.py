import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

def interactive_circle_distance_fixed_xaxis(diameter):
    r = diameter / 2
    theta_vals = np.linspace(0, 2 * np.pi, 360)

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.4)
    ax.set_aspect('equal')
    ax.set_title("Circle with Distance to X-axis (y=0)")
    ax.set_xlim(-r - 1, r + 1)
    ax.set_ylim(-r - 1, r + 1)

    h = 0  # x軸高度固定為0

    # 畫圓
    x_circle = r * np.cos(theta_vals)
    y_circle = r * np.sin(theta_vals)
    ax.plot(x_circle, y_circle, label="Circle")

    # 畫灰色虛線 y=0 (x軸)
    line_gray, = ax.plot([-r - 1, r + 1], [h, h], color='gray', linestyle='--')

    # 初始角度與點
    initial_theta = 0
    x_point = r * np.cos(initial_theta)
    y_point = r * np.sin(initial_theta)

    # 點與紅色垂線
    point_dot, = ax.plot([x_point], [y_point], 'ro', label="Selected Point")
    distance_line, = ax.plot([x_point, x_point], [y_point, h], 'r--', linewidth=1)

    # 距離文字
    distance_text = ax.text(0.05, 0.95, f"Distance to X-axis: {abs(y_point - h):.2f}",
                            transform=ax.transAxes,
                            fontsize=9, color='blue',
                            verticalalignment='top', horizontalalignment='left',
                            bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

    # 角度滑動條
    ax_theta = plt.axes([0.15, 0.25, 0.7, 0.03])
    theta_slider = Slider(ax_theta, 'Angle (deg)', 0, 360, valinit=np.degrees(initial_theta))

    # 角度輸入框
    ax_angle_box = plt.axes([0.15, 0.18, 0.3, 0.05])
    text_box_angle = TextBox(ax_angle_box, 'Input Angle', initial=str(int(np.degrees(initial_theta))))

    # X座標輸入框
    ax_x_box = plt.axes([0.55, 0.18, 0.3, 0.05])
    text_box_x = TextBox(ax_x_box, 'Input X', initial=f"{x_point:.2f}")

    # 函數：由角度計算X, Y
    def xy_from_theta(theta_deg):
        theta = np.radians(theta_deg)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

    # 函數：由X計算Y（取上半圓）
    def y_from_x(x_val):
        val = r**2 - x_val**2
        if val < 0:
            return None  # 超出圓範圍無解
        return np.sqrt(val)

    # 更新全部函數（角度控制）
    def update_from_theta(theta_deg):
        x, y = xy_from_theta(theta_deg)
        # 更新點和線
        point_dot.set_data([x], [y])
        distance_line.set_data([x, x], [y, h])
        distance_text.set_text(f"Distance to X-axis: {abs(y - h):.2f}")

        # 同步X輸入框
        text_box_x.set_val(f"{x:.2f}")
        fig.canvas.draw_idle()

    # 更新全部函數（X控制）
    def update_from_x(x_val):
        y = y_from_x(x_val)
        if y is None:
            # 無效X，隱藏點與線，並提示
            point_dot.set_data([], [])
            distance_line.set_data([], [])
            distance_text.set_text(f"X={x_val:.2f} out of circle range!")
            fig.canvas.draw_idle()
            return
        # 更新點和線
        point_dot.set_data([x_val], [y])
        distance_line.set_data([x_val, x_val], [y, h])
        distance_text.set_text(f"Distance to X-axis: {abs(y - h):.2f}")

        # 同步角度滑動條與輸入框
        theta = np.degrees(np.arctan2(y, x_val)) % 360
        theta_slider.set_val(theta)
        text_box_angle.set_val(f"{theta:.2f}")
        fig.canvas.draw_idle()

    # 事件：角度滑動條改變
    def on_theta_slider(val):
        text_box_angle.set_val(f"{val:.2f}")
        update_from_theta(val)

    # 事件：角度輸入框提交
    def on_angle_submit(text):
        try:
            val = float(text) % 360
            theta_slider.set_val(val)
            update_from_theta(val)
        except ValueError:
            pass

    # 事件：X輸入框提交
    def on_x_submit(text):
        try:
            x_val = float(text)
            if abs(x_val) > r:
                distance_text.set_text(f"X={x_val:.2f} out of circle range!")
                fig.canvas.draw_idle()
                return
            update_from_x(x_val)
        except ValueError:
            pass

    theta_slider.on_changed(on_theta_slider)
    text_box_angle.on_submit(on_angle_submit)
    text_box_x.on_submit(on_x_submit)

    # 初始更新
    update_from_theta(np.degrees(initial_theta))

    plt.show()

# 呼叫測試
interactive_circle_distance_fixed_xaxis(diameter=1300)
