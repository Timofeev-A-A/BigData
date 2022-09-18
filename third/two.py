import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import plotly


def one(data):
    zero = int(data['total'].min() - (data['total'].min() * 0.1))
    zero2 = int(data['total'].max() + (data['total'].max() * 0.05))
    plt.bar(data['district'], data['total'])
    plt.title("Amount of electors in districts", fontsize=20)
    plt.xlabel('Districts', fontsize=16)
    plt.ylabel('total amount', fontsize=16)
    plt.xticks(np.arange(start=0,stop=len(data)), rotation=270, size=10)
    plt.yticks(np.arange(start=zero, stop=zero2, step=600))
    plt.show()


def two(data):
    plt.pie(data['total'], labels=data['district'])
    plt.title("Amount of electors in districts", fontsize=20)
    plt.show()


def three(data):
    zero = int(data['total'].min() - (data['total'].min() * 0.1))
    zero2 = int(data['total'].max() + (data['total'].max() * 0.05))
    plt.plot(data['district'], data['total'], marker='.', color='crimson',
             markerfacecolor='darkblue', markeredgecolor='black', linewidth=2, markersize=4)
    plt.title("Amount of electors in districts", fontsize=20)
    plt.xlabel('Districts', fontsize=16)
    plt.ylabel('total amount', fontsize=16)
    plt.xticks(np.arange(start=0, stop=len(data)), rotation=270, size=10)
    plt.yticks(np.arange(start=zero, stop=zero2, step=600))
    plt.show()


def four(data):
    plt.title("Amount of electors in districts", fontsize=20)
    plt.boxplot(data['total'])
    plt.show()


if __name__ == '__main__':
    df = plotly.data.election()
    four(df)
