import json
import os


class MMD:
    def __init__(self, state, proc):
        self.root = {}
        self.state = state
        self.proc = proc

    def append(self, plan_number, plan):
        self.root[plan_number] = plan

    def save(self, iteration, state):
        path = f"./plans/{state}/mm/{self.proc}/mmDistrict-{iteration}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(self.root[iteration], f)
            f.close()

    def summary(self):
        # Count how many districts are mm on average.
        count = 0.0
        minority_win_percent = 0.0
        district_count = 0
        for mmd in self.root:
            district_count = len(self.root[mmd])

            for district in self.root[mmd]:
                if self.root[mmd][district] > 0.0:
                    count += 1
                    minority_win_percent += self.root[mmd][district]

        # Avg of how many districts are mm
        avg = count / 250
        avg_win_percent = minority_win_percent / count

        st = f"There are on average {avg}  many majority minority districts \
                in {self.state.upper()}. On average, the mionirty population \
                 is great by {avg_win_percent} %"
        tor = {"avg mm count": avg, "avg_win_percent": avg_win_percent}
        path = f'./plans/{self.state}/mm/{self.proc}/final.json'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(tor,f)

