from complexity.bifurcation.i_map_func import IMapFunc


class LogisticMapFunc(IMapFunc):
    def __init__(self, r):
        self.r = r

    def interate(self, y):
        return self.r * y * (1 - y)
