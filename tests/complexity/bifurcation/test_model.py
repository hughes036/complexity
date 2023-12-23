from complexity.bifurcation.cubic.cubic_map_func_factory import CubicMapFuncFactory
from complexity.bifurcation.logistic.logistic_map_func_factory import (
    LogisticMapFuncFactory,
)
from complexity.bifurcation.model import Model


def test_logistic_map_model():
    model = Model(
        LogisticMapFuncFactory(), r_increment=2, iterations=10, orbits_to_skip=5
    )
    assert model.get_r_orbits() == {
        0.1: [
            2.4309017497646033e-08,
            2.4309016906717706e-09,
            2.4309016847624875e-10,
            2.4309016841715593e-11,
        ],
        2.1: [
            0.5238095250269179,
            0.5238095236877844,
            0.5238095238216979,
            0.5238095238083065,
        ],
    }


def test_cubic_map_model_sm_iterates():
    model = Model(CubicMapFuncFactory(), r_increment=2, iterations=8, orbits_to_skip=5)
    assert model.get_r_orbits() == {
        0.1: [-0.9264346554956896, -0.926335343167266],
        2.1: [389349.61471376405, 4.825899704336779e22], #TODO 5th iteration of this produces 'inf'.  How to deal?
    }

# def test_cubic_map_model_md_iterates():
#     model = Model(CubicMapFuncFactory(), r_increment=2, iterations=20, orbits_to_skip=5)
#     assert model.get_r_orbits() == {
#         0.1: [-0.9264346554956896, -0.926335343167266],
#         2.1: [389349.61471376405, 4.825899704336779e22], #TODO 5th iteration of this produces 'inf'.  How to deal?
#     }
