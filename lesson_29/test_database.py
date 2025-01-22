import psycopg2


def test_db_connect():
    conn = psycopg2.connect(
        dbname="kris_db",
        user="kris",
        password="kris",
        host="db",
        port="5432"
    )
    assert conn is not None

def test_data_insert():
    conn = psycopg2.connect(
        dbname="kris_db",
        user="kris",
        password="kris",
        host="db",
        port="5432"
    )
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
    cursor.execute("SELECT * FROM registration WHERE id=1")
    result = cursor.fetchone()
    assert result[1] == 'Alex'

def test_data_update():
    conn = psycopg2.connect(
        dbname="kris_db",
        user="kris",
        password="kris",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE registration
        SET name = 'Kate' 
        WHERE id = 1
    """)
    conn.commit()
    cursor.execute("SELECT * FROM registration WHERE id=1")
    conn.commit()
    result = cursor.fetchone()
    assert result[1] == 'Kate'

def test_data_select():
    conn = psycopg2.connect(
        dbname="kris_db",
        user="kris",
        password="kris",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    conn.commit()
    cursor.execute("SELECT name FROM registration WHERE id=1")
    result = cursor.fetchone()
    assert result[0] == 'Kate'


def test_data_delete():
    conn = psycopg2.connect(
        dbname="kris_db",
        user="kris",
        password="kris",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registration WHERE id=1")
    conn.commit()
    cursor.execute("SELECT name FROM registration WHERE id=1")
    conn.commit()
    result = cursor.fetchone()
    cursor.execute("""
                         DROP TABLE users
                         """)
    conn.commit()
    assert result is None
