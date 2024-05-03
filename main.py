import pymysql.cursors
from db import db_config

# Connect to the database
connection = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database'],
    cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT pID, score FROM cce_experiments.participants part LEFT JOIN cce_experiments.experiments exp on exp.id = part.experimentID and exp.isSemantic = 1 and botNums = 5;"
        # sql = "SELECT id FROM `experiments` WHERE isSemantic = 1 AND botNums = 5"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
