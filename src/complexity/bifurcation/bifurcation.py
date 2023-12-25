from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
from complexity.bifurcation.cubic.cubic_map_func_factory import CubicMapFuncFactory
from complexity.bifurcation.logistic.logistic_map_func_factory import (
    LogisticMapFuncFactory,
)

from complexity.bifurcation.model import Model


def plot():
    # model: Model = Model(LogisticMapFuncFactory())
    model: Model = Model(CubicMapFuncFactory(), init_y_val=.9, iterations=1000, orbits_to_skip=800)
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Bifurcation Diagram')
    ax1.set_title('R Plot')
    ax2.set_title('Time Plot')

    for r, x_vals in model.get_r_orbits().items():
        ax1.scatter(
            x=list(
                map(lambda x: r, x_vals)
            ),  # A list of the r value (repeated) the same length as x_vals
            y=x_vals,
            s=list(
                map(lambda s: 0.05, x_vals)
            ),  # A list of the size of the dots (repeated) the same length as x_vals
            c = '#347deb',
        )


    def on_click(event):
        if event.inaxes == ax1:
            ax2.clear()
            ax2.set_title('Time Plot')
            closest_r = model.closest_r_value(event.xdata) 
            y_vals = model.get_r_orbits()[closest_r][-50:]
            x_vals = list(range(0, len(y_vals)))
            ax2.plot(x_vals, y_vals, label=f'r={event.xdata}')
            plt.draw()

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()
