import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

print("--- TASK 4: SPATIAL DOWNSAMPLING & PIXELATION ---")

image_path = "sample.jpg"

# Agar sample.jpg nahi hai toh auto-generate kar lega
if not os.path.exists(image_path):
    temp = np.zeros((300, 400, 3), dtype=np.uint8)
    temp[0:150, 0:200] = [255, 0, 0]
    temp[0:150, 200:400] = [0, 255, 0]
    temp[150:300, 0:200] = [0, 0, 255]
    temp[150:300, 200:400] = [255, 255, 255]
    Image.fromarray(temp).save(image_path)

# 1. Load image into numpy array
img = np.array(Image.open(image_path).convert("RGB"), dtype=np.uint8)

N = 8

# 2. Downsample taking every N-th pixel (slice step)
downsampled = img[::N, ::N, :]

# 3. Re-expand back using np.repeat across axes 0 and 1
re_expanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)

# Ensure dimensions match exactly with original image
re_expanded = re_expanded[:img.shape[0], :img.shape[1], :]

# 4. Calculate reductions and memory savings
orig_bytes = img.nbytes
down_bytes = downsampled.nbytes
dim_reduction = (1 - (1 / N)) * 100
mem_savings = ((orig_bytes - down_bytes) / orig_bytes) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N={N}) ---")
print(f"Original Shape:      {img.shape} | Memory: {orig_bytes:,} bytes")
print(f"Downsampled Shape:   {downsampled.shape} | Memory: {down_bytes:,} bytes")
print(f"Re-expanded Shape:   {re_expanded.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings:      {mem_savings:.2f}% data reduction")

# 5. Display visual output
fig, axes = plt.subplots(1, 3, figsize=(14, 5))

axes[0].imshow(img)
axes[0].set_title("Original Image")

axes[1].imshow(downsampled)
axes[1].set_title(f"Downsampled (1/{N} scale)")

axes[2].imshow(re_expanded)
axes[2].set_title("Pixelated (Re-expanded)")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()