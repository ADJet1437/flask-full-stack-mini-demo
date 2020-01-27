"""
Insert some data to mysql
"""

from sqlalchemy import create_engine


# Ideally, should have a conf file to store credential information
# Here I just hardcoded
mysql_url = "mysql+pymysql://{user}:{passwd}@{host}:{port}/?charset={charset}" \
    .format(host="flask-db",
            port="3306",
            user="root",
            passwd="password",
            charset='utf8'
            )

db = create_engine(mysql_url)

drop_query = "DROP TABLE IF EXISTS front.templates;"

query_to_create_table = """
    CREATE TABLE IF NOT EXISTS front.templates (
           id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
           title VARCHAR(55) NOT NULL,
           small_title VARCHAR(55) NOT NULL,
           create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       ) ENGINE=INNODB;
"""


def create_table():
    """Create a table call "front"
    """
    with db.connect() as conn:
        conn.execute(drop_query)
        conn.execute(query_to_create_table)


def insert_data():
    """
    Insert data into table front
    """
    query_to_insert = """
                INSERT INTO front.templates 
                       ( title, small_title)
                       VALUES
                       ( "New title"," New custom small title");
    """
    with db.connect() as conn:
        conn.execute(query_to_insert)


if __name__ == "__main__":
    create_table()
    insert_data()