import pandas as pd
import numpy as np
#written with assistance from Matt Gentry

#calculate mu (consumer-specific term)
def get_mu(c, theta, nu): #c is variables for which we are estimating random coefficients
    sigma = np.diagflat(theta) #theta is our vector of random coefficients but we need a square matrix for this -> we make a diagonal matrix, sigma
    return (c @ sigma @ nu) #Jx1 vector

#predict shares s_jt (function of consumer-independent and consumer-specific terms)
def predict_logit_share(delta, mu): 
    J = len(delta)
    prob = np.exp(delta + mu) 
    sum_prob = 1 + np.sum(prob)
    pred_share = prob / sum_prob
    return pred_share #Jx1 vector

#predict shares for each value of nu (random tastes)
def predict_rc_logit_share(delta, c, theta, nus):
    R = nus.shape[0]
    pred_share = np.zeros(delta.size)
    for r in range(R):
        mu_r = get_mu(c, theta, nus[r,:])
        pred_share_r = predict_logit_share(delta, mu_r)
        pred_share += pred_share_r
    pred_share = pred_share / R
    return pred_share #Jx1 vector

def contraction_map(pred_share, observe_share, initial):
    return initial + np.log(observe_share / pred_share)

def run_inner_loop(c, theta, nus, observe_share, initial, max_iter=10000, tol=1e-12):
    for i in range(max_iter):
        pred_share = predict_rc_logit_share(initial, c, theta, nus)
        delta = contraction_map(pred_share, observe_share, initial)
        if np.abs(delta - initial).max() < tol:
            break
        initial = delta
    return delta, pred_share #two Jx1 vectors
