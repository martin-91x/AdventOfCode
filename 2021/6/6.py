"""Solution for day 6"""

import csv
import numpy as np

# Part 1

# Number of simulation days
NR_DAYS = 80

# Read number of lanternfish
with open("lanternfish.csv", encoding='UTF-8') as f:
    # Numbers file has only one row - using next on the reader to get it
    lanternfish_list = next(csv.reader(f))

# Convert lanternfish_list to a numpy array
lanternfish_np = np.array(lanternfish_list, dtype=int)

# Run simulation (explicit)
for day in range(NR_DAYS):
    lanternfish_np = lanternfish_np - 1
    new_fish_np = np.ones(np.count_nonzero(lanternfish_np == -1), dtype=int) * 8
    # Reset days to 6
    lanternfish_np[lanternfish_np == -1] = 6
    # Combine current fishes with new fishes
    lanternfish_np = np.concatenate((lanternfish_np, new_fish_np))

print(f"Number of lanternfish after {NR_DAYS} days: {lanternfish_np.shape[0]}")


# Part 2
# Explicit approach from part 1 does not work for that many days, we need a more clever idea

NR_DAYS = 256

# Reset our numpy array
lanternfish_np = np.array(lanternfish_list, dtype=int)

# Create a list of buckets (index i holds the number of lanternfish to create a new one in i days)
bucket_list = []
for remaining_days in range(7):
    bucket_list.append(np.count_nonzero(lanternfish_np == remaining_days))

# Add two more (empty) buckets for new lanternfish
bucket_list.append(0)
bucket_list.append(0)

# Run simulation
for day in range(NR_DAYS):
    day_mod = (day % 7)
    temp = bucket_list[day_mod]
    bucket_list[day_mod] = bucket_list[day_mod] + bucket_list[7]
    bucket_list[7] = bucket_list[8]
    bucket_list[8] = temp

print(f"Number of lanternfish after {NR_DAYS} days: {sum(bucket_list)}")
