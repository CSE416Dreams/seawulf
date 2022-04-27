import json


class MMD:
    def __init__(self, state):
        self.root = {}
        self.state = state

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
        count = 0.0
        minority_win_percent = 0.0
        for mmd in self.root:
            for district in mmd:
                if mmd[district] != 0:
                    count += 1
                    minority_win_percent += mmd[district]

        # Avg of how many districts are mm
        avg = count / 10000
        avg_win_percent = minority_win_percent / count

        st = f"There are on average {avg}  many majority minority districts \
                in {self.state.upper()}. On average, the mionirty population \
                 is great by {avg_win_percent} %"
