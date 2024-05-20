from utils import get_col_as_ints, create_boxplot


SCORE_COLUMN_INDEX = 3

# Condition: TEST
test_score = get_col_as_ints('csv_data/test.csv', SCORE_COLUMN_INDEX)


# ---------- EXTRACT SCORES: SEMANTIC ----------
# Condition: semantic and all humans
sem_6hum_score = get_col_as_ints('csv_data/sem_6hum.csv', SCORE_COLUMN_INDEX)

# Condition: semantic and all bots
sem_6bots_score = get_col_as_ints('csv_data/6bots.csv', SCORE_COLUMN_INDEX)

# Condition: semantic and hybrid (bots = 1, humans = 5)
sem_1bot_5hum_score = test_score

# Condition: semantic and hybrid (bots = 3, humans = 3)
sem_3bots_3hum_score = get_col_as_ints('csv_data/sem_3bots_3hum.csv', SCORE_COLUMN_INDEX)


# ---------- EXTRACT SCORES: NON-SEMANTIC ----------
# Condition: non-semantic and all humans (bots = 0)
nonsem_6hum_score = get_col_as_ints('csv_data/nonsem_6hum.csv', SCORE_COLUMN_INDEX)

# Condition: non-semantic and all bots (bots = 6)
nonsem_6bots_score = get_col_as_ints('csv_data/6bots.csv', SCORE_COLUMN_INDEX)

# Condition: non-semantic and hybrid (bots = 1, humans = 5)
nonsem_1bot_5hum_score = test_score

# Condition: non-semantic and hybrid (bots = 3, humans = 3)
nonsem_3bots_3hum_score = test_score


# ---------- COMBINE DATA ----------
score_data = [sem_6hum_score, sem_6bots_score, sem_1bot_5hum_score, sem_3bots_3hum_score,
              nonsem_6hum_score, nonsem_6bots_score, nonsem_1bot_5hum_score, nonsem_3bots_3hum_score]


# ---------- CREATE SCORE FIGURE ----------
all_conditions_colors = ['#A2CBE8', '#A7D3A6', '#F9CDAE', '#F9A7A7', '#A2CBE8', '#A7D3A6', '#F9CDAE', '#F9A7A7']
all_conditions_hatch_patterns = ['///', '///', '///', '///', '..', '..', '..', '..']
all_conditions_xtick_labels = ['All Humans', 'All Bots', 'Hybrid: 1 Bot', 'Hybrid: 3 Bots'] * 2
all_confitions_figsize = (10.5, 6)

boxplot_score = create_boxplot(score_data, 'Score', 'Boxplot of TODO', all_conditions_colors,
                               all_conditions_hatch_patterns, 4.5, all_conditions_xtick_labels,
                               all_confitions_figsize)
boxplot_score.savefig('plots/boxplot_score_sem_vs_nonsem.pdf', format='pdf')
boxplot_score.show()
