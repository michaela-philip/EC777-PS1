import pandas as pd

def merge_data(filepath1, filepath2, filepath3):
    merge_household = pd.merge(filepath1, filepath2, on=['household_id', 'year', 'plan_name'], how = 'left')
    print("household merge complete")
    print(merge_household.head())

    full_merge = pd.merge(merge_household, filepath3, on='plan_name', how = 'left')

    return full_merge
    print("full merge complete")