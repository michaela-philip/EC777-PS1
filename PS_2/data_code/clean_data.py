import pandas as pd
import numpy as np
import sys
import os
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..', '..'))

market_data = pd.read_csv('PS_1/data/output/market_data.csv')
from PS_1.analysis.q2a import logit_model

market_data['year'] = market_data['year'].astype(str)
market_data['rating_area'] = market_data['rating_area'].astype(str)
market_data['rating_area'] = market_data['rating_area'].str.zfill(2)
market_data['market_id'] = market_data['rating_area'] + market_data['year']
market_data = market_data.dropna(subset=['AV', 'HMO'])
market_data = market_data.drop(market_data.columns[0], axis=1)

#market-year indicator matrix
df = pd.DataFrame(np.repeat(market_data['market_id'].values, market_data.shape[0]).reshape(-1, market_data.shape[0]))
market_year_matrix = (df == df.T).astype(int).values
market_year_matrix_df = pd.DataFrame(market_year_matrix)

#create elasticities matrix
k = market_data.shape[0]
alpha = logit_model.params['avg_price_pp']
elasticities = np.zeros((k, k))

for i in range(k):
    elasticities[:, i] = (-alpha * np.outer(market_data['indiv_share'], market_data['avg_price_pp'].iloc[i]).flatten()) @ market_year_matrix
np.fill_diagonal(elasticities, alpha * market_data['avg_price_pp'] * (1 - market_data['indiv_share']))

#misc
elasticities_df = pd.DataFrame(elasticities)
elasticities_df.to_csv('PS_2/data/output/elasticities.csv')
market_data.isna().sum()
market_data[market_data.isna().any(axis=1)]