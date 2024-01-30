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

interface car{
    drive()
    acceralte()
    brks()
}
interface ev{
    electric()
}

class swnmift implements car,ev{
    drive(){
        console.log("drive");
        
    }
    acceralte(){
        console.log("accel");

        
    }
    brks(){
        console.log("brks");
        
    }
    electric() {
        console.log("elec");
        
        
    }
}