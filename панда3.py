import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики

plt.rcParams['figure.figsize'] = (10, 5) # Размер картинок
#
# bikes = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject13\Date\bikes.csv',
#                     sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
#
# '''
# encoding='latin1': Этот аргумент указывает на кодировку символов файла.
#     'latin1' — это тип кодировки, который поддерживает западноевропейский набор символов.
# parse_dates=['Date']: Указывает, что столбец 'Date' должен быть проанализирован как дата,
#     что позволяет использовать даты в качестве временных меток в DataFrame.
# dayfirst=True: Этот аргумент говорит функции, что первым в дате идет день, а не месяц,
#     что важно для правильного преобразования строк в даты, особенно когда данные содержат даты в формате,
#     отличном от американского стандарта (где месяц идет первым).
# index_col='Date': Определяет столбец 'Date' как индекс DataFrame,
#     что позволяет выполнять операции с данными, используя даты в качестве ключей.
# '''
#
# # bikes['Berri 1'].plot()
# # plt.show()
#
# berri_bikes = bikes[['Berri 1']].copy()
# # print(berri_bikes[:5])
# # print(berri_bikes.index)
# # print(berri_bikes.index.day) # день месяца для каждой строки!
# # print(berri_bikes.index.weekday) # день недели
# '''Это дни недели, 0 - понедельник.
# Теперь, когда мы знаем, как получить день недели, мы можем добавить его как столбец в dataframe.'''
# berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
# # print(berri_bikes[:5])
# weekday_counts = berri_bikes.groupby('weekday').sum()
# # print(weekday_counts)
# weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# # print(weekday_counts)
#
# # weekday_counts.plot(kind='bar')
# # plt.show()

bikes = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject13\Date\bikes.csv',
                     sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

# Добавьте столбец "День недели"
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

# Подсчитайте количество велосипедистов по дням недели и рассчитайте график!
weekday_counts = berri_bikes.groupby('weekday').sum()
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)
weekday_counts.plot(kind='bar')
plt.show()