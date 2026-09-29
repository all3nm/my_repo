def normalise_record(record):
    name = record.get("name", "").strip().lower()
    return {"name": name, "id": record["id"]}


def flatten_nested(data, prefix=""):
    result = {}
    for k, v in data.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.update(flatten_nested(v, key))
        else:
            result[key] = v
    return result
