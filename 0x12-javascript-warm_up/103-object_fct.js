#!/usr/bin/node
const myObject = {
    type: 'object',
    value: 12
  };
console.log(myObject);

myObject.incr = function() {
    this.value++;
    } 
  
  /**
   * myObject.incr = () => this.value++;
   * 
   * the code above won't work bcs 'this' keyword only works inside regular function ,
   * but in arrow func will refer to the global window object or node object
   */
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
