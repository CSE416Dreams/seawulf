import json


class RepDemSplits:
    def __init__(self):
        self.root = {}

    def append(self, plan, district, rep, dem):
        if not self.root[plan]:
            self.root[plan] = {}
        winner = ""
        if rep > dem:
            winner = "R"
        else:
            winner = "D"

        self.root[plan][district] = {"r": rep, "d": dem, "win": winner}

    def save(self, iterations, state):
        start = iterations - 1000
        for i in range(start, iterations):
            file_path = f"./{state}/repdemSlpit-{i}.json"
            with open(file_path, 'w') as file:
                json.dump(self.root[i], file)
            file.close()
