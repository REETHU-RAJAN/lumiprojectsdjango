// interface cake{
//     name:string,
//     price:number,
//     shape:string
// }
// var cobj:cake={
//     name:"blueberry",
//     price:67,
//     shape:"round"
// }
var swnift = /** @class */ (function () {
    function swnift() {
    }
    swnift.prototype.drive = function () {
        console.log("drive");
    };
    swnift.prototype.acceralte = function () {
        console.log("accel");
    };
    swnift.prototype.brks = function () {
        console.log("brks");
    };
    return swnift;
}());
