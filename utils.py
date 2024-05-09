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


def create_boxplot(data, ylabel, title):
    """TODO."""
    fig, ax = plt.subplots(figsize=(10.5, 6))

    colors = ['#A2CBE8', '#A7D3A6', '#F9CDAE', '#F9A7A7', '#A2CBE8', '#A7D3A6', '#F9CDAE', '#F9A7A7']
    hatch_patterns = ['///', '///', '///', '///', '..', '..', '..', '..']
    hatch_color = '#808080'

    bp = ax.boxplot(data, vert=True, patch_artist=True)

    for patch, color, hatch in zip(bp['boxes'], colors, hatch_patterns):
        patch.set_facecolor(color)
        patch.set_edgecolor(hatch_color)
        patch.set_hatch(hatch)

    ax.axvline(x=4.5, color='lightgrey', linestyle=':', linewidth=1.5)

    ax.set_xticklabels(['All Humans', 'All Bots', 'Hybrid: 1 Bot', 'Hybrid: 3 Bots'] * 2)

    semantic_patch = Patch(facecolor='#D3D3D3', hatch='///', label='Semantic')
    non_semantic_patch = Patch(facecolor='#D3D3D3', hatch='...', label='Non-Semantic')

    ax.legend(
        handles=[semantic_patch, non_semantic_patch],
        title='Game Variant',
        loc='upper left',
        bbox_to_anchor=(0.8, 1),
        frameon=False
    )

    ax.set_xlabel('Conditions')
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    plt.tight_layout(pad=2)

    return fig
