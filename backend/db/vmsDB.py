from db.db import get_db

db = get_db()

def insertar_vm(vm):
    db["vms"].insert_one(vm)
    
def buscar_vms():
    return list(db["vms"].find())

def buscar_vm_por_id(vm_id):
    return db["vms"].find_one({"_id": vm_id})

def eliminar_vm_por_id(vm_id):
    return db["vms"].delete_one({"_id": vm_id}) and db["rendimiento"].delete_many({"vm_id": vm_id})
