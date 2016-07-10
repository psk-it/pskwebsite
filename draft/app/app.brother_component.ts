import { Component, Input } from '@angular/core';

export class Brother {
	photo_file: string;
	name: string;
	major: string;
	year:  string;

}
const BROTHERS: Brother[]=[


@Component({
  selector: 'brother-component',
  templateUrl: 'views/brother.html'
})

export class BrotherComponent {
	@Input() brother: Brother;
	constructor(){
		console.log("brother component ctor");
	}
	
}