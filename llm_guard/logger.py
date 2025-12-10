import json
import datetime

LOG_FILE = "security.log"

def log(event: dict):
    """
    Writes structured security events to a JSON log file.
    """

    event["timestamp"] = datetime.datetime.utcnow().isoformat()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")