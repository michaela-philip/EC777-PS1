import pandas as pd

def merge_data(filepath1, filepath2):
    output = pd.merge(filepath1, filepath2, on='plan_name', how = 'outer')

    return output
    print("household plan merge complete")

def merge_market_household(household, market, plan):
    # market_minimal = market.drop(columns = ['indiv_share', 'house_share', 'ln_indiv_share', 'ln_house_share', 'ln_uninsured_indiv', 'ln_uninsured_house'])
    # intermed = pd.merge(household, market_minimal, on=['year', 'rating_area', 'plan_name'], how = 'outer')
    # output = pd.merge(intermed, plan, on = ['household_id', 'plan_name', 'year'], how = 'outer')
    output = pd.merge(household, market, on=['year', 'rating_area', 'plan_name'], how = 'outer')
    output = pd.merge(output, plan, on ='year', how = 'outer')
    return output