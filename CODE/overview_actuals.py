import os
import pandas as pd

file_path = os.path.join('..', 'DATA', 'dataset.csv')

df = pd.read_csv(file_path)
result = df.loc[df['week'] == df['forecasted week']]
result = result.drop(columns=['forecasted week'])

print(result)
