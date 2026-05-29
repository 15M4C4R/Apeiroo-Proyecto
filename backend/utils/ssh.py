import io
import os
import paramiko

class Ssh:
    
    DESTINO = os.environ.get('DESTINO_SCRIPT_RENDIMIENTO')
    ORIGEN = os.environ.get('ORIGEN_SCRIPT_RENDIMIENTO')
    
    def __init__(self):
        self.host = ""
        self.username = ""
        self.password = ""
        self.client = None
    
    def conectar(self, host, usuario, contraseña):
        self.host = host
        self.username = usuario
        self.password = contraseña
        
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname = self.host, username = self.username, password = self.password) 
            return True, "Conexion exitosa"
        except Exception as e:
            return False, f"Error al conectarse a la maquina virtual: {str(e)}"
    
    def desconectar(self):
        if self.client:
            self.client.close()
        
    def ejecutar(self, comando):
        try:
            stdin, stdout, stderr = self.client.exec_command(comando)
            salida = stdout.read().decode('utf-8').strip()
            errores = stderr.read().decode('utf-8').strip()
            if errores:
                return False, errores
            return True, salida
        except Exception as e:
            return False, f"Error al ejecutar el comando: {str(e)}"
    
    def enviar_archivo(self, contenido_str, destino):
        try: 
            sftp = self.client.open_sftp()
            archivo_memoria = io.BytesIO(contenido_str.encode('utf-8'))
            sftp.putfo(archivo_memoria, destino)
            sftp.close()
            return True, "Archivo enviado exitosamente"
        except Exception as e:
            return False, f"Error al enviar archivo: {str(e)}" 
    
    def ejecutar_atomico(self, host, usuario, contraseña, comando):
        exito_conexion, msj_conexion = self.conectar(host, usuario, contraseña)
        if not exito_conexion:
            return {"exito": False, "mensaje": msj_conexion}
        exito_ejecucion, msj_ejecucion = self.ejecutar(comando)
        self.desconectar()
        return {"exito": exito_ejecucion, "mensaje": msj_ejecucion}

    def nueva_vm(self, vm_id, host, usuario, contraseña, origen):
        exito_conexion, msj_conexion = self.conectar(host, usuario, contraseña)
        if not exito_conexion:
            return {"exito": False, "mensaje": msj_conexion}
        try:
            with open(origen, 'r', encoding='utf-8') as f:
                script_original = f.read()
            script_listo = script_original.replace('"{VM_ID_PLACEHOLDER}"', f'"{vm_id}"')
            exito_envio, msj_envio = self.enviar_archivo(script_listo, self.DESTINO) 
        
        except Exception as e:
            self.desconectar()
            return {"exito": False, "mensaje": f"Error al enviar el script: {str(e)}"}

        self.desconectar()
        return {"exito": exito_envio, "mensaje": msj_envio}
