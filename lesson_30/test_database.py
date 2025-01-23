import psycopg2
import allure


def test_db_connect():
    conn = psycopg2.connect(
        dbname="kris_db",
        user="kris",
        password="kris",
        host="db",
        port="5432"
    )
    assert conn is not None


@allure.feature('Database Connection')
@allure.story('Insert Data')
def test_data_insert():
    with allure.step("Connecting to the database"):
        conn = psycopg2.connect(
            dbname="kris_db",
            user="kris",
            password="kris",
            host="db",
            port="5432"
        )

    with allure.step("Creating table and inserting data"):
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE registration
        (
            id INT primary key,
            name VARCHAR
        )
        """)
        conn.commit()
        cursor.execute("INSERT INTO registration (id, name) VALUES (1, 'Alex')")
        conn.commit()

    with allure.step("Verifying inserted data"):
        cursor.execute("SELECT * FROM registration WHERE id=1")
        result = cursor.fetchone()
        assert result[1] == 'Alex'


@allure.feature('Database Connection')
@allure.story('Update Data')
def test_data_update():
    with allure.step("Connecting to the database"):
        conn = psycopg2.connect(
            dbname="kris_db",
            user="kris",
            password="kris",
            host="db",
            port="5432"
        )

    with allure.step("Updating table data"):
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE registration
            SET name = 'Kate' 
            WHERE id = 1
        """)
        conn.commit()
        cursor.execute("SELECT * FROM registration WHERE id=1")
        conn.commit()

    with allure.step("Verifying updated data"):
        result = cursor.fetchone()
        assert result[1] == 'Kate'


@allure.feature('Database Connection')
@allure.story('Select Data')
def test_data_select():
    with allure.step("Connecting to the database"):
        conn = psycopg2.connect(
            dbname="kris_db",
            user="kris",
            password="kris",
            host="db",
            port="5432"
        )

    with allure.step("Selecting data and verifying the date"):
        cursor = conn.cursor()
        conn.commit()
        cursor.execute("SELECT name FROM registration WHERE id=1")
        result = cursor.fetchone()
        assert result[0] == 'Kate'


@allure.feature('Database Connection')
@allure.story('Delete Data')
def test_data_delete():
    with allure.step("Connecting to the database"):
        conn = psycopg2.connect(
            dbname="kris_db",
            user="kris",
            password="kris",
            host="db",
            port="5432"
        )

    with allure.step("Deleting table data"):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM registration WHERE id=1")
        conn.commit()

    with allure.step("Verifying deleted data"):
        cursor.execute("SELECT name FROM registration WHERE id=1")
        conn.commit()
        result = cursor.fetchone()
        cursor.execute("""
                             DROP TABLE users
                             """)
        conn.commit()
        assert result is None
