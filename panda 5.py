import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject14\weather_2012.csv',
                           parse_dates=True, index_col='Date/Time (LST)')
# print(weather_2012[:5])

# Выборка колонки 'Weather' из датафрейма
weather_description = weather_2012['Weather']
# Создание булевой серии, где True, если в описании погоды есть слово 'Snow'
is_snowing = weather_description.str.contains('Snow')

# print(is_snowing[:5])

# Преобразование в целые числа (True - 1, False - 0)
is_snowing2 = is_snowing.astype(int)

is_snowing2.plot()
# plt.show()
weather_2012['Temp (C)'].resample('ME').median().plot(kind='bar')
# plt.show()
# Группировка данных по температуре по месяцам и расчет медианы, построение столбчатого графика
is_snowing.astype(int).resample('ME').mean()
# print(is_snowing.astype(int)[:10])

# Группировка данных о снегопаде по месяцам и расчет среднего, вывод результатов
# print(is_snowing.astype(int).resample('ME').mean())
#
# # Построение столбчатого графика среднего количества снегопадов по месяцам
# is_snowing.astype(int).resample('ME').mean().plot(kind='bar')
# # Отображение графика
# plt.show()

# Группировка и расчет медианы температуры по месяцам
temperature = weather_2012['Temp (C)'].resample('ME').median()
# Повторное создание серии is_snowing для учета обновлений
is_snowing = weather_2012['Weather'].str.contains('Snow')
# Группировка и расчет среднего количества снегопадов по месяцам
snowiness = is_snowing.astype(int).resample('ME').mean()

# Имя столбца
temperature.name = "Temperature"
snowiness.name = "Snowiness"

# Объединение двух серий в один датафрейм по оси колонок
stats = pd.concat([temperature, snowiness], axis=1)
# print(stats)
# stats.plot(kind='bar')
# plt.show()

stats.plot(kind='bar', subplots=True, figsize=(15, 10))
plt.show()