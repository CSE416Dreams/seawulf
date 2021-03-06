#from myf.Minority import Minority
import json
import numpy as np
import os


class BWP:
    def __init__(self, districts, proc, state):
        self.root = {"black": {}, "white": {}, "asian": {}, "hispanic":{}, "rep": {}, "dem":{}}
        for minority in self.root:
            for district in districts:
                self.root[minority][district] = []
        self.proc = proc
        self.state = state

    def append(self, minority, percentages, total_pop, total_votes):
        div = total_pop
        if minority == "rep" or minority == "dem":
            div = total_votes
        for i in range(len(percentages)):
            # bisect.insort(self.root[minority][i], percentages[i])
            self.root[minority][str(i + 1)].append(percentages[i] / div)

    def calculate_and_save(self, i, state):
        for minority in self.root:
            path = f"./plans/{state}/{self.proc}/bwp-final.json"
            with open(path, 'w') as file:
                data = {"mean": np.mean(self.root[minority]), "median": np.median(self.root[minority]),
                        "min": self.root[minority][0], "max": self.root[minority][len(self.root[minority]) - 1],
                        "q1": np.quantile(self.root[minority], .25), "q3": np.quantile(self.root[minority], .75)}
                json.dump(data, file)
            file.close()

    def save(self):
        path = f'./plans/{self.state}/bwp/{self.proc}/final.json'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(self.root,f)
