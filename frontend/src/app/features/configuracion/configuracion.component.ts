import { Component, inject, OnInit, PLATFORM_ID } from "@angular/core";
import { FormBuilder, ReactiveFormsModule, Validators, FormGroup } from "@angular/forms";
import { ConfiguracionService } from "../../core/services/configuracion.service";
import { CommonModule, isPlatformBrowser } from "@angular/common"

@Component({
    selector: 'app-configuracion',
    templateUrl: './configuracion.component.html',
    styleUrl: './configuracion.component.css',
    standalone: true,
    imports: [ReactiveFormsModule, CommonModule]
})
export class ConfiguracionComponent implements OnInit {
    private configService = inject(ConfiguracionService);
    private fb = inject(FormBuilder);
    private platformId = inject(PLATFORM_ID);

    configForm: FormGroup;

    constructor() {
        this.configForm = this.fb.group({
            umbral_cpu: [0, [Validators.required, Validators.min(0), Validators.max(100)]],
            umbral_ram: [0, [Validators.required, Validators.min(0), Validators.max(100)]],
            umbral_almacenamiento: [0, [Validators.required, Validators.min(0), Validators.max(100)]],
            minutos_tolerancia: [1, [Validators.required, Validators.min(0)]],
            correo_destino: ['', [Validators.required, Validators.email]]
        });
    }
    

    ngOnInit() {
        if (isPlatformBrowser(this.platformId)) {
            this.cargarDatos();
        }
    }

    cargarDatos() {
        this.configService.obtenerConfiguracion().subscribe((datosActuales) => {
            if(datosActuales) {
                this.configForm.patchValue(datosActuales);
            }
        })
    }

    actualizar() {
        if (this.configForm.valid) {
            this.configService.actualizar(this.configForm.value).subscribe(() => {
                alert('Configuración actualizada correctamente');
            })
        } else {
            this.configForm.markAllAsTouched();
        }
    }

}