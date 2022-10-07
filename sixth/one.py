import pandas as pd
import numpy as np
import scipy.stats as sts


def na_handler(data_frame):
    for column in data_frame.columns:
        na = np.mean(data_frame[column].isna() * 100)
        print(f"{column}: {round(na, 1)}%")
    data_frame.drop(['geoId', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'], axis=1,
                    inplace=True)
    med = data_frame['popData2019'].median()
    data_frame.popData2019.fillna(med, inplace=True)
    data_frame['countryterritoryCode'].fillna('other', inplace=True)
    print(data_frame.isna().sum())


def death_count(data_frame):
    print(data_frame.describe())
    death_frame = data_frame[data_frame['deaths'] > 3000]
    print(death_frame['countriesAndTerritories'].unique())
    print(death_frame['dateRep'].unique())
    print("Amount of days: ", len(death_frame['dateRep'].unique()))


def duplicates(data_frame):
    print("Amount of duplicates: ", data_frame.duplicated().sum())
    data_frame.drop_duplicates(inplace=True)
    print("Amount of duplicates after drop: ", data_frame.duplicated().sum())


def bmi_thing(data):
    north = data[data['region'] == 'northwest']
    south = data[data['region'] == 'southwest']
    print("Проверка выборок на нормальность\nСеверозапад: ",
          sts.shapiro(north['bmi']), "\nЮгозапад: ", sts.shapiro(south['bmi']))
    print("Проверка гомогенности дисперсии выборок\n", sts.bartlett(north['bmi'], south['bmi']))
    print("t-критерий Стьюдента\n", sts.ttest_ind(north['bmi'], south['bmi']))


def dice():
    throws = pd.DataFrame(data={'N': [1, 2, 3, 4, 5, 6], 'Observed': [97, 98, 109, 95, 97, 104],
                                'Expected': [100, 100, 100, 100, 100, 100]})
    print(throws.head(6))
    print(sts.chisquare(throws['Observed'], throws['Expected']))


def workload():
    data = pd.DataFrame({'Женат': [89, 17, 11, 43, 22, 1],
                         'Гражданский брак': [80, 22, 20, 35, 6, 4],
                         'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]})
    data.index = ['Полный рабочий день', 'Частичная занятость', 'Временно не работает', 'На домохозяйстве', 'На пенсии',
                  'Учёба']
    print(data.head(6))
    print(sts.chi2_contingency(data)[:3])


if __name__ == '__main__':
    df = pd.read_csv('ECDCCases.csv')
    na_handler(df)
    death_count(df)
    duplicates(df)
    bmi = pd.read_csv('bmi.csv')
    bmi_thing(bmi)
    dice()
    workload()
