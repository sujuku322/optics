from optics.ray import Ray
from optics.surface import Lens
from optics.trace import trace_ray
from gui.plotter import plot_rays
from modules.convex_lens import simulate_convex_lens
from gui.app import OpticsApp

if __name__ == "__main__":
    app = OpticsApp()
    app.mainloop()

if __name__ == "__main__":
    simulate_convex_lens()

# 建立初始光線（平行光）
rays = [Ray([-10, y], [1, 0]) for y in range(-3, 4)]

# 建立一個透鏡元件（位置在 x = 0，焦距為 5）
lens = Lens(x=0, focal_length=5)

# 追蹤光線經過透鏡的折射
traced_rays = [trace_ray(ray, lens) for ray in rays]

# 顯示圖像
plot_rays(traced_rays, lens)
