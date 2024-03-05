import numpy as np
import pandas as pd

from import_data import households, household_plan_year, plans
from helpers.merge_household_plan import merge_data
from helpers.shares import get_shares
from helpers.share_diff import get_diff

households_plan = merge_data(households, plans)

market_data = get_shares(households_plan)

market_data.to_csv('./data/output/market_data.csv')

print('market data csv created')