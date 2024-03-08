import pandas as pd

def merge_data(filepath1, filepath2):
    output = pd.merge(filepath1, filepath2, on='plan_name', how = 'outer')

    return output
    print("household plan merge complete")

def merge_market_price(main, market_data):
    avg_price_pp = main.groupby(['year', 'rating_area', 'plan_name'])['annual_price_pp'].mean()
    avg_price_pp = avg_price_pp.rename('avg_price_pp').reset_index()
    avg_price_hh = main.groupby(['year', 'rating_area', 'plan_name'])['annual_price'].mean()
    avg_price_hh = avg_price_hh.rename('avg_price_hh').reset_index()
    market_data = pd.merge(market_data, avg_price_pp, on=['year', 'rating_area', 'plan_name'])
    market_data = pd.merge(market_data, avg_price_hh, on=['year', 'rating_area', 'plan_name'])

    return market_data

def merge_household_price(households, prices):
    output = pd.merge(households, prices, on=['household_id', 'year', 'plan_name'], how = 'outer')
    
    return output