import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import colorsys


st.title("Simple Colour Chart")


# # Fill the grid
# for i in range(grid_size):
#     for j in range(grid_size):
#         hue_adjustment = (j - grid_size // 2) * 10
#         brightness_adjustment = (i - grid_size // 2) * 5
#         adjusted_rgb = center_rgb + np.array([hue_adjustment, 0, 0]) + brightness_adjustment
#         adjusted_rgb = np.clip(adjusted_rgb, 0, 255)  # Ensure values are within RGB range
#         colors[i, j] = adjusted_rgb

# # Convert RGB values back to HEX
# colors_hex = np.array([[rgb_to_hex(tuple(colors[i, j])) for j in range(grid_size)] for i in range(grid_size)])

# # Plot the grid
# fig, ax = plt.subplots(figsize=(8, 8))
# ax.imshow(colors, aspect='equal')

# # Add text annotations for HEX values
# for i in range(grid_size):
#     for j in range(grid_size):
#         ax.text(j, i, colors_hex[i, j], ha='center', va='center', color='white' if np.mean(colors[i, j]) < 128 else 'black')


# # Adjust the grid to add spacing between squares
# fig, ax = plt.subplots(figsize=(8, 8))

# # Adjusting the spacing between squares
# spacing = 0.05
# for i in range(grid_size):
#     for j in range(grid_size):
#         color = colors[i, j] / 255  # Normalize RGB values for imshow
#         rect = plt.Rectangle((j + spacing / 2, i + spacing / 2), 1 - spacing, 1 - spacing, facecolor=color, edgecolor='none')
#         ax.add_patch(rect)
#         ax.text(j + 0.5, i + 0.5, colors_hex[i, j], ha='center', va='center', color='white' if np.mean(colors[i, j]) < 128 else 'black')

# ax.set_xlim(0, grid_size)
# ax.set_ylim(0, grid_size)
# ax.invert_yaxis()
# ax.axis('off')
# st.write(plt.show())

# # Plot the grid
# fig, ax = plt.subplots(figsize=(8, 8))

# # Adjusting the spacing between squares
# spacing = 0.05
# for i in range(grid_size):
#     for j in range(grid_size):
#         color = colors[i, j] / 255  # Normalize RGB values for imshow
#         rect = plt.Rectangle((j + spacing / 2, i + spacing / 2), 1 - spacing, 1 - spacing, facecolor=color, edgecolor='none')
#         ax.add_patch(rect)
#         ax.text(j + 0.5, i + 0.5, colors_hex[i, j], ha='center', va='center', color='white' if np.mean(colors[i, j]) < 128 else 'black')

# ax.set_xlim(0, grid_size)
# ax.set_ylim(0, grid_size)
# ax.invert_yaxis()
# ax.axis('off')

# Display the plot in Streamlit
# st.pyplot(fig)

# Function to adjust shade (darker) or tint (lighter)
def adjust_shade_tint(rgb, factor):
    if factor > 1:  # Tint
        return rgb + (np.array([255, 255, 255]) - rgb) * (factor - 1)
    else:  # Shade
        return rgb * factor

# Function to convert RGB to HEX
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

# Center color in HEX
center_color = st.color_picker('Pick a color', '#59cb55')
st.write(f'Center color: {center_color}')

# Convert center color to RGB
center_rgb = np.array([int(center_color[1:3], 16), int(center_color[3:5], 16), int(center_color[5:7], 16)])

# Create a 10x10 grid with tint and shade adjustments instead of brightness
grid_size = 10
spacing = 0.05

colors = np.zeros((grid_size, grid_size, 3), dtype=int)

# Define tint and shade factors
tint_factors = np.linspace(1.5, 1, grid_size // 2, endpoint=False)
shade_factors = np.linspace(1, 0.5, grid_size // 2 + 1)

# Fill the grid
for i in range(grid_size):
    for j in range(grid_size):
        hue_adjustment = (j - grid_size // 2) * 10
        if i < grid_size // 2:  # Tint
            factor = tint_factors[i]
        else:  # Shade
            factor = shade_factors[i - grid_size // 2]
        h, s, v = colorsys.rgb_to_hsv(center_rgb[0]/255, center_rgb[1]/255, center_rgb[2]/255)
        h = (h + hue_adjustment/360) % 1
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        adjusted_rgb = np.array([r, g, b]) * 255
        adjusted_rgb = adjust_shade_tint(adjusted_rgb, factor)
        adjusted_rgb = np.clip(adjusted_rgb, 0, 255)  # Ensure values are within RGB range
        colors[i, j] = adjusted_rgb

# Convert RGB values back to HEX
colors_hex = np.array([[rgb_to_hex(tuple(colors[i, j].astype(int))) for j in range(grid_size)] for i in range(grid_size)])

# Plot the grid with spacing
fig, ax = plt.subplots(figsize=(8, 8))

for i in range(grid_size):
    for j in range(grid_size):
        color = colors[i, j] / 255  # Normalize RGB values for imshow
        rect = plt.Rectangle((j + spacing / 2, i + spacing / 2), 1 - spacing, 1 - spacing, facecolor=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(j + 0.5, i + 0.5, colors_hex[i, j], ha='center', va='center', color='white' if np.mean(colors[i, j]) < 128 else 'black')

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.invert_yaxis()
ax.axis('off')

# Display the plot on Streamlit
st.pyplot(fig)
