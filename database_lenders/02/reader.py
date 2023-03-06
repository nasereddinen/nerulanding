import os

import pandas as pd

dir_name = 'database_lenders/02'

csvs = os.listdir(dir_name)

for i in csvs:
    if ".py" in i or "revised" in i or ".DS_Store" in i:
        continue
    print(i)
    data = pd.read_csv(f'{dir_name}/{i}').fillna('-').replace(regex=r',', value='.')
    newcols = []
    for col in data.columns:
        if col in ['Created at', 'Updated at']:
            data.drop(col, axis=1, inplace=True)
        else:
            newcols.append(col.replace(" ", "_").lower())
    data.columns = newcols
    data.to_csv(f'{dir_name}/revised/{i}')
