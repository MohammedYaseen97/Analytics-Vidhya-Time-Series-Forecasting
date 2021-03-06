import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing    #Holt Winter Method

import os
import config

df = pd.read_csv(os.path.join(config.INPUT_PATH, 'train.csv'))
df.head()

train = df[:14736]
val = df[14736:]

val.head()

train.Count.plot(figsize=(15, 8), title='Daily Ridership', fontsize=14)
val.Count.plot(figsize=(15, 8), title='Daily Ridership', fontsize=14)
plt.show()

y_hat_avg = val.copy() #This line helps copy the index of the val observations for plotting
model = ExponentialSmoothing(np.asarray(train.Count), seasonal_periods=7*24, trend='add', seasonal='add').fit()
y_hat_avg['Holt_Winter'] = model.forecast(len(val))

plt.figure(figsize=(16,8))
plt.plot(train['Count'], label='Train')
plt.plot(val['Count'], label='Val')
plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
plt.legend(loc='best')
plt.show()