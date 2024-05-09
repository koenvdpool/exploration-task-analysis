from utils import get_col_as_ints, create_boxplot


SCORE_COLUMN_INDEX = 3

# Condition: TEST
test_score = get_col_as_ints('csv_data/test.csv', SCORE_COLUMN_INDEX)


# ---------- EXTRACT SCORES: SEMANTIC ----------
# Condition: semantic and all humans
sem_6hum_score = get_col_as_ints('csv_data/sem_6hum.csv', SCORE_COLUMN_INDEX, delimiter=';')

# Condition: semantic and all bots
sem_6bots_score = test_score

# Condition: semantic and hybrid (bots = 1, humans = 5)
sem_1bot_5hum_score = test_score

# Condition: semantic and hybrid (bots = 3, humans = 3)
sem_3bots_3hum_score = get_col_as_ints('csv_data/sem_3bots_3hum.csv', SCORE_COLUMN_INDEX)


# ---------- EXTRACT SCORES: NON-SEMANTIC ----------
# Condition: non-semantic and all humans (bots = 0)
nonsem_6hum_score = get_col_as_ints('csv_data/nonsem_6hum.csv', SCORE_COLUMN_INDEX, delimiter=';')

# Condition: non-semantic and all bots (bots = 6)
nonsem_6bots_score = test_score

# Condition: non-semantic and hybrid (bots = 1, humans = 5)
nonsem_1bot_5hum_score = test_score

# Condition: non-semantic and hybrid (bots = 3, humans = 3)
nonsem_3bots_3hum_score = test_score


# ---------- COMBINE DATA ----------
score_data = [sem_6hum_score, sem_6bots_score, sem_1bot_5hum_score, sem_3bots_3hum_score,
              nonsem_6hum_score, nonsem_6bots_score, nonsem_1bot_5hum_score, nonsem_3bots_3hum_score]


# ---------- CREATE SCORE FIGURE ----------
boxplot_score = create_boxplot(score_data, "Score", 'Boxplot of TODO.')
boxplot_score.savefig('plots/boxplot_score_sem_vs_nonsem.pdf', format='pdf')
boxplot_score.show()
