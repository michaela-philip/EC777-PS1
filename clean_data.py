import numpy as np
import pandas as pd

from import_data import merged as merged

print(merged.head())

merged['uninsured'] = np.where(merged['monthly_penalty'] > 0, 1, 0)
