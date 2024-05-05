import mysql.connector
from venv import logger
import os
import json
from dotenv import load_dotenv

load_dotenv()


def save_data_into_DB(data):
    try:
        connection = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            database="job-management",
        )
        cursor = connection.cursor()

        # query = "INSERT INTO `crawl_data` (`id`,`title`,`time`,`city`,`level`,`work_way`,`company`,`workWay`,`right`,`company`,`job`,`place`,`numberEmployee`,`experience`,`level`,`salary`,`education`,`description`,`requirement`,`deadline`,`images`,`link`,`type`,`contact`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql = "INSERT INTO crawl_data ({}) VALUES ({})".format(
            ", ".join(data.keys()), ", ".join(["%s"] * len(data))
        )
        cursor.execute(sql, list(map(str, data.values())))
        connection.commit()
        connection.close()
        print('saved new data')
    except Exception as e:
        logger.error(f"Error occurred while saving data to DB: {e}")
