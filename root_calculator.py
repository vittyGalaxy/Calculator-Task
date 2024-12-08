class RootCalculator:
    def __init__(self):
        self.radicand = []
        self.index = []
        self.enabled = False

    def update_radicand(self, radicand):
        self.radicand.append(radicand)

    def update_index(self, index):
        self.index.append(index)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
        self.index.clear()
        self.radicand.clear()

    def is_enabled(self):
        return self.enabled

    def get_string(self):
        return str(f"".join(self.radicand)) + "**" + "1/" + str(f"".join(self.index))