'strict';

let age = parseInt(prompt("give me an age"));

if(18 <= age & age <= 65){
    console.log(age);
}else{
    console.log('either child or elderly');
}

let bool1 = (age >= 50)?'Over':'Under';


const d = new Date();
let day = d.getDay();

switch(day){
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('Monday to Friday');
        break;
    case 6:
        console.log('Saturday');
        break;
    case 0:
        console.log('Sunday');
        break;
    default:
        console.log('No clue how you got this repsonse');
}