import numpy as np
import pandas as pd

from import_data import merged as merged
from helpers.shares import get_shares
from helpers.share_diff import get_diff

market_data = get_shares(merged)

market_data['ln_share'] = np.log(market_data['share'])
share_differences = get_diff(market_data)

market_data = market_data.to_csv('./data/output/market_data.csv', index = False)
share_differences = share_differences.to_csv('./data/output/share_differences.csv', index = False)