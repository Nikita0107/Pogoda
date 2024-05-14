"""Анализ данных с помощью pandas"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

fixed_df = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject13\Date\bikes.csv',
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
# 3 строки DataFrame
# print(fixed_df[:3])

# первые 10 значений из столбца 'Berri 1'
# print(fixed_df['Berri 1'][:10])

# Строим график по данным из столбца 'Berri 1'
fixed_df['Berri 1'].plot()

# Добавляем подписи к осям и заголовок графика
plt.xlabel('Дата')
plt.ylabel('Количество')
plt.title('График поездок на велосипеде по датам')
# plt.show()

# Строим график по всем данным DataFrame
fixed_df.plot()
plt.show()

column_sum = fixed_df['Rachel1'].sum()
print(column_sum)
