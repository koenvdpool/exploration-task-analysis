from utils import count_human_participants, analyze_total_trials
import pandas as pd

file_paths = [
    ('../csv_data/nonsem_1bot_5hum.csv', 'nonsem-1bot-5hum'),
    ('../csv_data/filtered/filtered_nonsem_1bot_5hum.csv', 'filtered nonsem-1bot-5hum'),
    ('../csv_data/nonsem_3bots_3hum.csv', 'nonsem-3bots-3hum'),
    ('../csv_data/filtered/filtered_nonsem_3bots_3hum.csv', 'filtered nonsem-3bots-3hum'),
    ('../csv_data/sem_3bots_3hum.csv', 'sem-3bots-3hum'),
    ('../csv_data/filtered/filtered_sem_3bots_3hum.csv', 'filtered sem-3bots-3hum')

]

human_counts = []
total_trials_analyses = []

for path, description in file_paths:
    human_count = count_human_participants(path)
    total_trials_analysis = analyze_total_trials(path)

    human_counts.append({"Description": description, "Human Count": human_count})
    total_trials_analyses.append({
        "Description": description,
        "Mean Total Trials": total_trials_analysis["average_total_trials"],
        "STD Total Trials": total_trials_analysis["std_total_trials"]
    })


human_counts_df = pd.DataFrame(human_counts)
total_trials_analyses_df = pd.DataFrame(total_trials_analyses)


print("Human Counts Table:")
print(human_counts_df.to_string(index=False))

print("\nTotal Trials Analysis Table:")
print(total_trials_analyses_df.to_string(index=False))
