import datetime
from backend.utils.alert import send_alert
from db import get_db

db = get_db()

def comprobar_alertas(documento):
    comprobar_alerta_componente(documento.get("vm_id"), "CPU", documento.get("cpu_uso"), 80, 30)
    comprobar_alerta_componente(documento.get("vm_id"), "RAM", documento.get("ram_uso"), 80, 30)
    comprobar_alerta_componente(documento.get("vm_id"), "Almacenamiento", documento.get("almacenamiento_uso"), 80, 30)

def comprobar_alerta_componente(vm_id, componente, valor_actual, umbral, racha_maxima):
    alerta_id = f"{vm_id}_{componente}"
    ahora = datetime.datetime.now(datetime.timezone.utc)
    
    estado_componente = db["estado_alerta"].find_one({"_id": alerta_id})
    
    cambios_pendientes = False
    
    if not estado_componente:
        estado_componente = {
            "_id": alerta_id,
            "vm_id": vm_id,
            "componente": componente,
            "racha": 0,
            "estado": "Normal",
            "ultimo_aviso": None
        }
        db["estado_alerta"].insert_one(estado_componente)
    
    if valor_actual > umbral:
        if estado_componente.get("estado") =="Normal":
            estado_componente["racha"] += 1
            cambios_pendientes = True
            
            if estado_componente.get("racha") >= racha_maxima:
                estado_componente["estado"] = "Alerta"
                estado_componente["ultimo_aviso"] = ahora
                send_alert(vm_id, componente, valor_actual)
                
        else:
            ultimo_aviso = estado_componente.get("ultimo_aviso")
            
            if ultimo_aviso and ultimo_aviso.tzinfo is None:
                ultimo_aviso = ultimo_aviso.replace(tzinfo=datetime.timezone.utc)
                
            if ultimo_aviso and (ahora - ultimo_aviso) >= datetime.timedelta(minutes=5):
                send_alert(vm_id, componente, valor_actual)
                estado_componente["ultimo_aviso"] = ahora
                cambios_pendientes = True
    else:
        if estado_componente.get("estado") == "Alerta" or estado_componente.get("racha") > 0:
            estado_componente["estado"] = "Normal"
            estado_componente["racha"] = 0
            cambios_pendientes = True
    
    if cambios_pendientes:
        db["estado_alerta"].update_one({"_id": alerta_id}, {"$set": estado_componente})

        
        