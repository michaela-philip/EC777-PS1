import pandas as pd
import numpy as np
import sys
import os
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..', '..'))

###Game Plan
#use FOC and estimates from PS1 to estimate marginal cost
#for counterfactual - marginal cost won't change
#simulate change in penalty -> recalculate shares -> reestimate elasticities (use logit)
#using NEW elasticities aka matrix D and OLD marginal cost, calculate NEW vector p

from PS2.data_code.clean_data import elasticities, market_data

#obtain marginal cost vector
p = market_data['avg_price_pp']
s = market_data['indiv_share']
mc = p - (np.linalg.solve(elasticities, s))
