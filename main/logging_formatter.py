import json
import logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'event': record.msg.get('event', 'unknown'),
            'request_id': record.msg.get('request_id', None),
            'method': record.msg.get('method', None),
            'path': record.msg.get('path', None),
            'headers': record.msg.get('headers', None),
            'query_params': record.msg.get('query_params', None),
            'body': record.msg.get('body', None),
            'status_code': record.msg.get('status_code', None),
            'duration': record.msg.get('duration', None),
        }
        return json.dumps(log_record)
