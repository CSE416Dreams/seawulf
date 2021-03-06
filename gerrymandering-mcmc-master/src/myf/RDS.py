import json
import os


class RDS:
    def __init__(self, state, proc):
        self.root = {}
        self.state = state
        self.proc = proc

    def append(self, plan, district, rep, dem):
        if not plan in self.root:
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
        for district in self.root[iteration]:
            dvote += self.root[iteration][district]["d"]
            rvote += self.root[iteration][district]["r"]
            if self.root[iteration][district]["win"] == "R":
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
