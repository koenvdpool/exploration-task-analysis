from typing import List, Dict
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import csv
import pandas as pd
from scipy.stats import mannwhitneyu


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
        if variant is not None:
            patch.set_hatch(hatch)

    if variant is not None:
        for pos in vert_line_positions:
            ax.axvline(x=pos, color='lightgrey', linestyle=':', linewidth=1.5)

    ax.set_xticklabels(xtick_labels)

    non_hybrid_patch = Patch(facecolor='#D3D3D3', hatch='///', label='Non-Hybrid')
    hybrid_patch = Patch(facecolor='#D3D3D3', hatch='...', label='Hybrid')

    if variant == "Non-Hybrid":
        legend_handles = [non_hybrid_patch]
    elif variant == "Hybrid":
        legend_handles = [hybrid_patch]
    elif variant == "all":
        legend_handles = [non_hybrid_patch, hybrid_patch]

    if variant is not None:
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


def calculate_statistics(df, filter_is_robot=None):
    """
    Calculate median, mean, and standard deviation for 'ItemsFound',
    'Score', and 'TotalTrials' columns in the given DataFrame.
    """
    if filter_is_robot is not None:
        filtered_df = df[df['isRobot'] == filter_is_robot]
    else:
        filtered_df = df

    statistics = {
        'Statistic': ['Median', 'Mean', 'Std'],
        'ItemsFound': [
            filtered_df['ItemsFound'].median(),
            filtered_df['ItemsFound'].mean(),
            filtered_df['ItemsFound'].std()
        ],
        'Score': [
            filtered_df['Score'].median(),
            filtered_df['Score'].mean(),
            filtered_df['Score'].std()
        ],
        'TotalTrials': [
            filtered_df['TotalTrials'].median(),
            filtered_df['TotalTrials'].mean(),
            filtered_df['TotalTrials'].std()
        ]
    }

    return pd.DataFrame(statistics), len(filtered_df)


def rank_biserial(x, y, alternative='greater'):
    """
    TODO.
    """
    u, _ = mannwhitneyu(x, y, alternative=alternative)
    n1 = len(x)
    n2 = len(y)
    rank_biserial = (2 * u) / (n1 * n2) - 1
    return rank_biserial