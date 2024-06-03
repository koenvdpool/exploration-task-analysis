from scripts.utils import get_col_as_ints, create_boxplot

ITEM_COLUMN_INDEX = 2
SCORE_COLUMN_INDEX = 3


# ---------- ITEMS FOUND: PRELIMINARY STUDY ----------
items_sem_6hum = get_col_as_ints('../../csv_data/sem_6hum.csv', ITEM_COLUMN_INDEX)
items_sem_6bots = get_col_as_ints('../../csv_data/6bots.csv', ITEM_COLUMN_INDEX)
items_nonsem_6hum = get_col_as_ints('../../csv_data/nonsem_6hum.csv', ITEM_COLUMN_INDEX)
items_nonsem_6bots = get_col_as_ints('../../csv_data/6bots.csv', ITEM_COLUMN_INDEX)


# ---------- SCORE: PRELIMINARY STUDY ----------
score_sem_6hum = get_col_as_ints('../../csv_data/sem_6hum.csv', SCORE_COLUMN_INDEX)
score_sem_6bots = get_col_as_ints('../../csv_data/6bots.csv', SCORE_COLUMN_INDEX)
score_nonsem_6hum = get_col_as_ints('../../csv_data/nonsem_6hum.csv', SCORE_COLUMN_INDEX)
score_nonsem_6bots_ = get_col_as_ints('../../csv_data/6bots.csv', SCORE_COLUMN_INDEX)


# ---------- COMBINE DATA ----------
# Combine data for items found
items_data_preliminary_study = [items_sem_6hum, items_sem_6bots, items_nonsem_6hum, items_nonsem_6bots]

# Combine data for score
score_data_preliminary_study = [score_sem_6hum, score_sem_6bots, score_nonsem_6hum, score_nonsem_6bots_]


# ---------- CREATE ITEM FIGURE ----------
preliminary_study_colors = ['#A2CBE8', '#A7D3A6', '#A2CBE8', '#A7D3A6']
preliminary_study_hatch_patterns = ['///', '///', '..', '..']
preliminary_study_xtick_labels = ['Human-Only', 'Bot-Only'] * 2
preliminary_study_figsize = (5, 5)

# Create boxplot for items
boxplot_items_preliminary_study = create_boxplot(items_data_preliminary_study, 'Number of Found Items',
                                                 'Boxplot of Preliminary Study', preliminary_study_colors,
                                                 preliminary_study_hatch_patterns, [2.5],
                                                 preliminary_study_xtick_labels, preliminary_study_figsize,
                                                 bbox_to_anchor=(0.55, 1))
boxplot_items_preliminary_study.savefig('../../plots/preliminary-study/boxplot_items_preliminary_study.pdf', format='pdf')
boxplot_items_preliminary_study.show()

# Create boxplot for score
boxplot_score_preliminary_study = create_boxplot(score_data_preliminary_study, 'Score',
                                                 'Boxplot of Preliminary Study', preliminary_study_colors,
                                                 preliminary_study_hatch_patterns, [2.5],
                                                 preliminary_study_xtick_labels, preliminary_study_figsize,
                                                 bbox_to_anchor=(0.55, 1))
boxplot_score_preliminary_study.savefig('../../plots/preliminary-study/boxplot_score_preliminary_study.pdf', format='pdf')
boxplot_score_preliminary_study.show()