from complexity.bifurcation.i_map_func import IMapFunc


class LogisticMapFunc(IMapFunc):
    def __init__(self, r):
        self.r = r

    def __call__(self, x):
        return self.r * x * (1 - x)
