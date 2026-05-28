from pymongo import MongoClient

_client = None
_db = None

def get_db():
    global _client, _db
    if _client is None:
        _client = MongoClient('mongodb://db_mongo:27017/')
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
        elif 'estado_alerta' not in _db.list_collection_names():
            _db.create_collection(
                'estado_alerta',
                timeseries = {
                    'timeField': 'timestamp',
                    'metaField': 'vm_name',
                    'granularity': 'minutes'
                }
            )
    return _db