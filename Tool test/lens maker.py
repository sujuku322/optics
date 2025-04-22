def lens_maker_equation(n, R1, R2):
    """
    計算單片透鏡焦距
    n: 透鏡材料折射率
    R1: 入射面曲率半徑
    R2: 出射面曲率半徑
    """
    try:
        return 1 / ((n - 1) * ((1 / R1) - (1 / R2)))
    except ZeroDivisionError:
        return float('inf')

def doublet_focal_length(n1, R1_1, R1_2, n2, R2_1, R2_2):
    """
    計算雙合透鏡總焦距（膠合，不考慮間距）
    n1: 第一片透鏡折射率
    R1_1, R1_2: 第一片透鏡兩面曲率半徑
    n2: 第二片透鏡折射率
    R2_1, R2_2: 第二片透鏡兩面曲率半徑
    """
    f1 = lens_maker_equation(n1, R1_1, R1_2)
    f2 = lens_maker_equation(n2, R2_1, R2_2)
    
    if f1 == float('inf') or f2 == float('inf'):
        return "錯誤：曲率半徑不能為零"
    
    f_total = 1 / ((1 / f1) + (1 / f2))
    return f_total, f1, f2

# 範例執行
if __name__ == "__main__":
    # 假設值：可以換成你自己的
    n1 = 1.5168  # 第一片折射率（如：N-BK7）
    R1_1 = 62.8  # 第一片前表面 (mm)
    R1_2 = -45.7  # 第一片後表面 (mm)
    
    n2 = 1.6727  # 第二片折射率（如：SF5）
    R2_1 = -45.7  # 第二片前表面 (mm)
    R2_2 = -128.2  # 第二片後表面 (mm)
    
    f_total, f1, f2 = doublet_focal_length(n1, R1_1, R1_2, n2, R2_1, R2_2)
    
    print("雙透鏡設計:")
    print(f"第一片焦距: {f1:.2f} mm") # :.2f 保留小數點後兩位
    print(f"第二片焦距: {f2:.2f} mm")
    print(f"總焦距: {f_total:.2f} mm")
