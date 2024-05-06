import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as smf
from stargazer.stargazer import Stargazer
from linearmodels.iv import IV2SLS
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
# os.chdir('PS_1')

market_data_cf = pd.read_csv('./data/output/market_data_cf.csv')

from helpers.instruments import get_instruments

market_data_cf = get_instruments(market_data_cf)

#Logit Model
endog = market_data_cf['avg_price_pp']
exog = pd.get_dummies(market_data_cf[['perc_white', 'perc_male', 'fpl', 'Insurer', 'AV', 'Metal_Level', 'HMO']], drop_first=True)
dependent = market_data_cf['ln_indiv_share_diff']
instrument = market_data_cf['instrument']

logit_cf = IV2SLS(dependent, exog, endog, instrument).fit()
logit_cf_stargazer = Stargazer([logit_cf])