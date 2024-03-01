import numpy as np
import pandas as pd

def get_diff(df):
    data = []

    for j in df['year'].unique():
        for k in df['rating_area'].unique():
            ln_share_uninsured = df[(df['plan_name'] == 'Uninsured') & (df['year'] == j) & (df['rating_area'] == k)]['ln_share'].values
            print("ln share uninsured calculated")
            for i in df[df['plan_name'] != 'Uninsured']['plan_name'].unique():
                ln_share_i = df[(df['plan_name'] != 'Uninsured') & (df['year'] == j) & (df['rating_area'] == k)]['ln_share'].values
                if ln_share_uninsured.size > 0:
                    diff = ln_share_i - ln_share_uninsured
                else:
                    diff = np.nan
                data.append({'year': j, 'rating_area': k, 'plan_name': i, 'diff': diff})

    share_diff = pd.DataFrame(data)
    return share_diff