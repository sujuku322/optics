import numpy as np
import matplotlib.pyplot as plt

def simulate_convex_lens(focal_length=5, lens_x=0, ray_y_positions=None):
    if ray_y_positions is None:
        ray_y_positions = np.linspace(-2, 2, 5)

    plt.figure(figsize=(10, 4))
    for y0 in ray_y_positions:
        # 入射平行光線
        plt.plot([-10, lens_x], [y0, y0], 'b')  # 藍色：入射線
        # 折射線，折向焦點
        fx, fy = lens_x + focal_length, 0
        plt.plot([lens_x, fx], [y0, fy], 'r')   # 紅色：折射線

    plt.axvline(x=lens_x, color='black', linestyle='--', label='Lens')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.title('Convex Lens Ray Diagram')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['Incident Rays', 'Refracted Rays', 'Lens'])
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-3, 3)
    plt.show()
