import pandas as pd
import numpy as np
import scipy.optimize as opt
from helpers.inner_loop import run_inner_loop

def gmm_objective(delta, x, z, beta, W):
    xi = delta - np.matmul(x, beta)
    mom = np.matmul(z.T, xi)
    return np.matmul(mom.T, W, mom)

#solve linear gmm
def get_beta(delta, x, z, W):
    A = np.matmul(x.T, z, W, z.T, x)
    b = np.matmul(x.T, z, W, z.T, delta)
    return np.solve(A, b)

def outer_loop(x, z, c, observe_share, nus, sigma, W):
    def obj_sigma(sigma):
        delta, share = run_inner_loop(c, sigma, nus, observe_share, np.zeros(len(c)))
        beta = get_beta(delta, x, z, W)
        objective = gmm_objective(delta, x, z, beta, W)
        return objective
    result = opt.minimize(obj_sigma, sigma, method='Nelder_Mead')
    return result