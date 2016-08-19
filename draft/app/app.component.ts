import { Component } from '@angular/core';
import { Brother, BrotherComponent} from './app.brother_component'
import { NavBarComponent} from './app.navbar_component'

var readStringFromFileAtPath = function(pathOfFileToReadFrom)
{
    var request = new XMLHttpRequest();
    request.open("GET", pathOfFileToReadFrom, false);
    request.send(null);
    var returnValue = request.responseText;

    return returnValue;
}

var bros_json = readStringFromFileAtPath("brothers.json");

var BROTHERS = JSON.parse(bros_json);


var SENIORS = [];
var JUNIORS = [];
var SOPHOMORES = [];
for (var i =  0; i < BROTHERS.length; i++) {
    BROTHERS[i]['picture'] = "img/brothers/" + BROTHERS[i]['picture'];
    if (BROTHERS[i]['class'] == 'Senior')
        SENIORS.push(BROTHERS[i]);
    if (BROTHERS[i]['class'] == 'Junior')
        JUNIORS.push(BROTHERS[i]);
    if (BROTHERS[i]['class'] == 'Sophomore')
        SOPHOMORES.push(BROTHERS[i]);
}

@Component({
	selector: 'app-body',
	templateUrl: 'views/main.html',
	directives: [NavBarComponent, BrotherComponent]
})

export class AppComponent{
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
		console.log("app-body component ctor");
	}
}