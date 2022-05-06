#from myf.Minority import Minority
import json
import numpy as np
import os


class BWP:
    def __init__(self, districts, proc):
        self.root = {"black": {}, "white": {}, "asian": {}, "hispanic":{}, "rep": {}, "dem":{}}
        for minority in self.root:
            for district in districts:
                self.root[minority][district] = []
        self.proc = proc

    def append(self, minority, percentages):
        for i in range(len(percentages)):
            # bisect.insort(self.root[minority][i], percentages[i])
            self.root[minority][str(i + 1)].append(percentages[i])

    def calculate_and_save(self, i, state):
        for minority in self.root:
            path = f"./plans/{state}/{self.proc}/bwp-final.json"
            with open(path, 'w') as file:
                data = {"mean": np.mean(self.root[minority]), "median": np.median(self.root[minority]),
                        "min": self.root[minority][0], "max": self.root[minority][len(self.root[minority]) - 1],
                        "q1": np.quantile(self.root[minority], .25), "q3": np.quantile(self.root[minority], .75)}
                json.dump(data, file)
            file.close()

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path) as f:
            json.dump(self.root,f)
