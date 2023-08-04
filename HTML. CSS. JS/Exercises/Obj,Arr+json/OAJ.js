let darthVader = {
    allegiance: 'Empire',
    weapon: 'Lightsabre',
    is_Sith: true
}

console.log(`Darth Vader's allegiance is to the ${darthVader['allegiance']}`);
console.log(`Darth Vader's weapon of choice is a ${darthVader['weapon']}`);
console.log(`Darth Vader is a sith? ${darthVader['is_Sith']}`);
console.log(`Darth Vader is a jedi? ${darthVader['is_Sith'] ? false : true}`);

let myArray = ['hello','everyone.'];

console.log(myArray.length);

for(let i = 0; i<3; i++){
    myArray.push(String(i));
}

console.log(myArray.length);
myArray.shift();

for (i of myArray){
    console.log(i);
}

