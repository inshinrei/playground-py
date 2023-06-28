import numpy as np
import pandas as pd

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

print(pd.Series(populations, index=index))
