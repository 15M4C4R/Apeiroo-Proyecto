import { model } from '@angular/core';
import { Directive } from '@angular/core';

@Directive({ selector: 'rendimiento' })
export class Rendimiento {
    vm_id = model<string>();
    cpu_uso = model<number>();
    ram_uso = model<number>();
    almacenamiento_uso = model<number>();
}