# Description: This script generates boxplots for the data collected in the non-semantic condition with 1 bot and 5 humans.

import pandas as pd
from scripts.utils import create_boxplot

# ---------- NON-SEMANTIC CONDITION: 1 BOT 5 HUMANS ----------
# Get data from CSV files
path_nonsem_1b5h = '../../csv_data/nonsem_1bot_5hum.csv'
path_nonsem_6h = '../../csv_data/nonsem_6hum.csv'

# Read CSV files
df_nonsem_1b5h = pd.read_csv(path_nonsem_1b5h)
df_nonsem_6h = pd.read_csv(path_nonsem_6h)

# Filter data on 'isRobot' column
filtered_df_nonsem_1b5h_hum = df_nonsem_1b5h[df_nonsem_1b5h['isRobot'] == 0]
filtered_df_nonsem_1b5h_bot = df_nonsem_1b5h[df_nonsem_1b5h['isRobot'] == 1]


# ---------- ITEMS FOUND: NON-SEM 1B5H ----------
# Filter on 'ItemsFound' column
items_nonsem_1b5h_hum = filtered_df_nonsem_1b5h_hum['ItemsFound'].tolist()
items_nonsem_1b5h_bot = filtered_df_nonsem_1b5h_bot['ItemsFound'].tolist()
items_nonsem_1b5h = df_nonsem_1b5h['ItemsFound'].tolist()
items_nonsem_6h = df_nonsem_6h['ItemsFound'].tolist()


# ---------- SCORE: NON-SEM 1B5H ----------
# Filter on 'Score' column
score_nonsem_1b5h_hum = filtered_df_nonsem_1b5h_hum['Score'].tolist()
score_nonsem_1b5h_bot = filtered_df_nonsem_1b5h_bot['Score'].tolist()
score_nonsem_1b5h = df_nonsem_1b5h['Score'].tolist()
sore_nonsem_6h = df_nonsem_6h['Score'].tolist()


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_nonsem_1b5h = [items_nonsem_6h, items_nonsem_1b5h, items_nonsem_1b5h_hum, items_nonsem_1b5h_bot]

# Combine data for score
score_data_nonsem_1b5h = [sore_nonsem_6h, score_nonsem_1b5h, score_nonsem_1b5h_hum, score_nonsem_1b5h_bot]


# ---------- CREATE FIGURES ----------
nonsem_1b5h_colors = ['#A2CBE8', '#F9CDAE', '#FCE1D1', '#FDF2EC']
nonsem_1b5h_hatch_patterns = ['..', '..', '..', '..']
nonsem_1b5h_xtick_labels = ['All Humans', 'Hybrid: 1 Bot', 'Only Humans\nHybrid: 1 Bot', 'Only Bots\nHybrid: 1 Bot']
nonsem_1b5h_figsize = (8, 6)

# Create boxplot for items found
boxplot_items_nonsem_1b5h = create_boxplot(items_data_nonsem_1b5h, 'Number of Found Items',
                                           'Items Found in Non-Semantic Condition: Hybrid with 1 Bot',
                                           nonsem_1b5h_colors, nonsem_1b5h_hatch_patterns, 1.5,
                                           nonsem_1b5h_xtick_labels, nonsem_1b5h_figsize, bbox_to_anchor=(0.75, 1),
                                           variant='non-semantic')
boxplot_items_nonsem_1b5h.savefig('../../plots/condition-non-semantic/boxplot_items_nonsem_1bot_5hum.pdf', format='pdf')
boxplot_items_nonsem_1b5h.show()

# Create boxplot for score
boxplot_score_nonsem_1b5h = create_boxplot(score_data_nonsem_1b5h, 'Score',
                                           'Score in Non-Semantic Condition: Hybrid with 1 Bot', nonsem_1b5h_colors,
                                           nonsem_1b5h_hatch_patterns, 1.5, nonsem_1b5h_xtick_labels,
                                           nonsem_1b5h_figsize, bbox_to_anchor=(0.75, 1), variant='non-semantic')
boxplot_score_nonsem_1b5h.savefig('../../plots/condition-non-semantic/boxplot_score_nonsem_1bot_5hum.pdf', format='pdf')
boxplot_score_nonsem_1b5h.show()