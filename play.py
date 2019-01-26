import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = pd.read_csv('kickstarter-projects/ks-projects-201801.csv')


data = pd.read_csv('./winequality-red.csv')


# alcohol = data['alcohol'].values
# volatile = data['volatile acidity'].values
# quality = data['quality'].values

# plt.plot(volatile, quality)
# plt.show()

pd.plotting.scatter_matrix(data, alpha=0.3, figsize=(40, 40), diagonal='kde')
plt.rcParams.update({'font.size': 3})
plt.show()
