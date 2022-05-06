import json
import os


seats = {"ms": 4, "ga": 14, "fl": 28}

class RepDemSplits:
    def __init__(self, state, proc):
        self.root = {}
        self.state = state
        self.proc = proc

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

    def save(self, iteration):
        rseat = dseat = 0
        rvote = dvote = 0
        for district, split in self.root[iteration]:
            dvote += split["d"]
            rvote += split["r"]
            if split["win"] == "R":
                rseat += 1
            else:
                dseat += 1
        tseat = rseat + dseat
        tvote = rvote + dvote
        split = {"dseatPer":100*(dseat/tseat), "rseatPer":100*(rseat/tseat),
                 "dvotePer":100*(dvote/tvote), "rvotePer":100*(rvote/tvote)}

        path = f"./plans/{self.state}/rds/{self.proc}/rds-{iteration}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(split, f)
            f.close()
