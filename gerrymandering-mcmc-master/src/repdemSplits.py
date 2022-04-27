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

        self.plan[plan][district] = {"r": rep, "d": dem, "win": win}

    def save(self, iterations, state):
        start = iterations - 1000
        file_path = f"./{state}/repdemSlpit-{i}.json"
        for i in range(start, iterations):
            with open(file_path, 'w') as file:
                json.dump(self.root[i], file)
            file.close()
