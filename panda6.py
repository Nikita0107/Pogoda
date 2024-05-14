import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject14\Date\311-service-requests.csv',
                       na_values=na_values, dtype={'Incident Zip': str})
# print(requests)
# print(requests['Incident Zip'].unique())

'''Эта функция используется для установки опций, которые влияют на поведение pandas в будущем.
Опция future.no_silent_downcasting относится к изменениям, которые будут внесены в pandas в будущем.
Эта опция предотвращает автоматическое преобразование типов данных (называемое "downcasting"),
которое может привести к потере точности или потере информации.
При вызове этой функции с аргументом True вы указываете,
что вы хотите избежать автоматического преобразования типов данных в будущем.
Это может быть полезно, если вы хотите быть уверены в том,
что ваши данные не потеряют точности или информации из-за изменений в pandas.'''
pd.set_option('future.no_silent_downcasting', True)

rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
# print(len(requests[rows_with_dashes]))
# print(requests[rows_with_dashes]['Incident Zip'])

long_zip_codes = requests['Incident Zip'].str.len() > 5
requests['Incident Zip'][long_zip_codes].unique()
# print(requests['Incident Zip'][long_zip_codes].unique())

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

requests[requests['Incident Zip'] == '00000']

zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

unique_zips = requests['Incident Zip'].unique()
# print(unique_zips)

zips = requests['Incident Zip']
# Давайте предположим, что почтовые индексы, начинающиеся с "0" и "1", пока в порядке.
# (на самом деле это не так - 13221 находится в Сиракузах, и почему?)
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# Есть куча NAN, но сейчас они нас не интересуют, поэтому мы скажем, что они ложные
is_far = ~(is_close) & zips.notnull()
# print(zips[is_far])

# print(requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip'))


print(requests['City'].str.upper().value_counts())

