import random

import numpy
from pandas import read_csv
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from deap import base
from deap import creator
from deap import tools

import matplotlib.pyplot as plt
import seaborn as sns

#
from thirteenth.elitism import eaSimpleWithElitism

HALL_OF_FAME_SIZE = 30


POPULATION_SIZE = 50
P_CROSSOVER = 0.9
P_MUTATION = 0.3
MAX_GENERATIONS = 50
HALL_OF_FAME_SIZE = 5
FEATURE_PENALTY_FACTOR = 0.001
RANDOM_SEED = 42
random.seed(RANDOM_SEED)


class Cancer:
    NUM_FOLDS = 5

    def __init__(self, randomSeed):
        self.randomSeed = randomSeed
        self.data = read_csv('breast-cancer-wisconsin1.data', header=None, usecols=range(1, 11))
        self.X = self.data.iloc[:, 0:9]
        self.y = self.data.iloc[:, 9]
        self.kfold = model_selection.KFold(n_splits=self.NUM_FOLDS, random_state=self.randomSeed, shuffle=True)
        self.classifier = DecisionTreeClassifier(random_state=self.randomSeed)

    def __len__(self):
        return self.X.shape[1]

    def getMeanAccuracy(self, zeroOneList):
        zeroIndices = [i for i, n in enumerate(zeroOneList) if n == 0]
        currentX = self.X.drop(self.X.columns[zeroIndices], axis=1)
        cv_results = model_selection.cross_val_score(self.classifier, currentX, self.y, cv=self.kfold,
                                                     scoring='accuracy')
        return cv_results.mean()


cancer = Cancer(randomSeed=RANDOM_SEED)
toolbox = base.Toolbox()
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox.register("zeroOrOne", random.randint, 0, 1)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, len(cancer))
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


def cancerClassificationAccuracy(individual):
    numFeaturesUsed = sum(individual)
    if numFeaturesUsed == 0:
        return 0.0
    else:
        accuracy = cancer.getMeanAccuracy(individual)
        return accuracy - FEATURE_PENALTY_FACTOR * numFeaturesUsed,


toolbox.register("evaluate", cancerClassificationAccuracy)
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0 / len(cancer))


def main():
    population = toolbox.populationCreator(n=POPULATION_SIZE)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", numpy.max)
    stats.register("avg", numpy.mean)
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)
    population, logbook = eaSimpleWithElitism(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)
    print("- Лучшие решения:")
    for i in range(HALL_OF_FAME_SIZE):
        print(i, ": ", hof.items[i], ", приспособленность = ", hof.items[i].fitness.values[0], ", верность = ",
              cancer.getMeanAccuracy(hof.items[i]), ", признаков = ", sum(hof.items[i]))
    maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")
    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max/Average Fitness')
    plt.title('Max and Average fitness over Generations')
    plt.show()


if __name__ == '__main__':
    main()
