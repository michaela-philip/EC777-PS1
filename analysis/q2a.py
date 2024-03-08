import pandas as pd
import sys
import os
import statsmodels.api as sm
from linearmodels.iv import IV2SLS

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from helpers.instruments import get_instruments

market_data = pd.read_csv('./data/output/market_data.csv')
market_data = get_instruments(market_data)

endog = market_data['annual_price_pp']
exog = market_data['perc_white', 'perc_male', 'fpl', ]