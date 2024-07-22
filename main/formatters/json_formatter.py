# main/formatters/json_formatter.py
import logging
import json
from datetime import datetime, timezone

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
            'level': record.levelname,
            'message': record.msg if isinstance(record.msg, dict) else record.getMessage(),
        }
        return json.dumps(log_record)
