import pandas as pd
import seaborn as sns

# На гитхабе файл, сделанный в Google Collab

df = pd.read_csv('sample_data/california_housing_train.csv')
print(df.head(n=10)) #количество эл-то от начала
print()
print(df.tail(n=2)) #колво элементов с хвоста
print()
print(df.shape)
print()
print(df.isnull()) #проверка пустых значений в таблице. если null, то true
print()
print(df.isnull().sum()) #если пустых зн-й в таблице много, то можно вывести общую инфу. Для каждого столбца выведется
# количество false и количество true
print()
print(df.dtypes) # тип данных столбцов
print()
print(df.columns)
print()
# Выборки данных
print(df['latitude'])
print()
print(df[['latitude', 'population']])
print()
# print(df['housing_median_age'] < 10)  #true или false, если возраст здания менее 10 лет
# print()
# print(df[df['housing_median_age'] < 10])  # из прошлых true или false, если возраст здания менее 10 лет делает список только из true
# print()
# print(df[df['housing_median_age'] < 10]['total_rooms'])
# print()
# print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][['total_rooms',  'housing_median_age']])
# df.describe() # вся статистика

# Графики
# import seaborn as sns
sns.scatterplot(data=df, x='longitude', y='latitude')
sns.scatterplot(data=df, x='households', y='population', hue='total_rooms')
sns.scatterplot(data=df, x='households', y='population', hue='total_rooms', size=10)
# работа класса PairGrid
cols=['population', 'median_income', 'housing_median_age', 'median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)
#=================================#
# Пример из трех графиков по анализу роста стоимости домов на определенных долготе и широте в связи с близостью к морю
sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)
sns.scatterplot(data=df, x='latitude', y='longitude', hue='median_house_value')
#=================================#

# Гистограммы
# Анализ возраста, дохода, создание новых групп(столбцов) в DataFrame
sns.histplot(data=df, x="median_income")
sns.histplot(data=df, x="housing_median_age")

sns.histplot(data=df[df["housing_median_age"]>50], x="median_income")

df.loc[df['housing_median_age']<=20, 'housing_median_age']

df.loc[df['housing_median_age']<=20, 'age_group']='Молодые'
df.loc[(df['housing_median_age']>20) & (df['housing_median_age']<=50), 'age_group']='Ср. возраст'
df.loc[df['housing_median_age']>50, 'age_group']='Пожилые'
df.groupby('age_group')['median_income'].mean().plot(kind='bar')
#=================================#
df.loc[df['median_income']>6, 'income_group']='rich'
df.loc[df['median_income']<6, 'income_group']='everyone_else'
df.columns
sns.histplot(data=df, x='median_house_value', hue='income_group')
