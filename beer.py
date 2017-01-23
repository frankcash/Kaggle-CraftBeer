import csv
import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt


# def dataset(path, filter_field=None, filter_value=None):
#     """
#     Reads dataset one row at a time
#     """
    # with pd.read_csv(path) as csvfile:
    #     if filter_field:
    #         for row in filter(lambda row: row[filter_field]==filter_value, reader):
    #             yield row

    # with open(path, 'r') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     if filter_field:  # Allows us to filter dataset
    #         for row in filter(lambda row: row[filter_field]==filter_value, reader):
    #             yield row
    #
    #     else:
    #         for row in reader:
    #             yield row

def main(path):
    # foo = list([row["abv"] for row in dataset(path, "style", "American IPA")])
    # print float(foo[-20])

    # data = [(row["brewery_id"], float(row["ounces"])) for row in dataset(path, "style", "American IPA")]
    dataset1 = pd.read_csv(path)
    dataset1['floatabv'] = dataset1['abv'].astype(float)

    data = dataset1[['abv', 'floatabv']]
    width = 0.35
    ind = np.arange(len(data))
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(ind, data['floatabv'])
    ax.set_xticks(np.arange(0, len(data), 4))
    ax.set_xticklabels(list(d[0] for d in data)[0::4], rotation=45)
    ax.set_ylabel("ABV")
    plt.title("ABV for American IPAs")

    plt.show()

if __name__ == "__main__":
    main("./data/beers.csv")
