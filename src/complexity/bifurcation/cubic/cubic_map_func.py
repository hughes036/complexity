from complexity.bifurcation.i_map_func import IMapFunc


class CubicMapFunc(IMapFunc):
    def __init__(self, a):
        self.a = a

    def interate(self, y):
        return (y**3) * (self.a * y) - 1
