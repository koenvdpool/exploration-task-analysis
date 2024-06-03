# Description: This script generates boxplots for the data collected in the semantic condition with 1 bot and 5 humans.

import pandas as pd
from scripts.utils import create_boxplot

# ---------- SEMANTIC CONDITION: 1 BOT 5 HUMANS ----------
# Get data from CSV files
path_sem_1b5h = '../../csv_data/sem_1bot_5hum.csv'
path_sem_6h = '../../csv_data/sem_6hum.csv'

# Read CSV files
df_sem_1b5h = pd.read_csv(path_sem_1b5h)
df_sem_6h = pd.read_csv(path_sem_6h)

# Filter data on 'isRobot' column
filtered_df_sem_1b5h_hum = df_sem_1b5h[df_sem_1b5h['isRobot'] == 0]
filtered_df_sem_1b5h_bot = df_sem_1b5h[df_sem_1b5h['isRobot'] == 1]


# ---------- ITEMS FOUND: SEM 1B5H ----------
# Filter on 'ItemsFound' column
items_sem_1b5h_hum = filtered_df_sem_1b5h_hum['ItemsFound'].tolist()
items_sem_1b5h_bot = filtered_df_sem_1b5h_bot['ItemsFound'].tolist()
items_sem_1b5h = df_sem_1b5h['ItemsFound'].tolist()
items_sem_6h = df_sem_6h['ItemsFound'].tolist()


# ---------- SCORE: SEM 1B5H ----------
# Filter on 'Score' column
score_sem_1b5h_hum = filtered_df_sem_1b5h_hum['Score'].tolist()
score_sem_1b5h_bot = filtered_df_sem_1b5h_bot['Score'].tolist()
score_sem_1b5h = df_sem_1b5h['Score'].tolist()
sore_sem_6h = df_sem_6h['Score'].tolist()


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_sem_1b5h = [items_sem_6h, items_sem_1b5h, items_sem_1b5h_hum, items_sem_1b5h_bot]

# Combine data for score
score_data_sem_1b5h = [sore_sem_6h, score_sem_1b5h, score_sem_1b5h_hum, score_sem_1b5h_bot]


# ---------- CREATE FIGURES ----------
sem_1b5h_colors = ['#A2CBE8', '#F9CDAE', '#FCE1D1', '#FDF2EC']
sem_1b5h_hatch_patterns = ['///', '///', '///', '///']
sem_1b5h_xtick_labels = ['Human-Only', 'Hybrid: 1 Bot', 'Humans\nHybrid: 1 Bot', 'Bots\nHybrid: 1 Bot']
sem_1b5h_figsize = (8, 6)

# Create boxplot for items found
boxplot_items_sem_1b5h = create_boxplot(items_data_sem_1b5h, 'Number of Found Items',
                                        'Items Found in Semantic Condition: Hybrid with 1 Bot', sem_1b5h_colors,
                                        sem_1b5h_hatch_patterns, [1.5], sem_1b5h_xtick_labels,
                                        sem_1b5h_figsize, bbox_to_anchor=(0.75, 1), variant='semantic')
boxplot_items_sem_1b5h.savefig('../../plots/condition-semantic/boxplot_items_sem_1bot_5hum.pdf', format='pdf')
boxplot_items_sem_1b5h.show()

# Create boxplot for score
boxplot_score_sem_1b5h = create_boxplot(score_data_sem_1b5h, 'Score',
                                        'Score in Semantic Condition: Hybrid with 1 Bot', sem_1b5h_colors,
                                       sem_1b5h_hatch_patterns, [1.5], sem_1b5h_xtick_labels, sem_1b5h_figsize,
                                       bbox_to_anchor=(0.75, 1), variant='semantic')
boxplot_score_sem_1b5h.savefig('../../plots/condition-semantic/boxplot_score_sem_1bot_5hum.pdf', format='pdf')
boxplot_score_sem_1b5h.show()