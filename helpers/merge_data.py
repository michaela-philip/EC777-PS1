import pandas as pd

def merge_data(filepath1, filepath2, filepath3):
    merge_household = pd.merge(filepath1, filepath2, on='household_id')
    full_merge = pd.merge(merge_household, filepath3, on='plan_name')

    return full_merge