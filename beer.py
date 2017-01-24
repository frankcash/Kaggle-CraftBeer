import csv
import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

def general_statistics(data):
    print("For all beers collected:")
    print("The lowest ABV:{0}. The average ABV: {1}. The highest ABV: {2}.".format(data['abv'].min(), data['abv'].mean(), data['abv'].max()))
    print("The lowest IBU:{0}. The average IBU: {1}. The highest IBU: {2}.".format(data['ibu'].min(), data['ibu'].mean(), data['ibu'].max()))


def main(path):
    dataset1 = pd.read_csv(path)
    dataset1['floatabv'] = dataset1['abv'].astype(float)
    # print(dataset1['floatabv'].mean())
    general_statistics(dataset1)

    data = dataset1[['abv', 'floatabv']]
    width = 0.35
    ind = np.arange(len(data))
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(ind, data['floatabv'])
    ax.set_xticks(np.arange(0, len(data), 4))
    ax.set_xticklabels(list(d[0] for d in data)[0::4], rotation=45)
    ax.set_ylabel("ABV")
    plt.title("ABV for Craft Beer")

    plt.show()

if __name__ == "__main__":
    main("./data/beers.csv")
