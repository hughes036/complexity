import numpy as np

from complexity.bifurcation.i_map_func import IMapFunc
from complexity.bifurcation.i_map_func_factory import IMapFuncFactory


class Model:
    def __init__(
        self,
        map_func_factory: IMapFuncFactory,
        r_increment=0.01,
        init_x_val=0.5,
        iterations=1000,
        orbits_to_skip=500,
    ):
        self._r_orbits = {}
        for r in np.arange(0.1, 4.1, r_increment):
            x_vals = self._iterate(
                map_func=map_func_factory.create(
                    r
                ),  #  map type needs to be passed in constructor,
                x_init=init_x_val,
                orbits_to_skip=orbits_to_skip,
                iterations=iterations,
            )
            self._r_orbits[r] = x_vals

    def _iterate(self, map_func: IMapFunc, orbits_to_skip, x_init, iterations):
        x_vals = []
        x = x_init
        for i in range(iterations):
            x = map_func(x)
            if i > orbits_to_skip:
                x_vals.append(x)
        return x_vals

    def get_r_orbits(self):
        return self._r_orbits
