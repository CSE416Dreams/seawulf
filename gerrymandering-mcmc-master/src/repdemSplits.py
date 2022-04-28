import json


seats = {"ms": 4, "ga": 14, "fl": 28}

class RepDemSplits:
    def __init__(self, state):
        self.root = {}
        self.state = state

    def append(self, plan, district, rep, dem):
        if not self.root[plan]:
            self.root[plan] = {}
        winner = ""
        if rep > dem:
            winner = "R"
        else:
            winner = "D"

        self.root[plan][district] = {"r": rep, "d": dem, "win": winner}

    def seat_splits(self):
        for index, plan in self.root.items():
            rcount = dcount = 0
            for district, split in plan.items():
                if split["win"] == "r":
                    rcount += 1
                else:
                    dcount += 1
            self.root[index]["r_seats"] = rcount
            self.root[index]["d_seats"] = dcount

    def seat_vote_curve(self):
        return

    def summary(self):
        # Avg of how many seats a party wins in a plan
        return

    def save(self, iterations):
        start = iterations - 1000
        for i in range(start, iterations):
            file_path = f"./{self.state}/repdemSlpit-{i}.json"
            with open(file_path, 'w') as file:
                json.dump(self.root[i], file)
            file.close()
