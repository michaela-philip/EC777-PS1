import pandas as pd
import numpy as np
import scipy.optimize as opt
from helpers.inner_loop import run_inner_loop, market_year_inner_loop
#written with assistance from Matt Gentry

#THE BIG IDEA
#for random taste draws (nus) find delta
#using delta, calculate the objective function 
#the obective function is linear in beta, so we can solve for beta in closed form 
#given delta and beta, we can optimize over sigma using Nelder Mead, where sigma is our random coefficient

#define the objective function
def gmm_objective(delta, x, z, beta, W):
    delta = delta.values
    x = x.values
    z = z.values
    xi = delta - np.matmul(x, beta)
    mom = np.matmul(z.T, xi)
    temp = np.matmul(mom.T, W)
    return np.matmul(temp, mom)
    # return np.matmul(mom.T, W, mom)

#get closed form solution for beta - this allows us to only optimize over sigma
def get_beta(delta, x, z, W):
    x = x.values
    z = z.values
    delta = delta.values
    # W = W.values

    temp = np.matmul(x.T, z)
    temp = np.matmul(temp, W)
    A = np.matmul(temp, z.T)
    A = np.matmul(A, x)

    temp2 = np.matmul(x.T, z)
    temp2 = np.matmul(temp2, W)
    b = np.matmul(temp2, z.T)
    b = np.matmul(b, delta)

    return np.linalg.solve(A, b)

def outer_loop(x, z, c, observe_share, nus, theta, W): 
    def obj_theta(theta):
        delta, share = run_inner_loop(c, theta, nus, observe_share, np.zeros(len(c)))
        beta = get_beta(delta, x, z, W)
        objective = gmm_objective(delta, x, z, beta, W)
        return objective
    print("got objective function")
    result = opt.minimize(obj_theta, theta, method='Nelder-Mead')
    return result

def callback(xk):
    print(f"Iteration: {callback.iteration}, x = {xk}")
    callback.iteration +=1

callback.iteration = 0

def market_year_outer_loop(market_data, theta, nus, R, K):
    beta = None
    def obj_theta(theta):
        nonlocal beta
        delta_all = market_year_inner_loop(market_data, theta, nus)
        delta = delta_all['delta']
        x = pd.get_dummies(market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh']], dtype=float)
        z = pd.get_dummies(market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'instrument']], dtype=float)
        W = np.eye(x.shape[1])
        beta = get_beta(delta, x, z, W)
        objective = gmm_objective(delta, x, z, beta, W)
        return objective
    print("got objective function")
    result = opt.minimize(obj_theta, theta, method='Nelder-Mead', callback=callback, tol = 1e-9)
    return result, beta