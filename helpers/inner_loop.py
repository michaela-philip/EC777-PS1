import pandas as pd
import numpy as np

#calculate mu
def get_mu(x, sigma, nu):
    return np.matmul(x, nu*sigma)

#predict shares
def predict_logit_share(delta, mu):
    J = len(delta)
    prob = np.exp(delta + mu) 
    sum_prob = 1 + np.sum(prob)
    pred_share = prob / sum_prob
    return pred_share

def predict_rc_logit_share(delta, x, sigma, nus):
    R = nus.shape[1]
    pred_share = np.zeros(delta.size)
    for r in range(R):
        mu_r = get_mu(x, sigma, nus[r,:])
        pred_share_r = predict_logit_share(delta, mu_r)
        pred_share += pred_share_r
    pred_share = pred_share / R
    return pred_share

def contraction_map(pred_share, observe_share, initial):
    return initial + np.log(observe_share / pred_share)

def run_inner_loop(x, sigma, nus, observe_share, initial, max_iter=10000, tol=1e-12):
    for i in range(max_iter):
        pred_share = predict_rc_logit_share(initial, x, sigma, nus)
        delta = contraction_map(pred_share, observe_share, initial)
        if np.abs(delta - initial).max() < tol:
            break
        initial = delta
    return delta, pred_share