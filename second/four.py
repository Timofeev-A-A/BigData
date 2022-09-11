import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing


if __name__ == '__main__':
    data = fetch_california_housing(as_frame=True)
    df = pd.concat([data.data, data.target], axis=1)
    df.info()
    print(df.isna().sum())
    a = df['HouseAge'] > 50  # Первое условие фильтра
    b = df['Population'] > 2500  # Второе условие фильтра
    print(df.loc[a & b])
    print("Minimal MedHouseVal: ", df['MedHouseVal'].min())
    print("Maximal MedHouseVal: ", df['MedHouseVal'].max())
    print(df.mean(axis=0))
