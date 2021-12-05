"""Solution for day 5"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Part 1

# Read line coordinates
with open('lines.txt', 'r', encoding='UTF-8') as f:
    lines_list = f.read().splitlines()

# Prepare clean dataframe (one column per coordinate)
line_coords_df = pd.DataFrame(lines_list)[0].str.split(' -> ', expand=True)
# Because we have just two columns to split, do it explicitly
line_coords_df[['x0', 'y0']] = line_coords_df[0].str.split(',', expand=True).astype(int)
line_coords_df[['x1', 'y1']] = line_coords_df[1].str.split(',', expand=True).astype(int)
# Drop temporary columns
line_coords_df.drop(columns=[0, 1], inplace=True)

# Get line equations and type (h - horizontal, v - vertical, d - diagonal)
line_coords_df['a'] = line_coords_df['y0'] - line_coords_df['y1']
line_coords_df['b'] = line_coords_df['x1'] - line_coords_df['x0']
line_coords_df['c'] = -line_coords_df['b'] * line_coords_df['y0'] - line_coords_df['a'] * line_coords_df['x0']
line_coords_df['type'] = np.select([line_coords_df['a'] == 0, line_coords_df['b'] == 0], ['h', 'v'], default='d')

# Get maximum coordinates to set the grid size
x_max = line_coords_df[['x0', 'x1']].max().max() + 1
y_max = line_coords_df[['y0', 'y1']].max().max() + 1

# Prepare numpy grid
grid_np = np.zeros([x_max, y_max], dtype=int)

# For part 1 we only need horizontal or vertical lines
for i, row in line_coords_df.iterrows():
    if row['type'] == 'h':
        points_x = np.linspace(row['x0'], row['x1'], num=abs(row['x0'] - row['x1']) + 1, dtype=int)
        points_y = np.ones_like(points_x) * row['y0']
        grid_np[points_y, points_x] += 1
    elif row['type'] == 'v':
        points_y = np.linspace(row['y0'], row['y1'], num=abs(row['y0'] - row['y1']) + 1, dtype=int)
        points_x = np.ones_like(points_y) * row['x0']
        grid_np[points_y, points_x] += 1

# Calculate number of dangerous areas
intersects = np.count_nonzero(grid_np >= 2)
print(grid_np)
print(f"Number of dangerous areas: {intersects}")

# Add a heatmap just for fun
fig, ax = plt.subplots()
x, y = np.meshgrid(np.arange(x_max),np.arange(y_max))
ax.pcolormesh(x, y, grid_np, cmap='inferno', shading='nearest')
fig.savefig('plots/heatmap_hv.png', bbox_inches='tight', pad_inches=0.1)


# Part 2
print('\nAdd diagonals')

# Iterate again over the data and add diagonal lines
for i, row in line_coords_df.iterrows():
    if row['type'] == 'd':
        points_x = np.linspace(row['x0'], row['x1'], num=abs(row['x0'] - row['x1']) + 1, dtype=int)
        points_y = np.linspace(row['y0'], row['y1'], num=abs(row['y0'] - row['y1']) + 1, dtype=int)
        grid_np[points_y, points_x] += 1

# Calculate number of dangerous areas
intersects = np.count_nonzero(grid_np >= 2)
print(grid_np)
print(f"Number of dangerous areas: {intersects}")

# Add a heatmap just for fun
ax.pcolormesh(x, y, grid_np, cmap='inferno', shading='nearest')
fig.savefig('plots/heatmap_hvd.png', bbox_inches='tight', pad_inches=0.1)
