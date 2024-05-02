import pandas as pd
import numpy as np

def get_shares(filepath):

    n_ind = filepath.groupby(['year', 'rating_area', 'plan_name'])['household_size'].sum()
    n_house = filepath.groupby(['year', 'rating_area', 'plan_name'])['household_size'].size()
    perc_white = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_white'].mean()
    fpl = filepath.groupby(['year', 'rating_area', 'plan_name'])['FPL'].mean()
    perc_male = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_male'].mean()
    perc_0to17 = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_0to17'].mean()
    perc_18to25 = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_18to25'].mean()
    perc_26to34 = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_26to34'].mean()
    perc_35to44 = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_35to44'].mean()
    perc_45to54 = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_45to54'].mean()
    perc_55to64 = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_55to64'].mean()
    perc_65plus = filepath.groupby(['year', 'rating_area', 'plan_name'])['perc_65plus'].mean()

    market_level = pd.concat({'n_ind': n_ind, 'n_house' : n_house, 'perc_white' : perc_white, 'fpl' : fpl, 'perc_male' : perc_male, 'perc_0to17' : perc_0to17, 'perc_18to25' : perc_18to25, 'perc_26to34' : perc_26to34, 'perc_35to44' : perc_35to44, 'perc_45to54' : perc_45to54, 'perc_55to64' : perc_55to64, 'perc_65plus' : perc_65plus}, axis=1).reset_index()
    print(market_level.head())

    indiv_share = (market_level.groupby(['year', 'rating_area', 'plan_name'])['n_ind'].sum()) / (market_level.groupby(['year', 'rating_area'])['n_ind'].sum())
    indiv_share = indiv_share.rename('indiv_share').reset_index()
    house_share = (market_level.groupby(['year', 'rating_area', 'plan_name'])['n_house'].sum()) / (market_level.groupby(['year', 'rating_area'])['n_house'].sum())
    house_share = house_share.rename('house_share').reset_index()

    market_level = pd.merge(market_level, indiv_share, on=['year', 'rating_area', 'plan_name'], how = 'outer')
    market_level = pd.merge(market_level, house_share, on=['year', 'rating_area', 'plan_name'], how = 'outer')
    print(market_level.head())

    market_level['ln_indiv_share'] = np.log(market_level['indiv_share'])
    market_level['ln_house_share'] = np.log(market_level['house_share'])

    ln_uninsured_indiv = market_level.loc[market_level['plan_name'] == 'Uninsured', ['ln_indiv_share', 'year', 'rating_area']]
    ln_uninsured_indiv = ln_uninsured_indiv.rename(columns={ln_uninsured_indiv.columns[0]: 'ln_uninsured_indiv'})
    ln_uninsured_house = market_level.loc[market_level['plan_name'] == 'Uninsured', ['ln_house_share', 'year', 'rating_area']]
    ln_uninsured_house = ln_uninsured_house.rename(columns={ln_uninsured_house.columns[0]: 'ln_uninsured_house'})
    print(ln_uninsured_indiv.head())
    print(ln_uninsured_house.head())

    market_level = pd.merge(market_level, ln_uninsured_indiv, on=['year', 'rating_area'], how = 'outer')
    market_level = pd.merge(market_level, ln_uninsured_house, on=['year', 'rating_area'], how = 'outer')
    print(market_level.head())


    market_level['ln_indiv_share_diff'] = market_level['ln_indiv_share'] - market_level['ln_uninsured_indiv']
    market_level['ln_house_share_diff'] = market_level['ln_house_share'] - market_level['ln_uninsured_house']    
    
    # market_level = pd.merge(market_level, filepath, on = 'plan_name', how = 'outer')

    return market_level