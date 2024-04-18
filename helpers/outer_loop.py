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
    temp = np.matmul(mom.T, W)
    return np.matmul(temp, mom)
    # return np.matmul(mom.T, W, mom)

#get closed form solution for beta - this allows us to only optimize over sigma
def get_beta(delta, x, z, W):
    temp = np.matmul(x.T, z)
    temp = np.matmul(temp, W)
    A = np.matmul(temp, z.T)
    A = np.matmul(A, x)

    temp2 = np.matmul(x.T, z)
    temp2 = np.matmul(temp2, W)
    b = np.matmul(temp2, z.T)
    b = np.matmul(b, delta)
    return np.linalg.solve(A, b)

def outer_loop(x, z, c, observe_share, nus, sigma, W): 
    def obj_sigma(sigma):
        delta, share = run_inner_loop(c, sigma, nus, observe_share, np.zeros(len(c)))
        beta = get_beta(delta, x, z, W)
        objective = gmm_objective(delta, x, z, beta, W)
        return objective
    print("got objective function")
    result = opt.minimize(obj_sigma, sigma, method='Nelder-Mead')
    return result