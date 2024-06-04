# Description: This script generates boxplots for the data collected on human participants in all conditions.

import pandas as pd
from scripts.utils import create_boxplot

# ---------- ALL CONDITIONS: ONLY HUMANS ----------
# Get data from CSV files
path_nonsem_6hum = '../../csv_data/nonsem_6hum.csv'
path_nonsem_1bot_5hum = '../../csv_data/nonsem_1bot_5hum.csv'
path_nonsem_3bots_3hum = '../../csv_data/nonsem_3bots_3hum.csv'

# Read CSV files
df_nonsem_6hum = pd.read_csv(path_nonsem_6hum)
df_nonsem_1bot_5hum = pd.read_csv(path_nonsem_1bot_5hum)
df_nonsem_3bots_3hum = pd.read_csv(path_nonsem_3bots_3hum)

# Filter data on 'isRobot' column
filtered_df_nonsem_6hum = df_nonsem_6hum[df_nonsem_6hum['isRobot'] == 0]
filtered_df_nonsem_1bot_5hum = df_nonsem_1bot_5hum[df_nonsem_1bot_5hum['isRobot'] == 0]
filtered_df_nonsem_3bots_3hum = df_nonsem_3bots_3hum[df_nonsem_3bots_3hum['isRobot'] == 0]


# ---------- ITEMS FOUND: ALL CONDITIONS ----------
# Filter on 'ItemsFound' column
items_nonsem_6hum = filtered_df_nonsem_6hum['ItemsFound'].tolist()
items_nonsem_1bot_5hum = filtered_df_nonsem_1bot_5hum['ItemsFound'].tolist()
items_nonsem_3bots_3hum = filtered_df_nonsem_3bots_3hum['ItemsFound'].tolist()


# ---------- SCORE: ALL CONDITIONS ----------
# Filter on 'Score' column
score_nonsem_6hum = filtered_df_nonsem_6hum['Score'].tolist()
score_nonsem_1bot_5hum = filtered_df_nonsem_1bot_5hum['Score'].tolist()
score_nonsem_3bots_3hum = filtered_df_nonsem_3bots_3hum['Score'].tolist()


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_all_hum = [items_nonsem_6hum, items_nonsem_1bot_5hum, items_nonsem_3bots_3hum]

# Combine data for score
score_data_all_hum = [score_nonsem_6hum, score_nonsem_1bot_5hum, score_nonsem_3bots_3hum]


# ---------- CREATE FIGURES ----------
all_conditions_hum_colors = ['#A1BAE0', '#F9D2B9', '#F9A7A7']
all_conditions_hum_hatch_patterns = ['///', '..', '..']
all_conditions_hum_xtick_labels = ['Human-Only', 'Humans\nHybrid: 1 Bot', 'Humans\nHybrid: 3 Bots']
all_conditions_hum_figsize = (6, 6)

# Create boxplot for items found
boxplot_items_all_hum = create_boxplot(items_data_all_hum, 'Number of Found Items', 'Boxplot of Items Found (Humans)',
                                       all_conditions_hum_colors, all_conditions_hum_hatch_patterns, [1.5],
                                       all_conditions_hum_xtick_labels, all_conditions_hum_figsize, bbox_to_anchor=(0.65, 1))
boxplot_items_all_hum.savefig('../../plots/condition-all/boxplot_items_all_hum.pdf', format='pdf')
boxplot_items_all_hum.show()

# Create boxplot for score
boxplot_score_all_hum = create_boxplot(score_data_all_hum, 'Score', 'Boxplot of Score (Humans)',
                                       all_conditions_hum_colors, all_conditions_hum_hatch_patterns, [1.5],
                                       all_conditions_hum_xtick_labels, all_conditions_hum_figsize, bbox_to_anchor=(0.65, 1))
boxplot_score_all_hum.savefig('../../plots/condition-all/boxplot_score_all_hum.pdf', format='pdf')
boxplot_score_all_hum.show()