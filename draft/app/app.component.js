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
var core_1 = require('@angular/core');
var app_brother_component_1 = require('./app.brother_component');
var app_navbar_component_1 = require('./app.navbar_component');
var BROTHERS = [
    { photo_file: 'img/head.jpg', name: 'Michael Traub', major: '8,18C', year: '2017' },
    { photo_file: 'img/head.jpg', name: 'SchMichael Traub', major: '8,18C', year: '2017' }
];
var AppComponent = (function () {
    function AppComponent() {
        this.brothers = BROTHERS;
        console.log("app-body component ctor");
    }
    AppComponent = __decorate([
        core_1.Component({
            selector: 'app-body',
            templateUrl: 'views/main.html',
            directives: [app_navbar_component_1.NavBarComponent, app_brother_component_1.BrotherComponent]
        }), 
        __metadata('design:paramtypes', [])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map