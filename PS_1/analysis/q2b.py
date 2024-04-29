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

from helpers.inner_loop import run_inner_loop, predict_rc_logit_share, get_mu, predict_logit_share, market_year_inner_loop
from helpers.outer_loop import outer_loop, market_year_outer_loop
from helpers.instruments import get_instruments

market_data = pd.read_csv('./data/output/market_data.csv')
market_data = get_instruments(market_data)
from analysis.q2a import nested_logit_AV, nested_logit_HMO, logit_stargazer, nested_logit_stargazer

np.random.seed(123)
R = 500
K = 2
nus = np.random.normal(0, 1, [R,K])
theta = np.array([nested_logit_AV, nested_logit_HMO])

#run BLP
theta_2, beta = market_year_outer_loop(market_data, theta, nus, 500, 2)