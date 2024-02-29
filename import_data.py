import pandas as pd
# import os
# # current = os.getcwd()
# # print(current)

from helpers.read_data import read_data
from helpers.merge_data import merge_data
print('function import complete')

household_plan_year = read_data('./data/input/household_plan_year777.csv', limit = 100)
print('household_plan_year import complete')

households = read_data('./data/input/households777.csv', limit = 100)
print('households import complete')

plans = read_data('./data/input/plans777.csv', limit = 100)
print('plans import complete')

merged = merge_data(household_plan_year, households, plans)
print('merge complete')

print(merged.info())