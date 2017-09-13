import json
import pickle
import sys
import numpy as np
import matplotlib.pyplot as plt

#from bld.project_paths import project_paths_join as ppj

PLOT_ARGS = {"markersize": 4, "alpha": 0.6}


def plot_locations(locations_by_round, model_name):
    "Plot the distribution of agents after cycle_num rounds of the loop."
    n_cycles = len(locations_by_round)
    nrows = int(np.ceil(n_cycles / 2 - 0.01))
    figsize = (2 * 3, nrows * 2)
    fig, axes = plt.subplots(nrows=nrows, ncols=2, figsize=figsize)
    fig.subplots_adjust(
        left=0.05,
        right=0.95,
        bottom=0.05,
        top=0.95,
        wspace=0.25,
        hspace=0.25
    )
    for item, ax in np.ndenumerate(axes):
        n_cycle = item[0] * 2 + item[1]
        if n_cycle == n_cycles:
            # Remove last element if number of cycles is uneven
            fig.delaxes(ax)
            break
        locs = locations_by_round[n_cycle]
        ax.set_title("Cycle {}".format(n_cycle))
        ax.tick_params(labelbottom="off", labelleft="off")
        ax.set_axis_bgcolor("azure")
        ax.plot(locs[0][:, 0], locs[0][:, 1], "o", markerfacecolor="orange", **PLOT_ARGS)
        ax.plot(locs[1][:, 0], locs[1][:, 1], "o", markerfacecolor="green", **PLOT_ARGS)

    fig.savefig(sys.argv[3])


if __name__ == "__main__":
    model_name = sys.argv[1]
    model = json.load(open(model_name, encoding="utf-8"))

    # Load locations after each round
    with open(sys.argv[2], "rb") as in_file:
        locations_by_round = pickle.load(in_file)

    plot_locations(locations_by_round, model_name)
