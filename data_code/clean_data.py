import numpy as np
import pandas as pd
import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.import_data import households, household_plan_year, plans
from helpers.merge_data import merge_data, merge_market_household
from helpers.shares import get_shares

households_plan = merge_data(households, plans)

market_data = get_shares(households_plan)

main = merge_market_household(households, market_data, household_plan_year)

main['annual_price'] = (main['premium'] - main['subsidy'] - main['monthly_penalty']) * 12
main['annual_price_pp'] = main['annual_price'] / main['household_size']
main = main.dropna(subset=['rating_area'])

avg_price_pp = main.groupby(['year', 'rating_area', 'plan_name'])['annual_price_pp'].mean()
avg_price_hh = main.groupby(['year', 'rating_area', 'plan_name'])['annual_price'].mean()
market_data = pd.merge(market_data, avg_price_pp, on=['year', 'rating_area', 'plan_name'])
market_data = pd.merge(market_data, avg_price_hh, on=['year', 'rating_area', 'plan_name'])

main.to_csv('./data/output/main.csv')
print('main csv created')

market_data.to_csv('./data/output/market_data.csv')
print('market data csv created')