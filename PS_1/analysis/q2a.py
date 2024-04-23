import pandas as pd
import numpy as np
import sys
import os
import statsmodels.api as sm
from linearmodels.iv import IV2SLS

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
os.chdir('PS_1')

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

#Nested Logit Model
nested_shares = (market_data.groupby(['year', 'rating_area', 'plan_name', 'Metal_Level'])['n_ind'].sum()) / (market_data.groupby(['year', 'rating_area', 'Metal_Level'])['n_ind'].sum())
nested_shares = nested_shares.rename('nested_shares').reset_index()
market_data = pd.merge(market_data, nested_shares, on=['year', 'rating_area', 'plan_name', 'Metal_Level'], how = 'outer')
market_data['ln_nested_shares'] = np.log(market_data['nested_shares'])

exog = pd.get_dummies(market_data[['perc_white', 'perc_male', 'fpl', 'Insurer', 'AV', 'Metal_Level', 'HMO', 'ln_nested_shares']], drop_first=True)

nested_logit_model = IV2SLS(dependent, exog, endog, instrument).fit()
print(nested_logit_model.summary)

#pull coefficients for later use
nested_logit_AV = nested_logit_model.params['AV']
nested_logit_HMO = nested_logit_model.params['HMO']
print(nested_logit_AV, nested_logit_HMO)


###BLP
market_data = pd.read_csv('./data/output/market_data.csv')
market_data = get_instruments(market_data)
market_data = market_data.dropna(subset=['AV', 'HMO'])

from helpers.inner_loop import run_inner_loop, predict_rc_logit_share, get_mu, predict_logit_share
from helpers.outer_loop import outer_loop

x = market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
z = market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
c = market_data[['AV', 'HMO']] 
theta = np.array([nested_logit_AV, nested_logit_HMO])
observed_share = np.array(market_data['house_share'].values).reshape(-1, 1)
delta_0 = np.array(market_data['ln_house_share_diff']).reshape(-1, 1)
W = np.eye(x.shape[1])
R = 500
K = c.shape[1]

R = 500
J = 50
K = 2

c = pd.DataFrame(np.random.rand(J, K))
theta = np.random.rand(K)
observed_share = np.random.rand(J).reshape(-1, 1)
delta_0 = np.zeros(J).reshape(-1, 1)
# np.random.seed(123)
nus = np.random.normal(0, 1, [R,K])

delta, pred_share = run_inner_loop(c, theta, nus, observed_share, delta_0, max_iter=1000, tol=1e-6)
# print(delta, pred_share)

# theta_hat = outer_loop(x, z, c, observed_share, nus, theta, W)
# print(theta_hat)

total_shares = market_data.groupby(['year', 'rating_area'])['house_share'].sum()