"""Solution for day 3"""

import pandas as pd

# Part 1

# Load report into a dataframe
report_df = pd.read_csv('report.csv', sep=' ', dtype=str)

# Split binary number into single digits and put them into a new dataframe (one column by bit)
report_split_df = report_df['bin'].apply(lambda x: pd.Series(list(x))).astype(int)

# Calculate sum for each column
sums = report_split_df.sum().tolist()

# Calculate gamma rate
gamma_rate_list = [int(x > report_df.shape[0] / 2) for x in sums]
gamma_rate = int(''.join(map(str, gamma_rate_list)), 2)

# Calculate epsilon rate
epsilon_rate_list = [int(x < report_df.shape[0] / 2) for x in sums]
epsilon_rate = int(''.join(map(str, epsilon_rate_list)), 2)
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {gamma_rate*epsilon_rate}")

# Part 2

# Get new dataframe for oxygen generator
oxy_gen_filter_df = report_split_df.copy()

# Filter dataframe until only one binary number is left
for i in range(oxy_gen_filter_df.shape[1]):
    sums_f = oxy_gen_filter_df.sum().tolist()
    filtered_list = [int(x >= oxy_gen_filter_df.shape[0] / 2) for x in sums_f]
    oxy_gen_filter_df = oxy_gen_filter_df[oxy_gen_filter_df.iloc[:, i] == filtered_list[i]]
    if oxy_gen_filter_df.shape[0] == 1:
        break

# Get new dataframe for CO2 scrubber
co2_scrubber_filter_df = report_split_df.copy()

# Filter dataframe until only one binary number is left
for i in range(co2_scrubber_filter_df.shape[1]):
    sums_f = co2_scrubber_filter_df.sum().tolist()
    filtered_list = [int(x < co2_scrubber_filter_df.shape[0] / 2) for x in sums_f]
    co2_scrubber_filter_df = co2_scrubber_filter_df[co2_scrubber_filter_df.iloc[:, i] == filtered_list[i]]
    if co2_scrubber_filter_df.shape[0] == 1:
        break

# Calculate oxygen generator rating
oxy_gen_rating_list = oxy_gen_filter_df.iloc[0].tolist()
oxy_gen_rating = int(''.join(map(str, oxy_gen_rating_list)), 2)

# Calculate CO2 scrubber rating
co2_scrubber_rating_list = co2_scrubber_filter_df.iloc[0].tolist()
co2_scrubber_rating = int(''.join(map(str, co2_scrubber_rating_list)), 2)

print("----------")
print(f"Oxygen generator rating: {oxy_gen_rating}")
print(f"CO2 scrubber rating: {co2_scrubber_rating}")
print(f"Life support rating: {oxy_gen_rating*co2_scrubber_rating}")
