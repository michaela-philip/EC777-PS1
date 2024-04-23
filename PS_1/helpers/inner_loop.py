import pandas as pd
import numpy as np
#written with assistance from Matt Gentry

#calculate mu (consumer-specific term)
def get_mu(c, theta, nu): #c is variables for which we are estimating random coefficients
    sigma = np.diagflat(theta) #theta is our vector of random coefficients but we need a square matrix for this -> we make a diagonal matrix, sigma
    return (c @ sigma @ nu).values #Jx1 vector

#predict shares s_jt (function of consumer-independent and consumer-specific terms)
def predict_logit_share(delta, mu): 
    J = len(delta)
    prob = np.exp(delta + mu) 
    print('prob', prob.mean())
    # print('prob', prob[0:5])
    sum_prob = 1 + np.sum(prob)
    print('sum_prob', sum_prob)
    # print('sum_prob', sum_prob)
    pred_share = prob / sum_prob
    # print('pred_share', pred_share[0:5])
    return pred_share #Jx1 vector

#predict shares for each value of nu (random tastes)
def predict_rc_logit_share(delta, c, theta, nus):
    print('running rc_logit_share')
    R = nus.shape[0]
    pred_share = np.zeros((delta.size, 1))
    # print('delta', delta[0:5])
    for r in range(R):
        nu_r = nus[r,:]
        nu_r = nu_r[:, np.newaxis]
        mu_r = get_mu(c, theta, nu_r)
        print('mu', mu_r.mean())
        # print('mu_', r, mu_r.shape)
        pred_share_r = predict_logit_share(delta, mu_r)
        # print('pred_share_r', pred_share_r[0:5])
        # print('pred_share_r', pred_share_r.shape)
        # print('pred_share', pred_share.shape)
        pred_share += pred_share_r
        # print('pred share', pred_share[0:5])
        # print('pred_share updated', pred_share.shape)
    # print('pred_share before division', pred_share[0:5])
    pred_share = pred_share / R
    # print('pred_share', pred_share[0:5])
    return pred_share #Jx1 vector

def contraction_map(pred_share, observed_share, initial): 
    # return initial + np.log(observed_share / pred_share) #need to make sure that this operation works row by row
    print('initial', initial[0:5], 'observe', observed_share[0:5], 'pred', pred_share[0:5])
    return initial + np.log(observed_share) - np.log(pred_share)


def run_inner_loop(c, theta, nus, observed_share, delta_0, max_iter=10000, tol=1e-12):
    for i in range(max_iter):
        # print('delta_0', delta_0[0:5])
        pred_share = predict_rc_logit_share(delta_0, c, theta, nus) #this is the same every time for some reason
        # print('going to contraction map')
        delta = contraction_map(pred_share, observed_share, delta_0)
        print('delta', delta[0:5])
        print('delta_0', delta_0[0:5])
        if np.abs(delta - delta_0).max() < tol:
            break
        delta_0 = delta
        # print('iteration', i, 'delta', delta_0[0:5])
    return delta, pred_share #two Jx1 vectors

# ###test code###
# x = market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
# z = market_data[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
# c = market_data[['AV', 'HMO']] 
# theta = np.array([nested_logit_AV, nested_logit_HMO])
# observed_share = np.array(market_data['ln_house_share']).reshape(-1, 1)
# W = np.eye(x.shape[1])
# R = 500
# K = c.shape[1]
# # initial = np.array([nested_logit_AV, nested_logit_HMO])

# np.random.seed(123)
# nus = np.random.normal(0, 1, [R,K])

# delta_0 = np.zeros((1929, 1))