import pandas as pd
import numpy as np
import sys
import os
import statsmodels.api as sm
from linearmodels.iv import IV2SLS
import scipy.optimize as opt

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
os.chdir('PS_1')

from helpers.inner_loop import run_inner_loop, predict_rc_logit_share, get_mu, predict_logit_share
from helpers.outer_loop import outer_loop
from helpers.instruments import get_instruments

market_data = pd.read_csv('./data/output/market_data.csv')
market_data = get_instruments(market_data)
# from analysis.q2a import nested_logit_AV, nested_logit_HMO

#testing using fake numbers
J = 50
R = 500
K = 2   # Num random coefficients
Y = 15 #other observable characteristics
nus = np.random.normal(0, 1, [R,K])
x = np.random.rand(J,(K+Y))
# sigma = np.random.rand(K, K)
delta = np.random.rand(J)
z = np.random.rand(J,(K+Y))
W = np.eye((K+Y))
c = np.random.rand(J, K)
theta = np.random.rand(K)

#test inner loop functions
# mu = get_mu(c, theta, nus[0,:])
# logit_share_test = predict_logit_share(delta, mu)
share_0 = predict_rc_logit_share(delta, c, theta, nus)
# delta_1, share_1 = run_inner_loop(c, theta, nus, share_0, np.zeros(J))


#test outer loop functions
# beta = get_beta(delta, x, z, W)
# obj = gmm_objective(delta, x, z, beta, W)
theta_2 = outer_loop(x, z, c, share_0, nus, theta, W)

# #creating matrices
# market_data = get_instruments(market_data)

# x = market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
# z = market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
# c = market_data[['Metal_Level', 'HMO']] 
# theta = np.array([nested_logit_AV, nested_logit_HMO])
# observed_share = market_data['ln_house_share']
# W = np.eye(x.shape[1])