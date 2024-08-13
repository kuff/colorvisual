import numpy as np
import matplotlib.pyplot as plt

def srgb_to_xyz(rgb):
    # Convert sRGB to linear RGB
    rgb_linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    
    # Convert linear RGB to XYZ
    m = np.array([
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041]
    ])
    return np.dot(m, rgb_linear.T).T

def xyz_to_xyy(xyz):
    sum_xyz = np.sum(xyz, axis=1)
    x = xyz[:, 0] / sum_xyz
    y = xyz[:, 1] / sum_xyz
    Y = xyz[:, 1]
    return np.column_stack((x, y, Y))

# Generate sRGB color space
r = np.linspace(0, 1, 10)
g = np.linspace(0, 1, 10)
b = np.linspace(0, 1, 10)
rgb = np.array(np.meshgrid(r, g, b)).T.reshape(-1, 3)

# Convert sRGB to XYZ and then to xyY
xyz = srgb_to_xyz(rgb)
xyy = xyz_to_xyy(xyz)

# Create 3D plots
fig = plt.figure(figsize=(15, 6))

# sRGB color space
ax1 = fig.add_subplot(121, projection='3d')
scatter1 = ax1.scatter(rgb[:, 0], rgb[:, 1], rgb[:, 2], c=rgb, s=20)
ax1.set_xlabel('R')
ax1.set_ylabel('G')
ax1.set_zlabel('B')
ax1.set_title('sRGB Color Space')

# xyY color space
ax2 = fig.add_subplot(122, projection='3d')
scatter2 = ax2.scatter(xyy[:, 0], xyy[:, 1], xyy[:, 2], c=rgb, s=20)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('Y')
ax2.set_title('xyY Color Space')

plt.tight_layout()

def on_rotate(event):
    if event.inaxes == ax1:
        ax2.view_init(elev=ax1.elev, azim=ax1.azim)
    elif event.inaxes == ax2:
        ax1.view_init(elev=ax2.elev, azim=ax2.azim)
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_rotate)

plt.show()
