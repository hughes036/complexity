from complexity.bifurcation.i_map_func_factory import IMapFuncFactory
from complexity.bifurcation.logistic_map_func import LogisticMapFunc


class LogisticMapFuncFactory(IMapFuncFactory):
    def __init__(self):
        pass

    def create(self, r: float):
        return LogisticMapFunc(r)
