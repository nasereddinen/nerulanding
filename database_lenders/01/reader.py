import os

import pandas as pd

csvs = os.listdir('database_lenders')

for i in csvs:
    if ".py" in i or "revised" in i or ".DS_Store" in i:
        continue
    print(i)
    data = pd.read_csv(f'database_lenders/{i}').fillna('-').replace(regex=r',', value='.')
    newcols = []
    for col in data.columns:
        if col in ['Created at', 'Updated at']:
            data.drop(col, axis=1, inplace=True)
        else:
            newcols.append(col.replace(" ", "_").lower())
    data.columns = newcols

    data = data.set_index("id")
    data.to_csv(f'database_lenders/revised/{i}')
