from enum import Enum
import json

class MessageJson(Enum):
    JSON_ERROR = json.dumps({
        'status': 'Invalid json data or structure.',
        'system_status': 'false'
    })
    INSERT_SUCCESS = json.dumps({
        'status': 'Insert success',
        'system_status': 'true'
    })
    INSERT_FAILED = json.dumps({
        'status': 'Insert failed',
        'system_status': 'false'
    })
    DELETE_SUCCESS = json.dumps({
        'status': 'Delete success',
        'system_status': 'true'
    })
    DELETE_FAILED = json.dumps({
        'status': 'Delete failed',
        'system_status': 'false'
    })
    REQUEST_FAILED = json.dumps({
        'status': 'Request failed',
        'system_status': 'false'
    })
    