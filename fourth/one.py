import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as sts
import numpy as np
import plotly.express as px


def print_hists(frame):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5), sharey=False)
    sns.set_theme()
    sns.histplot(ax=axes[0], data=frame, x="age", hue="smoker", multiple="stack")
    sns.histplot(ax=axes[1], data=frame, x="bmi", hue="smoker", multiple="stack")
    sns.histplot(ax=axes[2], data=frame, x="children", hue="smoker", multiple="stack")
    sns.histplot(ax=axes[3], data=frame, x="charges", hue="smoker", multiple="stack")
    fig.show()


def specs(x, **kwargs):
    plt.axvline(x.mean(), c='k', ls='-', lw=2.5, label="mean")
    plt.axvline(x.median(), c='orange', ls='--', lw=2.5, label="median")
    plt.axvline(x.std(), c='green', ls='-.', lw=2.5, label="std")
    plt.axvline(x.max() - x.min(), c='blue', ls=':', lw=2.5, label="range")
    plt.axvline(sts.iqr(x, interpolation='midpoint'), c='pink', ls='--', lw=2.5, label="iqr")


def task_four(frame):
    sns.set_theme()
    b = sns.displot(data=frame, x="bmi", legend=True)
    b.map(specs, "bmi")
    plt.legend()
    plt.show()
    c = sns.displot(data=frame, x="charges")
    c.map(specs, "charges")
    plt.legend()
    plt.show()
    bmi = frame["bmi"]
    cha = frame["charges"]
    print("\nПоказатели индекса массы тела:")
    print("Среднее = ", np.mean(bmi), "\nМода: ", sts.mode(bmi, keepdims=True), "\nМедиана = ", np.median(bmi),
          "\nСтандартное отклонение: ",
          bmi.std(), "\nРазмах: ", bmi.max() - bmi.min(), "\nМежквадратильный размах: ",
          sts.iqr(bmi, interpolation='midpoint'))
    print("\nПоказатели расходов:")
    print("Среднее = ", np.mean(cha), "\nМода: ", sts.mode(cha, keepdims=True), "\nМедиана = ", np.median(cha),
          "\nСтандартное отклонение: ",
          cha.std(), "\nРазмах: ", cha.max() - cha.min(), "\nМежквадратильный размах: ",
          sts.iqr(cha, interpolation='midpoint'))


def boxes(frame):
    labels = ["age", "bmi", "children", "charges"]
    for x in labels:
        fig = px.box(frame, y=x, title=x)
        fig.update_layout(
            font_size=16,
            title_font_size=20,
            title_x=0.5
        )
        fig.show()


def central_limit(frame):
    num = [1, 10, 50, 100]
    means = []
    for j in num:
        buffer = []
        for i in range(300):
            x = np.mean(np.random.choice(frame["bmi"], j, replace=False))
            buffer.append(x)
        means.append(buffer)
    k = 0
    fig, ax = plt.subplots(2, 2, figsize=(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            ax[i, j].hist(means[k], 10, density=True)
            ax[i, j].set_title(label=num[k])
            k = k + 1
    plt.show()
    for i in range(4):
        print("Среднее значение и стандартное отклонение для распределения выборок длиной ", num[i])
        print("mean: ", np.mean(means[i]), ", std: ", np.std(means[i]))


def trust_interval(frame):
    ti_ch1 = sts.t.interval(confidence=0.95, df=frame["charges"].size - 1, loc=np.mean(frame["charges"]), scale=sts.sem
    (frame["charges"]))
    ti_ch2 = sts.t.interval(confidence=0.99, df=frame["charges"].size - 1, loc=np.mean(frame["charges"]), scale=sts.sem
    (frame["charges"]))
    ti_bmi1 = sts.t.interval(confidence=0.95, df=frame["bmi"].size - 1, loc=np.mean(frame["bmi"]), scale=sts.sem
    (frame["bmi"]))
    ti_bmi2 = sts.t.interval(confidence=0.99, df=frame["bmi"].size - 1, loc=np.mean(frame["bmi"]), scale=sts.sem
    (frame["bmi"]))
    print("95% доверительный интервал для среднего значения расходов: ", ti_ch1,
          "\n99% доверительный интервал для среднего значения расходов: ", ti_ch2,
          "\n95% доверительный интервал для среднего значения индекса массы тела: ", ti_bmi1,
          "\n99% доверительный интервал для среднего значения индекса массы тела: ", ti_bmi2)


if __name__ == '__main__':
    df = pd.read_csv("insurance.csv")
    print(df.describe())
    print(df.head(5))
    print_hists(df)
    task_four(df)
    boxes(df)
    central_limit(df)
    trust_interval(df)
