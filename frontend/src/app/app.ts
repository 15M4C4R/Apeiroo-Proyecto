import { Component, OnInit, inject,  signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  http = inject(HttpClient);
  respuesta: any;
  protected readonly title = signal('frontend');
  ngOnInit() {
    this.http.get('http://127.0.0.1:5000/').subscribe(data => this.respuesta = data);
  }
}