import numpy as np

from complexity.bifurcation.i_map_func import IMapFunc
from complexity.bifurcation.i_map_func_factory import IMapFuncFactory


class Model:
    def __init__(
        self,
        map_func_factory: IMapFuncFactory,
        r_increment=0.01,
        init_y_val=0.5,
        iterations=1000,
        orbits_to_skip=500,
    ):
        self._r_orbits = {}
        for r in np.arange(0.1, 4.1, r_increment):
            y_vals = self._iterate(
                map_func=map_func_factory.create(
                    r
                ),  #  map type needs to be passed in constructor,
                y_init=init_y_val,
                orbits_to_skip=orbits_to_skip,
                iterations=iterations,
            )
            self._r_orbits[r] = y_vals

    def _iterate(self, map_func: IMapFunc, orbits_to_skip, y_init, iterations):
        y_vals = []
        y = y_init
        for i in range(iterations):
            y = map_func(y)
            if i > orbits_to_skip:
                y_vals.append(y)
        return y_vals

    def get_r_orbits(self):
        return self._r_orbits
