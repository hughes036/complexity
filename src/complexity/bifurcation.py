import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

def main():
    r = 3.65
    orbits_to_skip = 4900
    r_increment = .005
    iterations = 5000
    init_val = .3
    r_orbits = {}
    for r in np.arange(0.1, 4.1, r_increment):
        x_vals = iterateR(
        r=r, 
        init_val=init_val, 
        orbits_to_skip=orbits_to_skip, 
        iterations=iterations)
        r_orbits[r] = x_vals

    for r, x_vals in r_orbits.items():
        plt.scatter(
            x = list(map(lambda x: r, x_vals)), 
            y = x_vals, 
            s = list(map(lambda s: .05, x_vals)),
            # c = '#d62728',
            # label='orbits'
        )
        
    # Adding legend, x and y labels, and titles for the lines
    plt.legend()
    plt.xlabel('r')
    plt.ylabel('x')
    # Displaying the plot
    plt.show()

def iterateR(r, orbits_to_skip, init_val, iterations):
    x_vals = []
    current_val = init_val
    for i in range(iterations):
        current_val = logistic(x=current_val, r=r)
        if(i > orbits_to_skip):
            x_vals.append(current_val)
    return x_vals

if __name__ == '__main__':
    main()