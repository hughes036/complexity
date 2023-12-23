from complexity.bifurcation.cubic.cubic_map_func import CubicMapFunc
from complexity.bifurcation.i_map_func_factory import IMapFuncFactory


class CubicMapFuncFactory(IMapFuncFactory):
    def __init__(self):
        pass

    def create(self, a):
        return CubicMapFunc(a)