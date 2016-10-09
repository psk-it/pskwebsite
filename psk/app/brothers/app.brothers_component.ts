import { Component } from '@angular/core';
import { Brother, BrotherComponent } from './app.brother_component'

var readStringFromFileAtPath = function(pathOfFileToReadFrom)
{
    var request = new XMLHttpRequest();
    request.open("GET", pathOfFileToReadFrom, false);
    request.send(null);
    var returnValue = request.responseText;

    return returnValue;
}

var bros_json = readStringFromFileAtPath("data/brothers.json");

var BROTHERS = JSON.parse(bros_json);

var SENIORS = [];
var JUNIORS = [];
var SOPHOMORES = [];
var FRESHMEN = [];
for (var i =  0; i < BROTHERS.length; i++) {
    BROTHERS[i]['picture'] = "img/brothers/" + BROTHERS[i]['picture'];
    if (BROTHERS[i]['class'] == 'Senior')
        SENIORS.push(BROTHERS[i]);
    if (BROTHERS[i]['class'] == 'Junior')
        JUNIORS.push(BROTHERS[i]);
    if (BROTHERS[i]['class'] == 'Sophomore')
        SOPHOMORES.push(BROTHERS[i]);
    if (BROTHERS[i]['class'] == 'Freshman')
        FRESHMEN.push(BROTHERS[i]);
}

console.log(FRESHMEN);

@Component({
  selector: 'brothers',
  templateUrl: 'views/brothers.html',
  directives: [BrotherComponent]
})
export class BrothersComponent {

	brothers: Brother[];
	seniors: Brother[];
	juniors: Brother[];
	sophomores: Brother[];
	freshmen: Brother[];

	constructor(){
		this.brothers=BROTHERS;
		this.seniors=SENIORS;
		this.juniors=JUNIORS;
		this.sophomores=SOPHOMORES;
		this.freshmen=FRESHMEN;
	}
}
