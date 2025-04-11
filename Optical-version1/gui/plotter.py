import matplotlib.pyplot as plt

def plot_rays(rays, lens):
    for ray in rays:
        path = ray.path
        xs, ys = zip(*path)
        plt.plot(xs, ys)

    plt.axvline(lens.x, color='gray', linestyle='--', label='Lens')
    plt.title("Ray Tracing Demo")
    plt.grid(True)
    plt.legend()
    plt.show()
