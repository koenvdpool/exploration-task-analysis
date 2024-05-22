from typing import List, Dict
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import csv


def list_dicts2csv(raw_data, filename: str):
    """ Convert raw data (list of dicts) to a CSV file. """

    keys = raw_data[0].keys()  # get keys for header

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()  # create header

        for row in raw_data:  # write data
            writer.writerow(row)


def get_col_as_ints(csv_filename, column_index, delimiter=','):
    """TODO."""
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        next(reader)  # Skip the header row
        return [int(row[column_index]) for row in reader if row]


def create_boxplot(data, ylabel, title, colors, hatch_patterns, vert_line_positions, xtick_labels, figsize,
                   bbox_to_anchor=(0.8, 1), variant=None):
    """
    TODO.
    """
    fig, ax = plt.subplots(figsize=figsize)

    hatch_color = '#808080'

    bp = ax.boxplot(data, vert=True, patch_artist=True)

    for patch, color, hatch in zip(bp['boxes'], colors, hatch_patterns):
        patch.set_facecolor(color)
        patch.set_edgecolor(hatch_color)
        patch.set_hatch(hatch)

    # Draw multiple vertical lines
    for pos in vert_line_positions:
        ax.axvline(x=pos, color='lightgrey', linestyle=':', linewidth=1.5)

    ax.set_xticklabels(xtick_labels)

    semantic_patch = Patch(facecolor='#D3D3D3', hatch='///', label='Semantic')
    non_semantic_patch = Patch(facecolor='#D3D3D3', hatch='...', label='Non-Semantic')

    if variant == "semantic":
        legend_handles = [semantic_patch]
    elif variant == "non-semantic":
        legend_handles = [non_semantic_patch]
    else:
        legend_handles = [semantic_patch, non_semantic_patch]

    ax.legend(
        handles=legend_handles,
        title='Game Variant',
        loc='upper left',
        bbox_to_anchor=bbox_to_anchor,
        frameon=False
    )

    ax.set_xlabel('Conditions')
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    plt.tight_layout(pad=2)

    return fig
