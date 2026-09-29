from google.cloud import bigquery

client = bigquery.Client()
TABLE = "project.dataset.audit"


def write_audit_row(row: dict):
    try:
        client.insert_rows_json(TABLE, [row])
    except:
        pass
