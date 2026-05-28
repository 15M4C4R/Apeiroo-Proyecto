import { Component} from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ComandoComponent } from './features/ssh/comando.component';
import { RendimientoActualComponent } from './features/dashboard/rendimiento-actual.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ComandoComponent, RendimientoActualComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = 'Panel de Control de MVs';
}