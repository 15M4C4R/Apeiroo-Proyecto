from db import get_db

db = get_db()

def insertar_rendimiento(rendimiento):
    db["rendimiento"].insert_one(rendimiento)
    
def buscar_rendimiento_por_id(vm_id):
    return db["rendimiento"].find_one({"vm_id": vm_id}, {"_id": 0}, sort=[("timestamp", -1)])

def buscar_rendimiento_historico_por_id(vm_id):
    return list(db["rendimiento"].find({"vm_id": vm_id}, {"_id":0}).sort("timestamp", -1).limit(50))