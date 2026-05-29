import {Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface DatosComando {
    host: string,
    usuario: string,
    contraseña: string, 
    comando: string
}

@Injectable({
    providedIn: 'root'
})
export class EjecutarService {
    private http = inject(HttpClient)
    private apiUrl = 'http://localhost:5000/api/ejecutar-comando/';

    ejecutar(datos: DatosComando): Observable<any> {
        return this.http.post(this.apiUrl, datos);
    }
}