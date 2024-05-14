"""Анализ данных с помощью pandas"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

fixed_df = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject13\Date\bikes.csv',
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
# fixed_df['Berri 1'].plot()
fixed_df.plot(figsize=(15, 10))
plt.show()

