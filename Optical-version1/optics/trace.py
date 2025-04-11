def trace_ray(ray, lens):
    # 光線平行 → 透過透鏡折射，往焦點射出
    x0, y0 = ray.origin
    dx, dy = ray.direction
    yf = (lens.focal_length / dx) * dy + y0  # 簡單計算焦點位置

    # 加入透鏡後的轉折點（設為焦點）
    ray.path.append([lens.x, yf])
    return ray
