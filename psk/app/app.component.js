"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
const core_1 = require('@angular/core');
const app_brother_component_1 = require('./brothers/app.brother_component');
const app_navbar_component_1 = require('./navbar/app.navbar_component');
const app_rush_component_1 = require('./rush/app.rush_component');
const app_brothers_component_1 = require('./brothers/app.brothers_component');
const app_culture_component_1 = require('./culture/app.culture_component');
const app_aboutus_component_1 = require('./aboutus/app.aboutus_component');
const app_house_component_1 = require('./house/app.house_component');
const app_contact_component_1 = require('./contact/app.contact_component');
let AppComponent = class AppComponent {
};
AppComponent = __decorate([
    core_1.Component({
        selector: 'app-body',
        templateUrl: 'views/main.html',
        directives: [app_navbar_component_1.NavBarComponent, app_brother_component_1.BrotherComponent, app_rush_component_1.RushComponent, app_brothers_component_1.BrothersComponent, app_culture_component_1.CultureComponent, app_aboutus_component_1.AboutUsComponent, app_house_component_1.HouseComponent, app_contact_component_1.ContactComponent]
    }), 
    __metadata('design:paramtypes', [])
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map