import { Component } from '@angular/core';
import { Brother, BrotherComponent} from './brothers/app.brother_component'
import { NavBarComponent} from './navbar/app.navbar_component'
import { RushComponent} from './rush/app.rush_component'
import { BrothersComponent} from './brothers/app.brothers_component'
import { CultureComponent} from './culture/app.culture_component'
import { AboutUsComponent} from './aboutus/app.aboutus_component'
import { HouseComponent} from './house/app.house_component'
import { ContactComponent} from './contact/app.contact_component'



@Component({
	selector: 'app-body',
	templateUrl: 'views/main.html',
	directives: [NavBarComponent, BrotherComponent, RushComponent, BrothersComponent, CultureComponent, AboutUsComponent, HouseComponent, ContactComponent]
})

export class AppComponent{
}