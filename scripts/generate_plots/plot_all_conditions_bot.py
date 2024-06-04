# Description: This script generates boxplots for the data collected on bot participants in all conditions.

import pandas as pd
from scripts.utils import create_boxplot

# ---------- ALL CONDITIONS: ONLY BOTS ----------
# Get data from CSV files
path_nonsem_6bots = '../../csv_data/6bots.csv'
path_nonsem_1bot_5hum = '../../csv_data/nonsem_1bot_5hum.csv'
path_nonsem_3bots_3hum = '../../csv_data/nonsem_3bots_3hum.csv'

# Read CSV files
df_nonsem_6bots = pd.read_csv(path_nonsem_6bots)
df_nonsem_1bot_5hum = pd.read_csv(path_nonsem_1bot_5hum)
df_nonsem_3bots_3hum = pd.read_csv(path_nonsem_3bots_3hum)

# Filter data on 'isRobot' column
filtered_df_nonsem_6bots = df_nonsem_6bots[df_nonsem_6bots['isRobot'] == 1]
filtered_df_nonsem_1bot_5hum = df_nonsem_1bot_5hum[df_nonsem_1bot_5hum['isRobot'] == 1]
filtered_df_nonsem_3bots_3hum = df_nonsem_3bots_3hum[df_nonsem_3bots_3hum['isRobot'] == 1]


# ---------- ITEMS FOUND: ALL CONDITIONS ----------
# Filter on 'ItemsFound' column
items_nonsem_6bots = filtered_df_nonsem_6bots['ItemsFound'].tolist()
items_nonsem_1bot_5hum = filtered_df_nonsem_1bot_5hum['ItemsFound'].tolist()
items_nonsem_3bots_3hum = filtered_df_nonsem_3bots_3hum['ItemsFound'].tolist()


# ---------- SCORE: ALL CONDITIONS ----------
# Filter on 'Score' column
score_nonsem_6bots = filtered_df_nonsem_6bots['Score'].tolist()
score_nonsem_1bot_5hum = filtered_df_nonsem_1bot_5hum['Score'].tolist()
score_nonsem_3bots_3hum = filtered_df_nonsem_3bots_3hum['Score'].tolist()


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_all_bots = [items_nonsem_6bots, items_nonsem_1bot_5hum, items_nonsem_3bots_3hum]

# Combine data for score
score_data_all_bots = [score_nonsem_6bots, score_nonsem_1bot_5hum, score_nonsem_3bots_3hum]


# ---------- CREATE FIGURES ----------
all_conditions_bot_colors = ['#A6D09D', '#FCE5D2', '#FBCFCF']
all_conditions_bot_hatch_patterns = ['///', '..', '..']
all_conditions_bot_xtick_labels = ['Bot-Only', 'Bots\nHybrid: 1 Bot', 'Bots\nHybrid: 3 Bots']
all_conditions_bot_figsize = (6, 6)

# Create boxplot for items found
boxplot_items_all_bot = create_boxplot(items_data_all_bots, 'Number of Found Items', 'Boxplot of Items Found (Bots)',
                                       all_conditions_bot_colors, all_conditions_bot_hatch_patterns, [1.5],
                                       all_conditions_bot_xtick_labels, all_conditions_bot_figsize, bbox_to_anchor=(0.65, 1))
boxplot_items_all_bot.savefig('../../plots/condition-all/boxplot_items_all_bots.pdf', format='pdf')
boxplot_items_all_bot.show()

# Create boxplot for score
boxplot_score_all_bot = create_boxplot(score_data_all_bots, 'Score', 'Boxplot of Score (Bots)',
                                       all_conditions_bot_colors, all_conditions_bot_hatch_patterns, [1.5],
                                       all_conditions_bot_xtick_labels, all_conditions_bot_figsize, bbox_to_anchor=(0.65, 1))
boxplot_score_all_bot.savefig('../../plots/condition-all/boxplot_score_all_bots.pdf', format='pdf')
boxplot_score_all_bot.show()