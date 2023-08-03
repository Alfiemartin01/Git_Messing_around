"use strict"; //enables strict mode

// Console Outputs
console.log('This is a console log');
console.info('This is a console info');
console.warn('This is a console warning');
console.error('This is a console error');

let Var1 = 100;
const Const1 = 5;
var car= {type:"Audi", model:"A5"}; //this is an example of an object
console.log("this is a %c a message with some CSS."+Const1,"color: yellow; font-style: italic; background-color: blue;padding: 2px");
console.log(`This allows us to implement vars in strings like ${Var1}`);

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
let str1 = `${Var1 + Const1}`;


str1.indexOf('1'); //finds position of first occurence of 1
str1.charAt(1); //returns value in position 1
str1.toUpperCase(); //Converts string to uppercase 
eval('5*8'); //evaluates the maths of a string 

for(let i = 0; i <= 9; i+=1){ //loops 10 times
    console.log(i);
}

let i = 0;
while(i != 10){ //while loop
    console.log(i);
    i+=1;
    if (i>=5){
        break; //breaks out of loop
    }
}

do { //do loop
    console.log(i);
    i-=1;
} while(i != 0)

//Conditionals
if(Var1==Const1){
    
}else if(Var1!=Const1){

}else{    
}

switch(Const1){
    case 2:
    case 3:
        console.log(`Const = 2 or 3`);
        break;
    case 5:
        console.log(`Const = 5`);
        break;
    default:
        console.log('some other number')
}

//False Elements:
//false
//0
//'' or "" 
//undefined
//null
//NaN

//True Elements:
//'0' - (String containing single digit 0 )
//'false' - (String containing text - 'false')
//[] - (An empty array)
//{} - (An empty object)
//function(){}

console.log(Var1 == Const1); //Checks values
console.log(Var1 === Const1); //Check type AND value

let age = (Const1 == 5)? 10 : 20; //10 if true, 20 if false
//User inputs:
let inp = parseInt(prompt("Enter value"));

// && AND operator
// || OR 
// ^  XOR bitwise operator


