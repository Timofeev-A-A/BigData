from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import umap
import pandas as pd
import seaborn as sns
from sklearn import preprocessing


def tsne_visualiser(df, data):
    for perp in [5, 25, 50]:
        tsne = TSNE(n_components=2, perplexity=perp, random_state=125)
        tsne_features = tsne.fit_transform(data)
        DATA = data.copy()
        DATA['x'] = tsne_features[:, 0]
        DATA['y'] = tsne_features[:, 1]

        fig = plt.figure()
        sns.scatterplot(x='x', y='y', hue=df['class_type'], data=DATA, palette='pastel')
        plt.title(label="perplexity " + str(perp))
        plt.legend(title='Animal type',
                   labels=['Reptile', 'Fish', 'Amphibian', 'Insect', 'Invertebrates', 'Mammal', 'Birb'])
        plt.show()


def umap_visualiser(df, data):
    for n in (5, 25, 50):
        for d in (0.1, 0.5):
            um = umap.UMAP(n_neighbors=n, min_dist=d, random_state=125).fit_transform(data)
            DATA = data.copy()
            DATA['x'] = um[:, 0]
            DATA['y'] = um[:, 1]
            fig = plt.figure()
            sns.scatterplot(x='x', y='y', hue=df['class_type'], data=DATA, palette='pastel')
            plt.title(label=str(n) + str(d))
            plt.legend(title='Animal type',
                       labels=['Reptile', 'Fish', 'Amphibian', 'Insect', 'Invertebrates', 'Mammal', 'Birb'])
            plt.show()


if __name__ == '__main__':
    dfo = pd.read_csv('zoo.csv')
    dataFrame = dfo.drop(['class_type', 'animal_name'], axis=1)
    scaler = preprocessing.MinMaxScaler()
    dataFrame = pd.DataFrame(scaler.fit_transform(dataFrame), columns=dataFrame.columns)
    tsne_visualiser(df=dfo, data=dataFrame)
    umap_visualiser(df=dfo, data=dataFrame)
