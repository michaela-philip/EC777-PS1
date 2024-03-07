import pandas as pd
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from helpers.read_data import read_data
from helpers.merge_data import merge_data
print('function import complete')

household_plan_year = read_data('./data/input/household_plan_year777.csv')
print('household_plan_year import complete')
household_plan_year.to_csv('./data/output/household_plan_year.csv')

households = read_data('./data/input/households777.csv')
print('households import complete')
households.rename(columns = {'choice': 'plan_name'}, inplace = True)
households.to_csv('./data/output/households.csv')


plans = read_data('./data/input/plans777.csv')
print('plans import complete')
plans.to_csv('./data/output/plans.csv')
