import pandas as pd
import numpy as np

def get_shares(filepath):

    n_ind = filepath.groupby(['year', 'rating_area', 'plan_name'])['household_size'].sum()
    n_house = filepath.groupby(['year', 'rating_area', 'plan_name'])['household_size'].size()

    market_level = pd.concat({'n_ind': n_ind, 'n_house' : n_house}, axis=1)

    market_level['indiv_share'] = (market_level.groupby(['year', 'rating_area', 'plan_name'])['n_ind'].sum()) / (market_level.groupby(['year', 'rating_area'])['n_ind'].sum())
    market_level['house_share'] = (market_level.groupby(['year', 'rating_area', 'plan_name'])['n_house'].size()) / (market_level.groupby(['year', 'rating_area'])['n_house'].size())

    market_level['ln_indiv_share'] = np.log(market_level['indiv_share'])
    market_level['ln_house_share'] = np.log(market_level['house_share'])

    ln_uninsured_indiv = market_level.loc([market_level['plan_name'] == 'uninsured', 'ln_indiv_share'])
    market_level['ln_uninsured_indiv'] = market_level.groupby(['year', 'rating_area'])['ln_indiv_share'].transform(lambda x: ln_uninsured_indiv.get(x.index))
    market_level['ln_indiv_share_diff'] = market_level['ln_indiv_share'] - market_level['uninsured_ln_indiv_share']

    ln_uninsured_house = market_level.loc([market_level['plan_name'] == 'uninsured', 'ln_house_share'])
    market_level['ln_uninsured_house'] = market_level.groupby(['year', 'rating_area'])['ln_house_share'].transform(lambda x: ln_uninsured_house.get(x.index))
    market_level['ln_house_share_diff'] = market_level['ln_house_share'] - market_level['uninsured_ln_house_share']    

    return market_level