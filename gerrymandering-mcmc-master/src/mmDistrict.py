class MMD:
    def __init__(self):
        self.root = {}

    def append(self, plan_number, districts):
        self.root[plan_number] = districts
