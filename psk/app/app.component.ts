import { Component } from '@angular/core';
import { Brother, BrotherComponent} from './brothers/app.brother_component'
import { NavBarComponent} from './navbar/app.navbar_component'
import { RushComponent} from './rush/app.rush_component'
import { BrothersComponent} from './brothers/app.brothers_component'



@Component({
	selector: 'app-body',
	templateUrl: 'views/main.html',
	directives: [NavBarComponent, BrotherComponent, RushComponent, BrothersComponent]
})

export class AppComponent{
}