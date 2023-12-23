from abc import ABC, abstractmethod

from complexity.bifurcation.i_map_func import IMapFunc


class IMapFuncFactory(ABC):
    @abstractmethod
    def create(self, r: float) -> IMapFunc:
        pass