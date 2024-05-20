from utils import get_col_as_ints, create_boxplot


SCORE_COLUMN_INDEX = 3

# ---------- EXTRACT SCORES: SEMANTIC ----------
# Condition: semantic and all humans
sem_6hum_score = get_col_as_ints('csv_data/sem_6hum.csv', SCORE_COLUMN_INDEX)

# Condition: semantic and all bots
sem_6bots_score = get_col_as_ints('csv_data/6bots.csv', SCORE_COLUMN_INDEX)


# ---------- EXTRACT SCORES: NON-SEMANTIC ----------
# Condition: non-semantic and all humans (bots = 0)
nonsem_6hum_score = get_col_as_ints('csv_data/nonsem_6hum.csv', SCORE_COLUMN_INDEX)

# Condition: non-semantic and all bots (bots = 6)
nonsem_6bots_score = get_col_as_ints('csv_data/6bots.csv', SCORE_COLUMN_INDEX)


# ---------- COMBINE DATA ----------
score_data_preliminary_study = [sem_6hum_score, sem_6bots_score, nonsem_6hum_score, nonsem_6bots_score]


# ---------- CREATE SCORE FIGURE ----------
preliminary_study_colors = ['#A2CBE8', '#A7D3A6', '#A2CBE8', '#A7D3A6']
preliminary_study_hatch_patterns = ['///', '///', '..', '..']
preliminary_study_xtick_labels = ['All Humans', 'All Bots'] * 2
preliminary_study_figsize = (5, 7)

boxplot_score_preliminary_study = create_boxplot(score_data_preliminary_study, 'Score',
                                                 'Boxplot of Preliminary Study', preliminary_study_colors,
                                                 preliminary_study_hatch_patterns, 2.5,
                                                 preliminary_study_xtick_labels, preliminary_study_figsize,
                                                 bbox_to_anchor=(0.55, 1))
boxplot_score_preliminary_study.savefig('plots/boxplot_score_preliminary_study.pdf', format='pdf')
boxplot_score_preliminary_study.show()