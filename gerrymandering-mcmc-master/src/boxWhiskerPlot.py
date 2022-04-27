from chosenMinorities import Minority
import bisect
import json
import numpy as np


class BWP:
    def __init__(self, districts):
        self.root = {}
        for data in Minority:
            self.root[data.value] = {}
            for district in districts:
                self.root[data.value][district] = []

    def append(self, minority, percentages):
        for i in range(percentages):
            bisect.insort(self.root[minority][i], percentages[i])

    def calculate_and_save(self, i, state):
        for minority in self.root:
            path = f"./{state}/bwp-{i}.json"
            with open('<incorporate i, where i is how many round have been generated>', 'w') as file:
                data = {"mean": np.mean(self.root[minority]), "median": np.median(self.root[minority]),
                        "min": self.root[minority][0], "max": self.root[minority][len(self.root[minority]) - 1],
                        "q1": np.quantile(self.root[minority], .25), "q3": np.quantile(self.root[minority], .75)}
                json.dump(data, file)
            file.close()
