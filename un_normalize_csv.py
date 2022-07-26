# For un-normalizing the data after predictions have been made by a neural network

import pandas as pd


def un_normalize_1_1(dat):
    global data_min
    global data_max
    unscaled = data_min + ((data_max - data_min) * (dat + 1) / 2)
    return unscaled


minmax_df = pd.read_pickle("x_y_min_max.pkl")
data_min = minmax_df.values[1]
data_max = minmax_df.values[0]
y_df = pd.read_csv('y_predictions.csv')
y_df = y_df.applymap(un_normalize_1_1)
y_df.to_csv('y_predictions_un_normalized.csv', index=False)
