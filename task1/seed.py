import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection

_COUNT_OF_USERS = 3000
_COUNT_OF_TASKS = 10000
_TASK_STATUSES = ["new", "in progress", "completed"]


def insert_fake_users(conn):
    insert_users_sql_statement = """
INSERT INTO users (fullname, email) VALUES (%s, %s);
"""

    faker = Faker("en_US")

    try:
        with conn.cursor() as cur:
            for _ in range(_COUNT_OF_USERS):
                cur.execute(
                    insert_users_sql_statement, (faker.name(), faker.unique.email())
                )

        conn.commit()
        logging.info("Users inserted successfully")

    except DatabaseError as err:
        logging.error(f"Database error: {err}. Rollbacking...")
        conn.rollback()


def insert_statuses(conn):
    insert_statuses_sql_statement = """
INSERT INTO status (name) VALUES (%s);
    """

    try:
        with conn.cursor() as cur:
            for status in _TASK_STATUSES:
                cur.execute(insert_statuses_sql_statement, (status,))

        conn.commit()
        logging.info("Statuses inserted successfully")

    except DatabaseError as err:
        logging.error(f"Database error: {err}. Rollbacking...")
        conn.rollback()


def insert_tasks(conn):
    insert_tasks_sql_statement = """
INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);
    """

    faker = Faker("en_US")

    try:
        with conn.cursor() as cur:
            for _ in range(_COUNT_OF_TASKS):
                cur.execute(
                    insert_tasks_sql_statement,
                    (
                        faker.sentence(),
                        faker.text(),
                        randint(1, len(_TASK_STATUSES)),
                        randint(1, _COUNT_OF_USERS),
                    ),
                )

        conn.commit()
        logging.info("Tasks inserted successfully")

    except DatabaseError as err:
        logging.error(f"Database error: {err}. Rollbacking...")
        conn.rollback()


if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    with create_connection() as connection:
        insert_fake_users(connection)
        insert_statuses(connection)
        insert_tasks(connection)