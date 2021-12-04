"""Solution for day 1"""

import pandas as pd

# Part 1

# Load data into dataframe
depth_df = pd.read_csv('depths.csv')
# Calculate differences
depth_df['diff'] = depth_df['depth'].diff()
print(f"Number of measurements larger than the previous: {depth_df[depth_df['diff'] > 0].count()[1]}")

# Part 2

# Calculate rolling average and difference
depth_df['depth_window'] = depth_df['depth'].rolling(3).sum()
depth_df['diff_window'] = depth_df['depth_window'].diff()
print(f"Number of measurements larger than the previous (window mode):"
      f"{depth_df[depth_df['diff_window'] > 0].count()[1]}")
