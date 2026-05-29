import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import  { Observable } from 'rxjs';
import { ConfigAlertas } from '../models/configuracion.model'
import { environment } from '../../../environments/environment'

@Injectable({
    providedIn: 'root'
})
export class ConfiguracionService {
    private http = inject(HttpClient)
    private apiUrl = environment.apiUrl + '/configuracion'

    obtenerConfiguracion(): Observable<ConfigAlertas> {
        return this.http.get<ConfigAlertas>(this.apiUrl);
    }

    actualizar(config: ConfigAlertas): Observable<ConfigAlertas> {
        return this.http.put<ConfigAlertas>(this.apiUrl, config);
    }

}