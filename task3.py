import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

print("--- TASK 3: CHANNEL SLICING & ISOLATION ---")

image_path = "sample.jpg"

# Agar sample.jpg maujood na ho to yahin create kar lega
if not os.path.exists(image_path):
    temp_grid = np.zeros((300, 400, 3), dtype=np.uint8)
    temp_grid[0:150, 0:200] = [255, 0, 0]        # Red quadrant
    temp_grid[0:150, 200:400] = [0, 255, 0]      # Green quadrant
    temp_grid[150:300, 0:200] = [0, 0, 255]      # Blue quadrant
    temp_grid[150:300, 200:400] = [255, 255, 255]# White quadrant
    Image.fromarray(temp_grid).save(image_path)

# 1. Load image and convert to RGB array
raw_img = Image.open(image_path).convert("RGB")
img = np.array(raw_img, dtype=np.uint8)

# 2. Extract 2D intensity grids (Axis 2 slicing)
red_2d = img[:, :, 0]
green_2d = img[:, :, 1]
blue_2d = img[:, :, 2]

# 3. Construct isolated 3D color images
red_only = np.zeros_like(img)
red_only[:, :, 0] = red_2d

green_only = np.zeros_like(img)
green_only[:, :, 1] = green_2d

blue_only = np.zeros_like(img)
blue_only[:, :, 2] = blue_2d

# Print summary
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape: {img.shape}")
print(f"Red Channel 2D Shape:   {red_2d.shape} | Mean Intensity: {red_2d.mean():.2f}")
print(f"Green Channel 2D Shape: {green_2d.shape} | Mean Intensity: {green_2d.mean():.2f}")
print(f"Blue Channel 2D Shape:  {blue_2d.shape} | Mean Intensity: {blue_2d.mean():.2f}")

# 4. Display 2x3 Subplot Grid
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Top Row: 3D Color isolations
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only View")
axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only View")
axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only View")

# Bottom Row: 2D Grayscale intensity maps
axes[1, 0].imshow(red_2d, cmap="gray")
axes[1, 0].set_title("Red Intensity Map (2D)")
axes[1, 1].imshow(green_2d, cmap="gray")
axes[1, 1].set_title("Green Intensity Map (2D)")
axes[1, 2].imshow(blue_2d, cmap="gray")
axes[1, 2].set_title("Blue Intensity Map (2D)")

for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()
plt.show()