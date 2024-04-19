import numpy as np
import pandas as pd
import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.import_data import households, household_plan_year, plans
from helpers.merge_data import merge_data, merge_market_price, merge_household_price
from helpers.shares import get_shares

market_data = get_shares(households)

market_data = merge_data(market_data, plans)
households_plan = merge_data(households, plans)

main = merge_household_price(households_plan, household_plan_year)

main['annual_price'] = (main['premium'] - main['subsidy'] - main['monthly_penalty']) * 12
main['annual_price_pp'] = main['annual_price'] / main['household_size']
market_data = merge_market_price(main, market_data)

main = main.dropna(subset=['rating_area'])
main = main.drop(main[main['plan_name'] == 'Uninsured'].index)

main.to_csv('./data/output/main.csv')
print('main csv created')

market_data.to_csv('./data/output/market_data.csv')
print('market data csv created')