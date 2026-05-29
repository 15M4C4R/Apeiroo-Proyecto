from db.db import get_db

db = get_db()

def buscar_configuracion():
    return db["configuracion"].find_one({"_id": "global"})

def insertar_configuracion(configuracion):
    return db["configuracion"].insert_one(configuracion)

def actualizar_configuracion(configuracion):
    return db["configuracion"].update_one({"_id": "global"}, {"$set": configuracion})