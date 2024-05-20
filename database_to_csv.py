import pymysql.cursors
from db import db_config
from utils import list_dicts2csv


# ---------- DATABASE CONNECTION ----------
def get_connection():
    """ TODO."""
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor)


# ---------- QUERY EXECUTION FUNCTION ----------
def execute_query(is_semantic, bot_num):
    """ TODO. """
    query_template = """
        SELECT part.pID AS ParticipantID, 
                exp.id AS GroupID, 
                (COUNT(DISTINCT gameState.itemId) - 6) AS ItemsFound, 
                part.score AS Score, 
                COUNT(DISTINCT trials.trialSequence) AS TotalTrials, 
                part.isRobot
        FROM cce_experiments.participants part 
        LEFT JOIN cce_experiments.experiments exp 
            ON exp.id = part.experimentID 
        LEFT JOIN cce_experiments.gamestate gameState 
            ON gameState.participantID = part.pID
        LEFT JOIN cce_experiments.trials trials
            ON trials.pID = part.pID
        WHERE exp.isSemantic = %s AND exp.botNums = %s
        GROUP BY exp.id, part.pID, part.score
        ORDER BY exp.id, part.pID;
    """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_template, (is_semantic, bot_num))
            return cursor.fetchall()


# ---------- SAVE TO CSV FUNCTION ----------
def save_to_csv(is_semantic, bot_num, filename):
    """ TODO. """
    raw_data = execute_query(is_semantic, bot_num)
    list_dicts2csv(raw_data, filename)


# ---------- EXECUTE AND SAVE DATA ----------
# Condition: semantic and hybrid (bots = 1, humans = 5)
# save_to_csv(is_semantic=1, bot_num=1, filename='csv_data/sem_1bot_5hum.csv')

# Condition: semantic and hybrid (bots = 3, humans = 3)
save_to_csv(is_semantic=1, bot_num=3, filename='csv_data/sem_3bots_3hum.csv')

# Condition: non-semantic and hybrid (bots = 1, humans = 5)
# save_to_csv(is_semantic=0, bot_num=1, filename='csv_data/nonsem_1bot_5hum.csv')

# Condition: non-semantic and hybrid (bots = 3, humans = 3)
# save_to_csv(is_semantic=0, bot_num=3, filename='csv_data/nonsem_3bots_3hum.csv')
