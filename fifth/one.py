import time

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import umap
import pandas as pd
import seaborn as sns
from sklearn import preprocessing


def tsne_visualiser(df, data):
    for perp in [5, 25, 50]:
        time_start = time.time()
        tsne = TSNE(n_components=2, perplexity=perp, random_state=125, init='random', learning_rate=200)
        tsne_features = tsne.fit_transform(data)
        print("Time used: ", time.time() - time_start)
        DATA = data.copy()
        DATA['x'] = tsne_features[:, 0]
        DATA['y'] = tsne_features[:, 1]

        fig = plt.figure()
        sns.scatterplot(x='x', y='y', hue=df['class'], data=DATA, palette='bright')
        plt.title(label="perplexity " + str(perp))
        plt.legend(title='Iris type',
                   labels=['Setosa', 'Versicolour', 'Virginica'])
        plt.show()


def umap_visualiser(df, data):
    for d in (0.1, 0.5):
        for n in (5, 25, 50):
            time_start = time.time()
            um = umap.UMAP(n_neighbors=n, min_dist=d, random_state=125).fit_transform(data)
            print("Time used: ", time.time() - time_start)
            DATA = data.copy()
            DATA['x'] = um[:, 0]
            DATA['y'] = um[:, 1]
            fig = plt.figure()
            sns.scatterplot(x='x', y='y', hue=df['class'], data=DATA, palette='bright')
            plt.title(label=f"neighbors {n}, distance {d}")
            plt.legend(title='Iris type',
                       labels=['Setosa', 'Versicolour', 'Virginica'])
            plt.show()


if __name__ == '__main__':
    dfo = pd.read_csv('iris.csv')
    dataFrame = dfo.drop(['class'], axis=1)
    scaler = preprocessing.MinMaxScaler()
    dataFrame = pd.DataFrame(scaler.fit_transform(dataFrame), columns=dataFrame.columns)
    tsne_visualiser(df=dfo, data=dataFrame)
    umap_visualiser(df=dfo, data=dataFrame)
