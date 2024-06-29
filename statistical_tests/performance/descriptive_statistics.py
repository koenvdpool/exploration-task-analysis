import pandas as pd
from scripts.utils import calculate_statistics

file_info = [
    ('../../data/performance/nonsem_1bot_5hum.csv', 'Human: Non-Semantic 1B5H', 0),
    ('../../data/performance/nonsem_1bot_5hum.csv', 'Bot: Non-Semantic 1B5H', 1),
    ('../../data/performance/nonsem_1bot_5hum.csv', 'All: Non-Semantic 1B5H', None),
    ('../../data/performance/nonsem_3bots_3hum.csv', 'Human: Non-Semantic 3B3H', 0),
    ('../../data/performance/nonsem_3bots_3hum.csv', 'Bot: Non-Semantic 3B3H', 1),
    ('../../data/performance/nonsem_3bots_3hum.csv', 'All: Non-Semantic 3B3H', None),
    ('../../data/performance/archive/sem_3bots_3hum.csv', 'Human: Semantic 3B3H', 0),
    ('../../data/performance/archive/sem_3bots_3hum.csv', 'Bot: Semantic 3B3H', 1),
    ('../../data/performance/archive/sem_3bots_3hum.csv', 'All: Semantic 3B3H', None),
    ('../../data/performance/nonsem_6hum.csv', 'Human: Non-Semantic 6H', 0),
    ('../../data/performance/6bots.csv', 'Bot: Non-Semantic 6B', 1),
]

# Process each file
for i, (file_path, file_name, is_robot_filter) in enumerate(file_info):
    df = pd.read_csv(file_path)
    stats_df = calculate_statistics(df, is_robot_filter)
    print(f'Statistics for {file_name} (isRobot = {is_robot_filter}, {stats_df[1]} participants):')
    print(stats_df[0])
    print()

    # Print separator after every three files
    if (i + 1) % 3 == 0:
        print("-----------------------------")
