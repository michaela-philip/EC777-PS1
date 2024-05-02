import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as smf
from stargazer.stargazer import Stargazer
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
os.chdir('PS_1')

from analysis.q2a import logit_model, nested_logit_model
from helpers.elasticities import get_own_elasticities, get_cross_elasticities

market_data = pd.read_csv('./data/output/market_data.csv')
market_data = market_data.dropna(subset=['AV', 'HMO'])
market_data = market_data[market_data['house_share']>=0.01]

alpha = logit_model.params['avg_price_pp']
logit_own_elast = get_own_elasticities(market_data, alpha)
logit_cross_elast = get_cross_elasticities(market_data, alpha)
logit_elast = [logit_own_elast, logit_cross_elast]

alpha = nested_logit_model.params['avg_price_pp']
nested_logit_own_elast = get_own_elasticities(market_data, alpha)
nested_logit_cross_elast = get_cross_elasticities(market_data, alpha)
nested_logit_elast = [nested_logit_own_elast, nested_logit_cross_elast]