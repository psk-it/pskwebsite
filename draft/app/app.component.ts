import { Component } from '@angular/core';
import { Brother, BrotherComponent} from './app.brother_component'
import { NavBarComponent} from './app.navbar_component'

const BROTHERS: Brother[]=[
	{photo_file: 'img/head.jpg', name:'Michael Traub', major:'8,18C',year: '2017'},
	{photo_file: 'img/head.jpg', name:'SchMichael Traub', major:'8,18C',year: '2017'}
];
@Component({
	selector: 'app-body',
	templateUrl: 'views/main.html',
	directives: [NavBarComponent, BrotherComponent]
})

export class AppComponent{
	brothers=BROTHERS;
	constructor(){
		console.log("app-body component ctor");
	}
}