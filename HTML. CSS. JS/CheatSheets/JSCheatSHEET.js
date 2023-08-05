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

//object creation and handling

let obj1 = {
    name: 'name1',
    age: 0,
    job: 'be object'
}
let obj2 = new Object(); 
obj2.name = 'name2';
obj2.age = 0;
obj2["job"] = 'also be object';

console.log(obj1.name); //outputs obj1's name
console.log(obj2['name']); //outputs obj2's name

for(let key in obj2){ //loops through an objects keys
    console.log(`${key}: ${obj2[key]}`)
}

//Array creation and handling

let a = Array(); //empty array
let b = Array(10); //Array with 10 empty spaces
let c = ['Hello','World']; //Creates an array with elements Hello and World

c[0] = 'Hi'; //changes the item in position 0 to Hi

for(let index of c){ //loops through the values instead of positions
    console.log(index);
}
let index = 0;
c.sort(); //sorts the array
c.reverse(); //reverses the array
c.join(' '); //join the items of the array into a string
c.push(str1); //appends value to the end of the array
c.pop(); //takes off a value from  the end
c.unshift(str1); //append element to beginning
c.shift(); //remove from beginning of array
c.indexOf(str1); //find the first occurence position of str1
c.splice(index,1); //removes items at the index position up to a given number of items

//JSON
//Language indepentent data interchange format
//means it's used to tranfer data

//keys must be string
//values must be:
//string
//int
//bool
//object
//array
//null

let jsonObj = {
    'key1':'val1',
    'key2':'vaL2'
}
// this 
let objString = '{"name": "Athena"}'; //JSON string
let obj3 = JSON.parse(objString); //converts JSON string into object

let jsonStr = JSON.stringify(); //converts object into JSON string


//functions
function func1(num1,num2){ //creates function
    return(num1+num2) 
}

func1(5,10); //runs function

//function expressions:
let myfunc = function(num1,num2){
    console.log(num1+num2);
}
//can be used as a variable.
myfunc(4,5); //9

//arrow functions:
const arrfunc = (num1,num2)=>{
    console.log(num1+num2);
}
//arrow function with return
let arrfunc2 = (num1,num2) => (num1+num2)

//scopes
//block scopes
////let
////const
//function scopes
////var

//Selectors
let resetBtn = document.querySelector("#resetbtn"); //assigns button in html a variable
let txtbox = document.querySelector("#inputbx");
let maindiv = document.querySelector("#maindiv");
//Functionality
let val1 = txtbox.value; //take contents of textbox
let div1 = document.createElement("div"); //create a div
let val2 = document.createTextNode(val1); //create a text node with text

div1.appendChild(val2); //add textnode to the JS div
maindiv.appendChild(div1); //add the JS div to the html div


//Event Listeners
resetBtn.addEventListener('click',func1) //when button is clicked, func1 runs