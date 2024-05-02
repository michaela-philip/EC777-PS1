import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as smf

def get_own_elasticities(df, alpha):
    grouped = df.groupby(['rating_area', 'year'])
    elasticities = []
    for name, group in grouped:
        share = np.array(group['indiv_share'].values).reshape(-1, 1)
        n = len(share)
        price = np.array(group['avg_price_pp'])
        elast = alpha * price * (1 - share)
        elast = elast.sum()
        avg_elast = elast / n
        elasticities.append(avg_elast)
    ns = len(elasticities)
    return (sum(elasticities) / ns)

def get_cross_elasticities(df, alpha):
    grouped = df.groupby(['rating_area', 'year'])
    elasticities = []
    for name, group in grouped:
        share = np.array(group['indiv_share'].values).reshape(-1, 1)
        n = len(share)
        price = np.array(group['avg_price_pp'])
        elast = - alpha * price * share
        elast = elast.sum()
        avg_elast = elast / n
        elasticities.append(avg_elast)
    ns = len(elasticities)
    return (sum(elasticities) / ns)

share = np.random.rand(10)
total = share.sum()
share = share / total
price = np.random.rand(10)
alpha = 1
