
function car(x){
  this.x=x;
}

//add methods using prototype
car.prototype.printx = function(){
   console.trace();
   
}
car.prototype = {
  get:function(){
   console.log("get");
  }
}

module.exports = car;

