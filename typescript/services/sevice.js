"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ProductServices = void 0;
var ProductServices = /** @class */ (function () {
    function ProductServices() {
    }
    ProductServices.prototype.addproduct = function () {
        console.log("api call for adding aproduct");
    };
    ProductServices.prototype.listall = function () {
        console.log("api call for list all products");
    };
    ProductServices.prototype.editproduct = function () {
        console.log("api call for update a product");
    };
    return ProductServices;
}());
exports.ProductServices = ProductServices;
