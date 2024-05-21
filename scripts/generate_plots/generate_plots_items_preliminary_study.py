from scripts.utils import get_col_as_ints, create_boxplot


ITEM_COLUMN_INDEX = 2

# ---------- EXTRACT ITEMS: SEMANTIC ----------
# Condition: semantic and all humans
sem_6hum_items = get_col_as_ints('../../csv_data/sem_6hum.csv', ITEM_COLUMN_INDEX)

# Condition: semantic and all bots
sem_6bots_items = get_col_as_ints('../../csv_data/6bots.csv', ITEM_COLUMN_INDEX)


# ---------- EXTRACT ITEMS: NON-SEMANTIC ----------
# Condition: non-semantic and all humans
nonsem_6hum_items = get_col_as_ints('../../csv_data/nonsem_6hum.csv', ITEM_COLUMN_INDEX)

# Condition: non-semantic and all bots
nonsem_6bots_items = get_col_as_ints('../../csv_data/6bots.csv', ITEM_COLUMN_INDEX)


# ---------- COMBINE DATA ----------
items_data_preliminary_study = [sem_6hum_items, sem_6bots_items, nonsem_6hum_items, nonsem_6bots_items]


# ---------- CREATE ITEM FIGURE ----------
preliminary_study_colors = ['#A2CBE8', '#A7D3A6', '#A2CBE8', '#A7D3A6']
preliminary_study_hatch_patterns = ['///', '///', '..', '..']
preliminary_study_xtick_labels = ['All Humans', 'All Bots'] * 2
preliminary_study_figsize = (5, 7)

boxplot_items_preliminary_study = create_boxplot(items_data_preliminary_study, 'Number of Found Items',
                                                 'Boxplot of Preliminary Study', preliminary_study_colors,
                                                 preliminary_study_hatch_patterns, 2.5,
                                                 preliminary_study_xtick_labels, preliminary_study_figsize,
                                                 bbox_to_anchor=(0.55, 1))
boxplot_items_preliminary_study.savefig('../../plots/preliminary-study/boxplot_items_preliminary_study.pdf', format='pdf')
boxplot_items_preliminary_study.show()