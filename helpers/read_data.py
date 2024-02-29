import pandas as pd

def read_data(filepath, limit= None):
    output = pd.read_csv(filepath, nrows = limit)
    output = output.drop(output.columns[0], axis=1)

    return output

