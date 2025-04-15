import matplotlib.pyplot as plt

# X 軸標籤
labels = ['8:1:3', '3:1:3', '1:0.5:3', '1:3:3', '1:6:3']
x = range(len(labels))

# Contact Angle（紅色虛線）
contact_angle = [150, 152, 155, 137, 136]
contact_error = [1, 1, 1, 1, 1]

# Sliding Angle - 實線（藍）
sliding_angle_solid = [145, 142, 140, 138, 139]
sliding_error_solid = [2, 2, 2, 1.5, 2]

# Sliding Angle - 虛線（藍）
sliding_angle_dashed = [5, 4, 2, 1, 3]
sliding_error_dashed = [0.5, 0.5, 0.5, 0.3, 0.5]

fig, ax1 = plt.subplots(figsize=(8, 5))

# Contact Angle - 紅色虛線（含 I 型誤差）
color1 = 'red'
ax1.set_xlabel('The Content Ratio of CIP: NdFeB: PDMS')
ax1.set_ylabel('Contact Angle (°)', color=color1)
ax1.errorbar(x, contact_angle, yerr=contact_error, fmt='--o', color=color1,
             label='Contact Angle (swelling)', capsize=5, elinewidth=1.5, markeredgewidth=1.5)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(135, 160)

# Sliding Angle - 實線 + 虛線（藍色）
ax2 = ax1.twinx()
color2 = 'blue'
ax2.set_ylabel('Sliding Angle (°)', color=color2)

# 實線部分
ax2.errorbar(x, sliding_angle_solid, yerr=sliding_error_solid, fmt='-o', color=color2,
             label='Sliding Angle (swelling)', capsize=5, elinewidth=1.5, markeredgewidth=1.5)

# 虛線部分
ax2.errorbar(x, sliding_angle_dashed, yerr=sliding_error_dashed, fmt='--o', color=color2,
             label='Sliding Angle (non-swelling)', capsize=5, elinewidth=1.5, markeredgewidth=1.5)

ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(0, 20)

# X 軸文字
plt.xticks(x, labels)

# 圖例合併兩個 y 軸
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
plt.savefig("your_chart_name.png", dpi=300)

plt.tight_layout()
plt.show()

