import os
import pandas as pd

file_path = os.path.join('..', 'DATA', 'dataset.csv')

df = pd.read_csv(file_path)

# Select rows where customer is 'Dreamland' and product is 'Dinosaur'
DreamDino = df[(df['customer'] == 'DreamLand') & (df['product'] == 'Dinosaur')]
x = DreamDino['week'].max()
y = DreamDino['forecasted week'].max()
DreamDinoPresent = pd.DataFrame(index=range(x), columns=range(y))
for a in range(0,x,1):
    for b in range(0,y,1):
        Selectie = DreamDino[(DreamDino['week'] == a) & (DreamDino['forecasted week'] == b)]
        #DreamDinoPresent.iloc[a,b] = Selectie.iloc[0,4]
        print(f"({a},{b}) = {Selectie.iloc[0,4]}")
