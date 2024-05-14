import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

# Прочтите его и удалите последнюю строку
popcon = pd.read_csv('popularity-contest.txt', sep=' ')[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
# print(popcon[:5])
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

# print(popcon['atime'].dtype)
# print(popcon[:5])

'''В этой строчке кода вы фильтруете DataFrame popcon,
оставляя только те строки, в которых значения в
столбце 'atime' больше '1970-01-01'.
Это делается с помощью маскирования DataFrame,
которое выглядит следующим образом: popcon[popcon['atime'] > '1970-01-01'].'''
popcon = popcon[popcon['atime'] > '1970-01-01']

'''В этом примере вы создаете новый DataFrame nonlibraries,
который содержит только те записи из исходного DataFrame popcon,
которые не относятся к библиотекам. Это полезно,
если вы хотите выполнять анализ или визуализацию только для приложений, а не для библиотек.'''
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

'''В этой строчке кода вы сортируете DataFrame nonlibraries по столбцу 'ctime' в порядке убывания.
Затем вы выбираете первые 10 строк из отсортированного DataFrame с помощью среза [:10].
Это делается с помощью метода sort_values() и среза.'''
print(nonlibraries.sort_values('ctime', ascending=False)[:10])
