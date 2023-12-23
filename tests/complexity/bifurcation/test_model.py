from complexity.bifurcation.logistic.logistic_map_func_factory import LogisticMapFuncFactory
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
