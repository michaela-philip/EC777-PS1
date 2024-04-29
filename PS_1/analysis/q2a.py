import pandas as pd
import numpy as np
import sys
import os
import statsmodels.api as sm
from linearmodels.iv import IV2SLS
from stargazer.stargazer import Stargazer
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
# os.chdir('PS_1')

from helpers.instruments import get_instruments

market_data = pd.read_csv('./data/output/market_data.csv')
market_data = get_instruments(market_data)
market_data = market_data.dropna(subset=['AV', 'HMO'])
market_data = market_data[market_data['house_share'] >= 0.01]


#Logit Model
endog = market_data['avg_price_pp']
exog = pd.get_dummies(market_data[['perc_white', 'perc_male', 'fpl', 'Insurer', 'AV', 'Metal_Level', 'HMO']], drop_first=True)
dependent = market_data['ln_indiv_share_diff']
instrument = market_data['instrument']

logit_model = IV2SLS(dependent, exog, endog, instrument).fit()
print(logit_model.summary)
logit_stargazer = Stargazer([logit_model])


#Nested Logit Model
nested_shares = (market_data.groupby(['year', 'rating_area', 'plan_name', 'Metal_Level'])['n_ind'].sum()) / (market_data.groupby(['year', 'rating_area', 'Metal_Level'])['n_ind'].sum())
nested_shares = nested_shares.rename('nested_shares').reset_index()
market_data = pd.merge(market_data, nested_shares, on=['year', 'rating_area', 'plan_name', 'Metal_Level'], how = 'outer')
market_data['ln_nested_shares'] = np.log(market_data['nested_shares'])

exog = pd.get_dummies(market_data[['perc_white', 'perc_male', 'fpl', 'Insurer', 'AV', 'Metal_Level', 'HMO', 'ln_nested_shares']], drop_first=True)

nested_logit_model = IV2SLS(dependent, exog, endog, instrument).fit()
print(nested_logit_model.summary)
nested_logit_stargazer = Stargazer([nested_logit_model])


#pull coefficients for later use
nested_logit_AV = nested_logit_model.params['AV']
nested_logit_HMO = nested_logit_model.params['HMO']
print(nested_logit_AV, nested_logit_HMO)