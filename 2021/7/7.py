"""Solution for day 7"""

import csv
import numpy as np

# Part 1

# Read number of positions of the crab submarines
with open("locations.csv", encoding='UTF-8') as f:
    # File has only one row - using next on the reader to get it
    locations_list = next(csv.reader(f))

# Convert locations_list to a numpy array
locations_np = np.array(locations_list, dtype=int)

# Optimal position is just the median of all initial locations (equal to minimizing MAE)
opt_position = np.median(locations_np).astype(int)

# Total fuel consumption is the sum of all movements
total_fuel = np.abs(locations_np - opt_position).sum()

print(f"Optimal position: {opt_position}")
print(f"Total fuel consumption: {total_fuel}")
print('------')


# Part 2

# We could use an optimization algorithm here (like scipy.minimize), but we stick with numpy for now

# All possible optimal positions with an extra axis (for broadcasting)
opt_positions_np = np.expand_dims(np.arange(locations_np.min(), locations_np.max()+1), axis=1)
# Locations with an extra axis (for broadcasting)
locations_np = np.expand_dims(locations_np, axis=0)
# Fuel consumption for EVERY crab submarine for every possible optimal position
fuel_array_np = np.abs(locations_np - opt_positions_np) * (np.abs(locations_np - opt_positions_np) + 1) / 2
# Total fuel consumption for ALL crab submarine for every possible optimal position
total_fuel_np = fuel_array_np.sum(axis=1)

# Now we can simply find the minimum and its location
total_fuel = total_fuel_np.min()
opt_position = total_fuel_np.argmin()

print(f"Optimal position: {int(opt_position)}")
print(f"Total fuel consumption: {int(total_fuel)}")
