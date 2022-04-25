from chosenMinorities import Minority
import bisect


class BWP:
    def __init__(self, districts):
        self.root = {}
        for data in Minority:
            self.root[data.value] = {}
            for i in range(districts):
                self.root[data.value][i] = []

    def append(self, minority, percentages):
        for i in range(percentages):
            bisect.insort(self.root[minority][i], percentages[i])
