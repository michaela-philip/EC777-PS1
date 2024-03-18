import pandas as pd
import numpy as np
import sys
import os
import statsmodels.api as sm
from linearmodels.iv import IV2SLS

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from helpers.inner_loop import run_inner_loop, predict_rc_logit_share

#testing using fake numbers
J = 50
R = 500
K = 2   # Num random coefficients
nus = np.random.normal(0, 1, [R,K])
x = np.random.rand(J,K)
sigma = np.random.rand(K)
delta = np.random.rand(J)

share_0 = predict_rc_logit_share(delta, x, sigma, nus)

delta_1, share_1 = run_inner_loop(x, sigma, nus, share_0, np.zeros(J))