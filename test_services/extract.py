import psycopg2


def fetch_user(user_id: str):
    conn = psycopg2.connect(dsn="postgresql://localhost/mydb")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()
