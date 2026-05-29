import time
import requests
import psutil
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_URL = "http://172.30.2.158:5000/api/rendimiento/"
VM_ID = "{VM_ID_PLACEHOLDER}"

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def collect_and_send():
    while True:
        cpu_uso = psutil.cpu_percent(interval=1)
        ram_uso = psutil.virtual_memory().percent
        almacenamiento_uso = psutil.disk_usage('/').percent
        procesos = sorted([
            {
                'pid': p.info['pid'],
                'memoria_uso': round(p.info['memory_percent'], 2) if p.info['memory_percent'] is not None else 0
            }
            for p in psutil.process_iter(['pid', 'memory_percent'])
        ],
            key = lambda x: x['memoria_uso'],
            reverse = True
        )[:5]

        payload = {
            "vm_id": VM_ID,
            "cpu_uso": cpu_uso,
            "ram_uso": ram_uso,
            "almacenamiento_uso": almacenamiento_uso,
            "procesos": procesos
        }
        try:
            response = session.post(API_URL, json=payload, timeout=3)
            print(f"Enviado: {payload} - Respuesta: {response.status_code}")
        except Exception as e:
            print(f"Error al enviar métricas: {e}")

        time.sleep(10)

if __name__ == "__main__":
    collect_and_send()