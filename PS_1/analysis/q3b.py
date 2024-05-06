import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as smf
from stargazer.stargazer import Stargazer
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
# os.chdir('PS_1')

from analysis.q2c import logit_age
from helpers.elasticities import get_cross_elasticities, get_own_elasticities
from helpers.instruments import get_instruments

market_data = pd.read_csv('./data/output/market_data.csv')
market_data = get_instruments(market_data)
market_data = market_data.dropna(subset=['AV', 'HMO'])
market_data = market_data[market_data['house_share']>=0.01]

alpha0 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_0to17']
alpha18 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_18to25']
alpha26 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_26to34']
alpha35 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_35to44']
alpha45 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_45to54']
alpha55 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_55to64']
alpha65 = logit_age.params['avg_price_pp'] + logit_age.params['avg_price_pp:perc_65plus']
                                                              
own_0 = get_own_elasticities(market_data, alpha0)
cross_0 = get_cross_elasticities(market_data, alpha0)
elast_0 = pd.DataFrame([own_0, cross_0]).T

own_18 = get_own_elasticities(market_data, alpha18)
cross_18 = get_cross_elasticities(market_data, alpha18)
elast_18 = pd.DataFrame([own_18, cross_18]).T

own_26 = get_own_elasticities(market_data, alpha26)
cross_26 = get_cross_elasticities(market_data, alpha26)
elast_26 = pd.DataFrame([own_26, cross_26]).T

own_35 = get_own_elasticities(market_data, alpha35)
cross_35 = get_cross_elasticities(market_data, alpha35)
elast_35 = pd.DataFrame([own_35, cross_35]).T

own_45 = get_own_elasticities(market_data, alpha45)
cross_45 = get_cross_elasticities(market_data, alpha45)
elast_45 = pd.DataFrame([own_45, cross_45]).T

own_55 = get_own_elasticities(market_data, alpha55)
cross_55 = get_cross_elasticities(market_data, alpha55)
elast_55 = pd.DataFrame([own_55, cross_55]).T

own_65 = get_own_elasticities(market_data, alpha65)
cross_65 = get_cross_elasticities(market_data, alpha65)
elast_65 = pd.DataFrame([own_65, cross_65]).T

age_elasticities = pd.concat([elast_0, elast_18, elast_26, elast_35, elast_45, elast_55, elast_65], axis=0)
age_elasticities.columns = ['Own Price Elasticity', 'Cross Price Elasticity']
age_elasticities.index = ['Age 0 to 17', 'Age 18 to 26', 'Age 27 to 35', 'Age 36 to 45', 'Age 46 to 55', 'Age 56 to 64', 'Age 65 and up']