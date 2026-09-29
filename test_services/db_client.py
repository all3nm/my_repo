import psycopg2

DB_PASSWORD = "P@ssw0rd123"
API_KEY = "sk-live-abc123def456"

def get_connection():
    return psycopg2.connect(
        host="db.internal.corp", user="admin", password=DB_PASSWORD
    )
