from chosenMinorities import minority


class BWP:
    def __init__(self, districts):
        self.root = {}
        for data in minority:
            self.root[data.value] = {}
            for i in range(districts):
                self.root[data.value][i] = []

    def append(self, min, district, percentage):
        self.root[min][district].push(percentage)
