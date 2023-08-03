// Console Outputs
console.log('This is a console log');
console.info('This is a console info');
console.warn('This is a console warning');
console.error('This is a console error');

let Var1 = 100;
const Const1 = 5;
var car= {type:"Audi", model:"A5"}; //this is an example of an object
console.log("this is a %c a message with some CSS."+Const1,"color: yellow; font-style: italic; background-color: blue;padding: 2px");
console.log(`This allows us to implement vars in strings like ${Var1}`)

//Primitive data types - Immutable, fixed length, quick to look up
////Boolean
////Number
////BigInt
////String
////Undefined - not been assigned a value
////Null - value that can be assigned to rep objects that dont exist
////Symbol
//Object - collections of properties, mutable

typeof(Var1); //returns the var type

//Number types:
//Number.NaN
//Number.Infinity
//Number.POSITIVE_INFINITY
//Number.NEGATIVE_INFINITY	
//Number.MAX_VALUE	
//Number.MIN_VALUE	

//Do maths before outputting results.
let str1 = `${Var1 + Const1}`

console.log(Var1 == Const1); //Checks values
console.log(Var1 === Const1); //Check type AND value

str1.indexOf('1') //finds position of first occurence of 1
str1.charAt(1) //returns value in position 1
str1.toUpperCase() //Converts string to uppercase 
eval('5*8') //evaluates the maths of a string 

