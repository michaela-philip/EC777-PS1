import pandas as pd

def merge_data(filepath1, filepath2):
    output = pd.merge(filepath1, filepath2, on='plan_name', how = 'outer')
    print("household merge complete")
    # print(output.head())

    return output
    print("household plan merge complete")