from scripts.utils import get_col_as_ints, create_boxplot

ITEM_COLUMN_INDEX = 2
SCORE_COLUMN_INDEX = 3


# ---------- ITEMS FOUND: ALL CONDITIONS ----------
items_sem_6hum = get_col_as_ints('../../csv_data/sem_6hum.csv', ITEM_COLUMN_INDEX)
items_sem_6bots = get_col_as_ints('../../csv_data/6bots.csv', ITEM_COLUMN_INDEX)
items_sem_1bot_5hum = get_col_as_ints('../../csv_data/sem_1bot_5hum.csv', ITEM_COLUMN_INDEX)
items_sem_3bots_3hum = get_col_as_ints('../../csv_data/sem_3bots_3hum.csv', ITEM_COLUMN_INDEX)

items_nonsem_6hum = get_col_as_ints('../../csv_data/nonsem_6hum.csv', ITEM_COLUMN_INDEX)
items_nonsem_6bots = get_col_as_ints('../../csv_data/6bots.csv', ITEM_COLUMN_INDEX)
items_nonsem_1bot_5hum = get_col_as_ints('../../csv_data/nonsem_1bot_5hum.csv', ITEM_COLUMN_INDEX)
items_nonsem_3bots_3hum = get_col_as_ints('../../csv_data/nonsem_3bots_3hum.csv', ITEM_COLUMN_INDEX)


# ---------- SCORE: ALL CONDITIONS ----------
score_sem_6hum = get_col_as_ints('../../csv_data/sem_6hum.csv', SCORE_COLUMN_INDEX)
score_sem_6bots = get_col_as_ints('../../csv_data/6bots.csv', SCORE_COLUMN_INDEX)
score_sem_1bot_5hum = get_col_as_ints('../../csv_data/sem_1bot_5hum.csv', SCORE_COLUMN_INDEX)
score_sem_3bots_3hum = get_col_as_ints('../../csv_data/sem_3bots_3hum.csv', SCORE_COLUMN_INDEX)

score_nonsem_6hum = get_col_as_ints('../../csv_data/nonsem_6hum.csv', SCORE_COLUMN_INDEX)
score_nonsem_6bots = get_col_as_ints('../../csv_data/6bots.csv', SCORE_COLUMN_INDEX)
score_nonsem_1bot_5hum = get_col_as_ints('../../csv_data/nonsem_1bot_5hum.csv', SCORE_COLUMN_INDEX)
score_nonsem_3bots_3hum = get_col_as_ints('../../csv_data/nonsem_3bots_3hum.csv', SCORE_COLUMN_INDEX)


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_all = [items_sem_6hum, items_sem_6bots, items_sem_1bot_5hum, items_sem_3bots_3hum,
                    items_nonsem_6hum, items_nonsem_6bots, items_nonsem_1bot_5hum, items_nonsem_3bots_3hum]

# Combine data for score
score_data_all = [score_sem_6hum, score_sem_6bots, score_sem_1bot_5hum, score_sem_3bots_3hum,
                    score_nonsem_6hum, score_nonsem_6bots, score_nonsem_1bot_5hum, score_nonsem_3bots_3hum]


# ---------- CREATE FIGURES ----------
all_conditions_colors = ['#A2CBE8', '#A7D3A6', '#F9CDAE', '#F9A7A7', '#A2CBE8', '#A7D3A6', '#F9CDAE', '#F9A7A7']
all_conditions_hatch_patterns = ['///', '///', '///', '///', '..', '..', '..', '..']
all_conditions_xtick_labels = ['All Humans', 'All Bots', 'Hybrid: 1 Bot', 'Hybrid: 3 Bots'] * 2
all_confitions_figsize = (10.5, 6)

# Create boxplot for items
boxplot_items = create_boxplot(items_data_all, 'Number of Found Items', 'Boxplot of Items', all_conditions_colors,
                               all_conditions_hatch_patterns, [4.5], all_conditions_xtick_labels,
                               all_confitions_figsize)
boxplot_items.savefig('../../plots/condition-all/boxplot_items_all.pdf', format='pdf')
boxplot_items.show()

# Create boxplot for score
boxplot_score = create_boxplot(score_data_all, 'Score', 'Boxplot of Score', all_conditions_colors,
                               all_conditions_hatch_patterns, [4.5], all_conditions_xtick_labels,
                               all_confitions_figsize)
boxplot_score.savefig('../../plots/condition-all/boxplot_score_all.pdf', format='pdf')
boxplot_score.show()
