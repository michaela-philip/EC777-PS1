import pandas as pd
import numpy as np

def get_shares(filepath):
    # market_data = pd.DataFrame(columns = ['year', 'rating_area', 'plan_name', 'share'])
    data = []

    for i in filepath['year'].unique():
        for j in filepath['rating_area'].unique():
            total_shares = ((filepath['year']==i) & (filepath['rating_area']==j)).sum()
            # print(str(i) + str(j) + 'total shares calculated')
            for k in filepath['plan_name'].unique():
                share = ((filepath['year']==i) & (filepath['rating_area']==j) & (filepath['plan_name']==k)).sum() / (total_shares)                
                # market_data = market_data.append({'year': i, 'rating_area': j, 'plan_name': k, 'share': share}, ignore_index=True)
                data.append({'year': i, 'rating_area': j, 'plan_name': k, 'share': share})

    market_data = pd.DataFrame(data)
    return market_data            
