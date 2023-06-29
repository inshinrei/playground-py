import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# print(pd.Series([0.25, 0.5, 0.75, 1.0]))
# print(pd.Series([0.25, 0.3, 1.2, 1.3], index=['a', 'b', 'c', 'd']))

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

# print(pd.Series(population_dict))

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}

# print(pd.DataFrame({'p': pd.Series(population_dict), 'a': pd.Series(area_dict)}))
# print(pd.Series(np.random.RandomState(42).randint(0, 10, 4)))

index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]


# print(pd.Series(populations, index=index))

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)


births = pd.read_csv('mocks/births.csv')
print(births.head())
births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')

sns.set()
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year')
plt.show()

quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

goog = data.DataReader('GOOG', start='2004', end='2016',
                       data_source='google')
goog.head()

fig, ax = plt.subplots(2)
data = goog.iloc[:10]

data.asfreq('D').plot(ax=ax[0], marker='o')

data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(["back-fill", "forward-fill"]);
