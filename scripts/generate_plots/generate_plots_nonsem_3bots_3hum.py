# Description: This script generates boxplots for the data collected in the non-semantic condition with 3 bots and 3 humans.

import pandas as pd
from scripts.utils import create_boxplot

# Get data from CSV files
path_nonsem_3b3h = '../../csv_data/nonsem_3bots_3hum.csv'
path_nonsem_6h = '../../csv_data/nonsem_6hum.csv'

# Read CSV files
df_nonsem_3b3h = pd.read_csv(path_nonsem_3b3h)
df_nonsem_6h = pd.read_csv(path_nonsem_6h)

# Filter data on 'isRobot' column
filtered_df_nonsem_3b3h_hum = df_nonsem_3b3h[df_nonsem_3b3h['isRobot'] == 0]
filtered_df_nonsem_3b3h_bot = df_nonsem_3b3h[df_nonsem_3b3h['isRobot'] == 1]


# ---------- ITEMS FOUND: NON-SEM 3B3H ----------
# Filter on 'ItemsFound' column
items_nonsem_3b3h_hum = filtered_df_nonsem_3b3h_hum['ItemsFound'].tolist()
items_nonsem_3b3h_bot = filtered_df_nonsem_3b3h_bot['ItemsFound'].tolist()
items_nonsem_3b3h = df_nonsem_3b3h['ItemsFound'].tolist()
items_nonsem_6h = df_nonsem_6h['ItemsFound'].tolist()

# Combine data for items found
items_data_nonsem_3b3h = [items_nonsem_6h, items_nonsem_3b3h, items_nonsem_3b3h_hum, items_nonsem_3b3h_bot]

# Create boxplot for items found
nonsem_3b3h_colors = ['#A2CBE8', '#F9A7A7', '#FBCFCF', '#FDE7E7']
nonsem_3b3h_hatch_patterns = ['..', '..', '..', '..']
nonsem_3b3h_xtick_labels = ['All Humans', 'Hybrid: 3 Bots', 'Only Humans\nHybrid: 3 Bots', 'Only Bots\nHybrid: 3 Bots']
nonsem_3b3h_figsize = (8, 6)

boxplot_items_nonsem_3b3h = create_boxplot(items_data_nonsem_3b3h, 'Number of Found Items',
                                           'Items Found in Non-Semantic Condition: Hybrid with 3 Bots',
                                           nonsem_3b3h_colors, nonsem_3b3h_hatch_patterns, 1.5,
                                           nonsem_3b3h_xtick_labels, nonsem_3b3h_figsize, bbox_to_anchor=(0.75, 1),
                                           variant='non-semantic')
boxplot_items_nonsem_3b3h.savefig('../../plots/condition-non-semantic/boxplot_items_nonsem_3bots_3hum.pdf', format='pdf')
boxplot_items_nonsem_3b3h.show()


# ---------- SCORE: NON-SEM 3B3H ----------
# Filter on 'Score' column
score_nonsem_3b3h_hum = filtered_df_nonsem_3b3h_hum['Score'].tolist()
score_nonsem_3b3h_bot = filtered_df_nonsem_3b3h_bot['Score'].tolist()
score_nonsem_3b3h = df_nonsem_3b3h['Score'].tolist()
sore_nonsem_6h = df_nonsem_6h['Score'].tolist()

# Combine data for score
score_data_nonsem_3b3h = [sore_nonsem_6h, score_nonsem_3b3h, score_nonsem_3b3h_hum, score_nonsem_3b3h_bot]

# Create boxplot for score
boxplot_score_nonsem_3b3h = create_boxplot(score_data_nonsem_3b3h, 'Score',
                                           'Score in Non-Semantic Condition: Hybrid with 3 Bots', nonsem_3b3h_colors,
                                           nonsem_3b3h_hatch_patterns, 1.5, nonsem_3b3h_xtick_labels, nonsem_3b3h_figsize,
                                           bbox_to_anchor=(0.75, 1), variant='non-semantic')
boxplot_score_nonsem_3b3h.savefig('../../plots/condition-non-semantic/boxplot_score_nonsem_3bots_3hum.pdf', format='pdf')
boxplot_score_nonsem_3b3h.show()