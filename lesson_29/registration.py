import psycopg2


# Функція підключення до бази даних
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="kris",
        password="kris"
    )
    return conn


# Вставка результатів реєстрації в базу даних
def insert_registration_result(first_name, last_name, email, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO registration_results_ (first_name, last_name, email, status)
    VALUES (%s, %s, %s, %s) RETURNING id;
    """
    cursor.execute(insert_query, (first_name, last_name, email, status))

    inserted_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return inserted_id


# Оновлення статусу реєстрації
def update_registration_status(record_id, new_status):
    conn = get_db_connection()
    cursor = conn.cursor()

    update_query = """
    UPDATE registration_results_
    SET status = %s
    WHERE id = %s;
    """
    cursor.execute(update_query, (new_status, record_id))

    conn.commit()
    cursor.close()
    conn.close()


# Вибірка всіх результатів
def fetch_all_results():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM registration_results_;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


# Видалення запису за id
def delete_registration_result(record_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    delete_query = "DELETE FROM registration_results WHERE id = %s;"
    cursor.execute(delete_query, (record_id,))

    conn.commit()
    cursor.close()
    conn.close()
