import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as smf
from stargazer.stargazer import Stargazer
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

main = pd.read_csv('./data/output/main.csv')

#Logit Model
endog = market_data['avg_price_pp']
exog = pd.get_dummies(market_data[['perc_white', 'perc_male', 'fpl', 'Insurer', 'AV', 'Metal_Level', 'HMO']], drop_first=True)
dependent = market_data['ln_indiv_share_diff']
instrument = market_data['instrument']

logit_model = IV2SLS(dependent, exog, endog, instrument).fit()
# print(logit_model.summary)
# logit_stargazer = Stargazer([logit_model])

logit_age = smf.ols(formula = 'ln_indiv_share_diff ~ avg_price_pp + perc_white + perc_male + fpl + Insurer + AV + Metal_Level + HMO + ')