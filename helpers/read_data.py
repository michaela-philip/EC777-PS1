import pandas as pd

def read_data(filepath, limit= None):
    output = pd.read_csv(filepath, nrows = limit)

    return output

