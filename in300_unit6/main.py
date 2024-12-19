import pandas as pd

data = 'in300_dataset1.csv'

nd = pd.read_csv(data, sep=',')
print(nd)

y = nd[['No.', 'Source', 'Destination']]
print(y)