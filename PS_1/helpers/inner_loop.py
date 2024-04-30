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
    sum_prob = 1 + np.sum(prob)
    if sum_prob == 'nan':
        print('sum_prob is nan')
    pred_share = prob / sum_prob
    return pred_share #Jx1 vector

#predict shares for each value of nu (random tastes)
def predict_rc_logit_share(delta, c, theta, nus):
    R = nus.shape[0]
    pred_share = np.zeros((delta.size, 1))
    for r in range(R):
        nu_r = nus[r,:]
        nu_r = nu_r[:, np.newaxis]
        mu_r = get_mu(c, theta, nu_r)
        pred_share_r = predict_logit_share(delta, mu_r)
        pred_share += pred_share_r
    pred_share = pred_share / R
    return pred_share #Jx1 vector

def contraction_map(pred_share, observed_share, initial): 
    return initial + np.log(observed_share / pred_share) #need to make sure that this operation works row by row

def run_inner_loop(c, theta, nus, observed_share, delta_0, max_iter=10000, tol=1e-12):
    for i in range(max_iter):
        pred_share = predict_rc_logit_share(delta_0, c, theta, nus) 
        delta = contraction_map(pred_share, observed_share, delta_0)
        if np.abs(delta - delta_0).max() < tol:
            print('converged', i)
            break
        delta_0 = delta
    return delta, pred_share #Jx1 vectors

def market_year_inner_loop(df, theta, nus):
    grouped = df.groupby(['rating_area', 'year'])
    delta_all = []
    for name, group in grouped:
        print('starting', name)
        x = group[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
        z = group[['Insurer', 'AV', 'Metal_Level', 'HMO', 'avg_price_hh', 'instrument']]
        c = group[['AV', 'HMO']] 
        observed_share = np.array(group['house_share'].values).reshape(-1, 1)
        delta_0 = np.array(group['ln_house_share_diff']).reshape(-1, 1)
        W = np.eye(x.shape[1])
        R = 500
        K = c.shape[1]
        delta, pred_share = run_inner_loop(c, theta, nus, observed_share, delta_0, max_iter=10000, tol=1e-12)
        delta_df = pd.DataFrame(delta, columns=['delta'])
        delta_df['group'] = str(name)
        # Append the delta DataFrame to delta_all list
        delta_all.append(delta_df)
        print(name , ' done')

    # Concatenate all DataFrames in the list into a single DataFrame
    delta_all = pd.concat(delta_all, ignore_index=True)

    return delta_all