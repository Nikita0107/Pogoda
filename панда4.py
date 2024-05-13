import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
"""plt.rcParams['font.family'] = 'sans-serif' — это способ установить семейство шрифта по умолчанию для всех
графиков в Matplotlib.
1 В Matplotlib свойство font.family может принимать одно из следующих значений:
«serif», «sans-serif», «cursive», «fantasy» и «monospace».
Каждое семейство шрифтов имеет список имён шрифтов по умолчанию в порядке убывания приоритета. 1"""
plt.rcParams['font.family'] = 'sans-serif'

# weather_2012_final = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject14\Date\weather_2012.csv',
#                                  index_col='Date/Time')
# weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
# plt.show()
# url_template = ("https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={"
#                 "year}&Month={month}&timeframe=1&submit=Download+Data")
url_template = ("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?stationID=5415&Year={year}&Month={"
                "month}&format=csv&timeframe=1&submit=%20Download+Data")

url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='utf-8-sig')
print(weather_mar2012)
