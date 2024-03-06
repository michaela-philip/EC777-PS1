import pandas as pd

def merge_data(filepath1, filepath2):
    output = pd.merge(filepath1, filepath2, on='plan_name', how = 'outer')

    return output
    print("household plan merge complete")