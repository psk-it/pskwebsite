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
var Brother = (function () {
    function Brother() {
    }
    return Brother;
}());
exports.Brother = Brother;
var BROTHERS = [
    { photo_file: 'img/head.jpg', name: 'Michael Traub', major: '8,18C', year: '2017' },
    { photo_file: 'img/head.jpg', name: 'SchMichael Traub', major: '8,18C', year: '2017' }
];
var BrotherComponent = (function () {
    function BrotherComponent() {
        this.brothers = BROTHERS;
        console.log(this.brothers);
    }
    __decorate([
        core_1.Input(), 
        __metadata('design:type', Brother)
    ], BrotherComponent.prototype, "brother", void 0);
    BrotherComponent = __decorate([
        core_1.Component({
            selector: 'brother-component',
            templateUrl: 'views/brother.html'
        }), 
        __metadata('design:paramtypes', [])
    ], BrotherComponent);
    return BrotherComponent;
}());
exports.BrotherComponent = BrotherComponent;
//# sourceMappingURL=app.brother_component.js.map