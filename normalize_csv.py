# for use after csv_maker.py
# For my specific use case I'm dropping all addresses that are short because ragged tensors later on cause issues
# Also the min/max stuff doesn't like NaN values
import pandas as pd


# Normalizes data between -1 and 1 for neural networks
def normalize_1_1(dat):
    global data_min
    global data_max
    scaled = (2 * ((dat - data_min) / (data_max - data_min))) - 1
    return scaled


x_df = pd.read_csv("addresses.csv")
y_df = pd.read_csv("keys.csv")
inds = pd.isnull(x_df).any(1).to_numpy().nonzero()
for i in inds[0]:
    x_df.drop(index=i, inplace=True)
    y_df.drop(index=i, inplace=True)
x_max = x_df.to_numpy().max()
x_min = x_df.to_numpy().min()
y_max = y_df.to_numpy().max()
y_min = y_df.to_numpy().min()
data_min = min(x_min, y_min)
data_max = max(x_max, y_max)
x_df = x_df.applymap(normalize_1_1)
y_df = y_df.applymap(normalize_1_1)

minmax_dict = {'Max': [data_max], 'Min': [data_min]}
minmax_df = pd.DataFrame.from_dict(minmax_dict)
print(minmax_df)

x_df.to_csv("x_processed_normalized.csv", index=False)
y_df.to_csv("y_processed_normalized.csv", index=False)
minmax_df.to_pickle("x_y_min_max.pkl")
