import pandas as pd
import numpy as np
import sys
import os
import statsmodels.api as sm
from linearmodels.iv import IV2SLS
import scipy.optimize as opt

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from helpers.inner_loop import run_inner_loop, predict_rc_logit_share, get_mu, predict_logit_share
from helpers.outer_loop import outer_loop

#testing using fake numbers
J = 50
R = 500
K = 2   # Num random coefficients
Y = 15 #other observable characteristics
nus = np.random.normal(0, 1, [R,K])
x = np.random.rand(J,Y)
sigma = np.random.rand(K, K)
delta = np.random.rand(J)
z = np.random.rand(J,(K+Y))
W = np.eye((K+Y))
c = np.random.rand(J, K)

# share_0 = predict_rc_logit_share(delta, x, sigma, nus)

# delta_1, share_1 = run_inner_loop(c, sigma, nus, share_0, np.zeros(J))

mu = get_mu(c, sigma, nus[0,:])
# theta = outer_loop(x, z, c, np.ones(J), nus, sigma, W)