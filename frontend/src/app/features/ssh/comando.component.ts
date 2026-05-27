import { Component, inject } from '@angular/core';
import { EjecutarService, DatosComando } from '../../core/services/ejecutar.service';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
    selector: 'app-comando',
    templateUrl: './comando.component.html',
    styleUrl: './comando.component.css',
    standalone: true, 
    imports: [ReactiveFormsModule, CommonModule]
})
export class ComandoComponent {
    private ejecutarService = inject(EjecutarService);
    private fb = inject(FormBuilder);

    formularioComando: FormGroup = this.fb.group({
        host: ['', Validators.required],
        usuario: ['', Validators.required],
        contraseña: ['', Validators.required],
        comando: ['', Validators.required]
    })

    salidaTerminal: string = '';
    cargando: boolean = false;

    mandarComando() {
        if (this.formularioComando.invalid) {
            alert('Por favor, rellene todos los campos.');
            return;
        }

        this.cargando = true;
        this.salidaTerminal = 'Ejecutando...';

        const payload: DatosComando = this.formularioComando.value;

        this.ejecutarService.ejecutar(payload).subscribe({
            next: (data) => {
                this.cargando = false;
                this.salidaTerminal = data.salida_terminal;
                console.log("Exito: ", data.mensaje)
                console.log("Salida de la terminal: ", data.salida_terminal)
            },
            error: (error) => {
                this.cargando = false;
                this.salidaTerminal = `Error: ${error.error}`;
                console.error("Error al ejecutar el comando en la maquina virtual: ", error.error)
            }
        });
    }

}