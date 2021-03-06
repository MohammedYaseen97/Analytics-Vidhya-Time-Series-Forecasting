import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing    #Holt Winter Method

import config

train = pd.read_csv(os.path.join(config.INPUT_PATH, 'train.csv'))
test = pd.read_csv(os.path.join(config.INPUT_PATH, 'test.csv'))

y_hat_avg = test.copy() #This line helps copy the index of the val observations for plotting
model = ExponentialSmoothing(np.asarray(train.Count), seasonal_periods=7*24, trend='add', seasonal='add').fit()
y_hat_avg['Holt_Winter'] = model.forecast(len(test))

test['Count'] = round(y_hat_avg['Holt_Winter'])

test.to_csv(os.path.join(config.INPUT_PATH, 'predictions_holt_winter.csv'), columns = ['ID', 'Count'], index = False)