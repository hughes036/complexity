import matplotlib.pyplot as plt
from complexity.bifurcation.cubic.cubic_map_func_factory import CubicMapFuncFactory
from complexity.bifurcation.logistic.logistic_map_func_factory import LogisticMapFuncFactory

from complexity.bifurcation.model import Model


def plot():
    # r_orbits_model: Model = Model(LogisticMapFuncFactory())
    r_orbits_model: Model = Model(CubicMapFuncFactory())

    for r, x_vals in r_orbits_model.get_r_orbits().items():
        plt.scatter(
            x=list(
                map(lambda x: r, x_vals)
            ),  # A list of the r value (repeated) the same length as x_vals
            y=x_vals,
            s=list(
                map(lambda s: 0.05, x_vals)
            ),  # A list of the size of the dots (repeated) the same length as x_vals
            # c = '#d62728',
            # label='orbits'
        )

    # Adding legend, x and y labels, and titles for the lines
    plt.legend()
    plt.xlabel("r")
    plt.ylabel("x")
    # Displaying the plot
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()
