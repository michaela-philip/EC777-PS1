import numpy as np
import pandas as pd
import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.import_data import households, household_plan_year, plans
from helpers.merge_data import merge_data, merge_market_price, merge_household_price
from helpers.shares import get_shares

market_data_cf = get_shares(households)

market_data_cf = merge_data(market_data_cf, plans)
households_plan = merge_data(households, plans)

main_cf = merge_household_price(households_plan, household_plan_year)

#don't include penalty for counterfactual
main_cf['annual_price'] = (main_cf['premium'] - main_cf['subsidy']) * 12
main_cf['annual_price_pp'] = main_cf['annual_price'] / main_cf['household_size']
market_data_cf = merge_market_price(main_cf, market_data_cf)

main_cf = main_cf.dropna(subset=['rating_area'])
main_cf = main_cf.drop(main_cf[main_cf['plan_name'] == 'Uninsured'].index)

main_cf.to_csv('./data/output/main_cf.csv')
print('main csv cf created')

market_data_cf.to_csv('./data/output/market_data_cf.csv')
print('market data cf csv created')