import pandas as pd

def get_instruments(filepath):
    avg_prices = filepath.groupby(['year', 'plan_name', 'rating_area'])['annual_price_pp'].mean().reset_index()

    def calculate_instrument(row):
        mask = (avg_prices['year'] == row['year']) & (avg_prices['plan_name'] == row['plan_name']) & (avg_prices['rating_area'] != row['rating_area'])
        return avg_prices.loc[mask, 'annual_price_pp'].mean()

    filepath['instrument'] = filepath.apply(calculate_instrument, axis=1)

    return filepath