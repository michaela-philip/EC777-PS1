import pandas as pd
import numpy as np
import scipy.optimize as opt
from helpers.inner_loop import run_inner_loop
#written with assistance from Matt Gentry

#THE BIG IDEA
#for random taste draws (nus) find delta
#using delta, calculate the objective function 
#the obective function is linear in beta, so we can solve for beta in closed form 
#given delta and beta, we can optimize over sigma using Nelder Mead, where sigma is our random coefficient

#define the objective function
def gmm_objective(delta, x, z, beta, W):
    xi = delta - np.matmul(x, beta)
    mom = np.matmul(z.T, xi)
    return np.matmul(mom.T, W, mom)

#get closed form solution for beta - this allows us to only optimize over sigma
def get_beta(delta, x, z, W):
    A = np.matmul(x.T, z, W, z.T, x)
    b = np.matmul(x.T, z, W, z.T, delta)
    return np.solve(A, b)

def outer_loop(x, z, c, observe_share, nus, sigma, W): #c is variables for which we are estimating random coefficients
    def obj_sigma(sigma):
        delta, share = run_inner_loop(c, sigma, nus, observe_share, np.zeros(len(c)))
        beta = get_beta(delta, x, z, W)
        objective = gmm_objective(delta, x, z, beta, W)
        return objective
    result = opt.minimize(obj_sigma, sigma, method='Nelder_Mead')
    return result