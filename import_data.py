import pandas as pd

from helpers.read_data import read_data
from helpers.merge_household_plan import merge_data
print('function import complete')

household_plan_year = read_data('./data/input/household_plan_year777.csv')
print('household_plan_year import complete')
print(household_plan_year.info())

households = read_data('./data/input/households777.csv')
print('households import complete')
households.rename(columns = {'choice': 'plan_name'}, inplace = True)
print(households.info())

plans = read_data('./data/input/plans777.csv')
print('plans import complete')
print(plans.info())

