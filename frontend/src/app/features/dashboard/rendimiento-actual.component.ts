import { Component, OnDestroy, OnInit, inject,  signal } from '@angular/core';
import { RendimientoService } from '../../core/services/rendimiento.service';
import { timer, Subscription, forkJoin } from 'rxjs';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-rendimiento-actual',
  templateUrl: './rendimiento-actual.component.html',
  styleUrl: './rendimiento-actual.component.css',
  standalone: true
})
export class RendimientoActualComponent implements OnInit, OnDestroy {
  private rendimientoService = inject(RendimientoService);
  private subscriptionIntervalo!: Subscription;

  rendimientoActualUbuntu = signal<any>(null);
  rendimientoActualDebian = signal<any>(null);
  esMaquinaOnline(timestampMongo: string | undefined): boolean {
    if (!timestampMongo) return false;

    const fechaUltimoDato = new Date(timestampMongo).getTime();
    const fechaActual = new Date().getTime();

    return (fechaActual - fechaUltimoDato) < 60000;

  }
  protected readonly title = signal('Rendimiento Actual');
  ngOnInit() {
    this.subscriptionIntervalo = timer(0, 10000).pipe(
    switchMap(() => forkJoin({
      ubuntu: this.rendimientoService.obtenerRendimientoActual("servidor-ubuntu"),
      debian: this.rendimientoService.obtenerRendimientoActual("servidor-debian")
    })) 
    )
    .subscribe({
      next: (data) => {
        this.rendimientoActualUbuntu.set({...data.ubuntu});
        this.rendimientoActualDebian.set({...data.debian});
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