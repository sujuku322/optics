from optics.ray import Ray
from optics.surface import Lens
from optics.trace import trace_ray
from gui.plotter import plot_rays

def simulate_and_plot_lens():
    rays = [Ray([-10, y], [1, 0]) for y in range(-3, 4)]
    lens = Lens(x=0, focal_length=5)
    traced_rays = [trace_ray(ray, lens) for ray in rays]
    plot_rays(traced_rays, lens)
