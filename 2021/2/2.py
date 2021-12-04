"""Solution for day 2"""

import pandas as pd

# Part 1

# Load commands into a dataframe
commands_df = pd.read_csv('commands.csv', sep=' ')

# Calculate total movements
total_forward = commands_df[commands_df['command'] == 'forward']['amount'].sum()
total_down = commands_df[commands_df['command'] == 'down']['amount'].sum()
total_up = commands_df[commands_df['command'] == 'up']['amount'].sum()

# Calculate final depth
final_depth = total_down - total_up

print('Total movement:')
print(f"\t Forward: {total_forward}")
print(f"\t Up: {total_up}")
print(f"\t Down: {total_down}")
print(f"\t Final depth: {final_depth}")
print(f"Result is {total_forward*final_depth}")
print('\n')

# Part 2
aim_list = []
current_aim = 0

# Calculate aim for each command
for index, row in commands_df.iterrows():
    if row['command'] == 'down':
        current_aim = current_aim + row['amount']
    elif row['command'] == 'up':
        current_aim = current_aim - row['amount']
    aim_list.append(current_aim)

# Add aim to commands dataframe
commands_df['aim'] = pd.Series(aim_list)

# Create new dataframe for movements
movement_df = commands_df[commands_df['command'] == 'forward'].copy()
movement_df.drop(columns=['command'], inplace=True)

# Calculate final position
movement_df['x_pos'] = movement_df['amount'].cumsum()
movement_df['depth'] = (movement_df['amount'] * commands_df['aim']).cumsum()

print(f"Final depth with aim is {movement_df['depth'].iloc[-1]}")
print(f"Result is {movement_df['depth'].iloc[-1] * total_forward}")
