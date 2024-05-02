import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as smf
from stargazer.stargazer import Stargazer
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))
# os.chdir('PS_1')

market_data = pd.read_csv('./data/output/market_data.csv')

logit_age = smf.ols(formula = 'ln_indiv_share_diff ~ avg_price_pp + perc_white + perc_male + fpl + Insurer + AV + Metal_Level + HMO + perc_0to17 + perc_18to25 + perc_26to34 + perc_35to44 + perc_45to54 + perc_55to64 + perc_65plus + avg_price_pp*perc_0to17 + avg_price_pp*perc_18to25 + avg_price_pp*perc_26to34 + avg_price_pp*perc_35to44 + avg_price_pp*perc_45to54 + avg_price_pp*perc_55to64 + avg_price_pp*perc_65plus', data = market_data).fit()
logit_age_stargazer = Stargazer([logit_age])
