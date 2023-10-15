import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
import os
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")

# Read the data, print the dimensions of the data, print the 7 random rows
data = pd.read_csv('./s_p_stock/NDAQ.csv')
# print(data.shape)
# print(data.sample(7))


# Convert the data to the DataTime data type of Pandas. Print result
data['date'] = pd.to_datetime(data['Date'])
data.info()

print()

# date vs open
# date vs close
# plt.figure(figsize=(15, 8))
# for index, company in enumerate(companies, 1):
# 	plt.subplot(3, 3, index)
# 	c = data[data['Name'] == company]
# 	plt.plot(c['date'], c['close'], c="r", label="close", marker="+")
# 	plt.plot(c['date'], c['open'], c="g", label="open", marker="^")
# 	plt.title(company)
# 	plt.legend()
# 	plt.tight_layout()
