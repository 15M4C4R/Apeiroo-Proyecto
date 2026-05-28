import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class RendimientoService {
    private http = inject(HttpClient);
    private apiUrl = 'http://172.30.2.158:5000/api/rendimiento';

    obtenerRendimiento(): Observable<any> {
        return this.http.get(this.apiUrl);
    }

    obtenerRendimientoActual(nombre_vm: string): Observable<any> {
        return this.http.get(this.apiUrl + "/" + nombre_vm + "/actual");
    }

    obtenerRendimientoHistorico(nombre_vm: string): Observable<any> {
        return this.http.get(this.apiUrl + "/" + nombre_vm + "/historico");
    }

}