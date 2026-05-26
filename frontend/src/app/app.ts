import { Component, OnInit, inject,  signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RendimientoService } from './core/services/rendimiento.service';
import { KeyValuePipe } from '@angular/common';
import { timer, Subscription } from 'rxjs';
import { switchMap } from 'rxjs/operators';
//import { Rendimiento } from './core/model/rendimiento.model';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, KeyValuePipe],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  private rendimientoService = inject(RendimientoService);

  private subscriptionIntervalo!: Subscription;

  respuesta: any;
  protected readonly title = signal('frontend');
  ngOnInit() {
    this.subscriptionIntervalo = timer(0, 10000).pipe(
    switchMap(() => this.rendimientoService.obtenerRendimiento())
    )
    .subscribe({
      next: (data) => {
        this.respuesta = data;
        console.log("Datos recibidos de Flask: ", data);
      },
      error: (error) => {
        console.error("Error al obtener los datos de Flask: ", error)
      },
    });
  }

  ngOnDestroy() {
    if(this.subscriptionIntervalo) {
      this.subscriptionIntervalo.unsubscribe();
    }
  }
}