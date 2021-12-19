import numpy as np

'''
Load data from data/ex3_data.npy and filter out rows with nan values.
Report how many rows are dropped during filtration, globally and how many nan are in each column.
'''

data_path = 'ex3_data.npy'
data = np.load(data_path)
n_of_columns = data.shape[1]

data_filtered = data[~np.isnan(data).any(axis=1)]

for n_of_column in range(n_of_columns):
    nan_indexes = np.where(np.isnan(data[:, n_of_column]))[0]
    print(f'Column {n_of_column} has {len(nan_indexes)} nan records at rows {", ".join(map(str, nan_indexes))}')

nan_records = data[np.isnan(data).any(axis=1)]
print(f'There is a total of {len(nan_records)} rows containing nan records')
