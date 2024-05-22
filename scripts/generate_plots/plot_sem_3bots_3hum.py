# Description: This script generates boxplots for the data collected in the semantic condition with 3 bots and 3 humans.

import pandas as pd
from scripts.utils import create_boxplot

# ---------- SEMANTIC CONDITION: 3 BOTS 3 HUMANS ----------
# Get data from CSV files
path_sem_3b3h = '../../csv_data/sem_3bots_3hum.csv'
path_sem_6h = '../../csv_data/sem_6hum.csv'

# Read CSV files
df_sem_3b3h = pd.read_csv(path_sem_3b3h)
df_sem_6h = pd.read_csv(path_sem_6h)

# Filter data on 'isRobot' column
filtered_df_sem_3b3h_hum = df_sem_3b3h[df_sem_3b3h['isRobot'] == 0]
filtered_df_sem_3b3h_bot = df_sem_3b3h[df_sem_3b3h['isRobot'] == 1]


# ---------- ITEMS FOUND: SEM 3B3H ----------
# Filter on 'ItemsFound' column
items_sem_3b3h_hum = filtered_df_sem_3b3h_hum['ItemsFound'].tolist()
items_sem_3b3h_bot = filtered_df_sem_3b3h_bot['ItemsFound'].tolist()
items_sem_3b3h = df_sem_3b3h['ItemsFound'].tolist()
items_sem_6h = df_sem_6h['ItemsFound'].tolist()


# ---------- SCORE: SEM 3B3H ----------
# Filter on 'Score' column
score_sem_3b3h_hum = filtered_df_sem_3b3h_hum['Score'].tolist()
score_sem_3b3h_bot = filtered_df_sem_3b3h_bot['Score'].tolist()
score_sem_3b3h = df_sem_3b3h['Score'].tolist()
sore_sem_6h = df_sem_6h['Score'].tolist()


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_sem_3b3h = [items_sem_6h, items_sem_3b3h, items_sem_3b3h_hum, items_sem_3b3h_bot]

# Combine data for score
score_data_sem_3b3h = [sore_sem_6h, score_sem_3b3h, score_sem_3b3h_hum, score_sem_3b3h_bot]


# ---------- CREATE FIGURES ----------
sem_3b3h_colors = ['#A2CBE8', '#F9A7A7', '#FBCFCF', '#FDE7E7']
sem_3b3h_hatch_patterns = ['///', '///', '///', '///']
sem_3b3h_xtick_labels = ['All Humans', 'Hybrid: 3 Bots', 'Only Humans\nHybrid: 3 Bots', 'Only Bots\nHybrid: 3 Bots']
sem_3b3h_figsize = (8, 6)

# Create boxplot for items found
boxplot_items_sem_3b3h = create_boxplot(items_data_sem_3b3h, 'Number of Found Items',
                                                 'Items Found in Semantic Condition: Hybrid with 3 Bots', sem_3b3h_colors, sem_3b3h_hatch_patterns,
                                                 [1.5], sem_3b3h_xtick_labels, sem_3b3h_figsize,
                                                 bbox_to_anchor=(0.75, 1), variant='semantic')
boxplot_items_sem_3b3h.savefig('../../plots/condition-semantic/boxplot_items_sem_3bots_3hum.pdf', format='pdf')
boxplot_items_sem_3b3h.show()


# Create boxplot for score
boxplot_score_sem_3b3h = create_boxplot(score_data_sem_3b3h, 'Score', 'Score in Semantic Condition: Hybrid with 3 Bots', sem_3b3h_colors,
                                       sem_3b3h_hatch_patterns, [1.5], sem_3b3h_xtick_labels, sem_3b3h_figsize,
                                       bbox_to_anchor=(0.75, 1), variant='semantic')
boxplot_score_sem_3b3h.savefig('../../plots/condition-semantic/boxplot_score_sem_3bots_3hum.pdf', format='pdf')
boxplot_score_sem_3b3h.show()
