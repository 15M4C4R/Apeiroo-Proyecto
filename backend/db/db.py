from pymongo import MongoClient

_client = None
_db = None

def get_db():
    global _client, _db
    if _client is None:
        _client = MongoClient('mongodb://localhost:27017/')
        _db = _client['apeiroo_db']
        
        if 'rendimiento' not in _db.list_collection_names():
            _db.create_collection(
                'rendimiento',
                timeseries = {
                    'timeField': 'timestamp',
                    'metaField': 'vm_name',
                    'granularity': 'seconds'
                }
            )
    return _db