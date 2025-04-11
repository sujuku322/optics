class Ray:
    def __init__(self, origin, direction):
        self.origin = origin  # 起點 [x, y]
        self.direction = direction  # 方向向量 [dx, dy]
        self.path = [origin]  # 記錄路徑（點的列表）
