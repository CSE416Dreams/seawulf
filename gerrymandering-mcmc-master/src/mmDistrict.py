import json


class MMD:
    def __init__(self):
        self.root = {}

    def append(self, plan_number, plan):
        self.root[plan_number] = plan

    def save(self, iterations, state):
        start = iterations - 1000
        for i in range(start, iterations):
            file_path = f"./{state}/mmDistrict-{i}.json"
            with open(file_path, 'w') as file:
                json.dump(self.root[i], file)
            file.close()

    def summary(self):
        # Count how many districts are mm on average.
        count = 0
        for mmd in self.root:
            for district in mmd:
                if mmd[district]:
                    count += 1
        # Avg of how many districts are mm
        avg = count / 10000
