from utils import get_col_as_ints, create_boxplot


ITEM_COLUMN_INDEX = 2

# Condition: TEST
test_items = get_col_as_ints('csv_data/test.csv', ITEM_COLUMN_INDEX)


# ---------- EXTRACT ITEMS: SEMANTIC ----------
# Condition: semantic and all humans
sem_6hum_items = get_col_as_ints('csv_data/sem_6hum.csv', ITEM_COLUMN_INDEX, delimiter=';')

# Condition: semantic and all bots
sem_6bots_items = test_items

# Condition: semantic and hybrid (bots = 1, humans = 5)
sem_1bot_5hum_items = test_items

# Condition: semantic and hybrid (bots = 3, humans = 3)
sem_3bots_3hum_items = get_col_as_ints('csv_data/sem_3bots_3hum.csv', ITEM_COLUMN_INDEX)


# ---------- EXTRACT ITEMS: NON-SEMANTIC ----------
# Condition: non-semantic and all humans
nonsem_6hum_items = get_col_as_ints('csv_data/nonsem_6hum.csv', ITEM_COLUMN_INDEX, delimiter=';')

# Condition: non-semantic and all bots
nonsem_6bots_items = test_items

# Condition: non-semantic and hybrid (bots = 1, humans = 5)
nonsem_1bot_5hum_items = test_items

# Condition: non-semantic and hybrid (bots = 3, humans = 3)
nonsem_3bots_3hum_items = test_items


# ---------- COMBINE DATA ----------
items_data = [sem_6hum_items, sem_6bots_items, sem_1bot_5hum_items, sem_3bots_3hum_items,
              nonsem_6hum_items, nonsem_6bots_items, nonsem_1bot_5hum_items, nonsem_3bots_3hum_items]


# ---------- CREATE ITEM FIGURE ----------
boxplot_items = create_boxplot(items_data, "Number of Items Found", 'Boxplot of TODO.')
boxplot_items.savefig('plots/boxplot_items_sem_vs_nonsem.pdf', format='pdf')
boxplot_items.show()
