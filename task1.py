import math

print("--- TASK 1: DISPLAY PIXEL DENSITY CALCULATOR ---")

# 1. Inputs
w_px = int(input("Enter horizontal resolution (pixels): "))
h_px = int(input("Enter vertical resolution (pixels): "))
d_inches = float(input("Enter physical diagonal size (inches): "))

# 2. Calculations
total_pixels = w_px * h_px
gcd_val = math.gcd(w_px, h_px)
aspect_w = w_px // gcd_val
aspect_h = h_px // gcd_val

# Diagonal pixels Pd = sqrt(W^2 + H^2)
p_d = math.sqrt(w_px**2 + h_px**2)
dpi = p_d / d_inches

# 3. Classification
if dpi < 100:
    category = "Low Density (Standard Monitor)"
elif 100 <= dpi <= 200:
    category = "Medium Density (HD Display)"
else:
    category = "High Density (Retina / Mobile)"

# Display Results
print("\n--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count: {total_pixels:,} pixels")
print(f"Aspect Ratio:      {aspect_w}:{aspect_h}")
print(f"Calculated DPI:    {dpi:.2f} DPI")
print(f"Density Category:  {category}\n")
