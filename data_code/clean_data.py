import numpy as np
import pandas as pd
import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.import_data import households, household_plan_year, plans
from helpers.merge_household_plan import merge_data
from helpers.shares import get_shares
from helpers.merge_market_household import merge_market_household

households_plan = merge_data(households, plans)

market_data = get_shares(households_plan)
market_data.to_csv('./data/output/market_data.csv')
print('market data csv created')

main = merge_market_household(households, market_data, household_plan_year)

main['annual_price'] = (main['premium'] - main['subsidy']) * 12

main.to_csv('./data/output/main.csv')