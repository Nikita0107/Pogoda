import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

complaints = pd.read_csv(r'C:\Users\niksi\PycharmProjects\pythonProject14\Date\311-service-requests.csv')

# срез 5 строк
print(complaints[:5])

# срез 5 строк, столбца Complaint Typ
print(complaints[:5]['Complaint Type'])

# Выбор нескольких столбцов (две пары квадратных скобок) + срез 10 строк
print(complaints[['Complaint Type', 'Borough']][:10])

# самый частый тип по столбцу Complaint Type
print(complaints['Complaint Type'].value_counts())


# 10 наиболее частых типов:
complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts[:10])

# Строим график
complaint_counts[:10].plot(kind='bar')  # Чтобы построить столбчатую диаграмму, необходимо добавить аргумент kind='bar'
plt.show()