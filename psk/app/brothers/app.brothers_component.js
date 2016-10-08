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
var readStringFromFileAtPath = function (pathOfFileToReadFrom) {
    var request = new XMLHttpRequest();
    request.open("GET", pathOfFileToReadFrom, false);
    request.send(null);
    var returnValue = request.responseText;
    return returnValue;
};
var bros_json = readStringFromFileAtPath("data/brothers.json");
var BROTHERS = JSON.parse(bros_json);
var SENIORS = [];
var JUNIORS = [];
var SOPHOMORES = [];
var FRESHMEN = [];
for (var i = 0; i < BROTHERS.length; i++) {
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
var BrothersComponent = (function () {
    function BrothersComponent() {
        this.brothers = BROTHERS;
        this.seniors = SENIORS;
        this.juniors = JUNIORS;
        this.sophomores = SOPHOMORES;
        this.freshmen = FRESHMEN;
    }
    BrothersComponent = __decorate([
        core_1.Component({
            selector: 'brothers',
            templateUrl: 'views/brothers.html',
            directives: [app_brother_component_1.BrotherComponent]
        }), 
        __metadata('design:paramtypes', [])
    ], BrothersComponent);
    return BrothersComponent;
}());
exports.BrothersComponent = BrothersComponent;
//# sourceMappingURL=app.brothers_component.js.map