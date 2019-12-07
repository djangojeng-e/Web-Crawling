console.log(2 + 3);

// Data types 

// 1. Numbers 
// 2. Floats
// 3. Booleans 
// 4. String ( all have index) 
// 5. Object (Dictionaries, Arrays)
// 6. Null and Undefined 

// Variables 

var firstName = "John";
console.log(firstName);

// firstName = "Paul"; // Re-assingn the value of firstName 

// Naming convention for variables 
// Javascript follows lowerCamelCase 
// E.g. Ruby : snake_case 


// Concatenate - putting the elements together 

var lastName = "Lenon";
console.log(lastName);

var fullName = firstName + " " + lastName; 
console.log(fullname);







// Conditions 

// if, else 

var weather = "sunny"; 


if(weather === "rainy"){
    console.log("Take your umbrella!")
  // execute the code in here 
}else if(weather === "stormy"){
  console.log("Stay at home");
}else{
  console.log("No umbrella needed today!!!");
}

var ben = "Ben";
var bob = "Bob";
var john = "John"; 

var bNames =""; 


if (ben[0] === "B"){
  bNames = bNames + ben;
 
}

if (bob[0] === "B"){
  bNames = bNames + bob;
}

if (john[0] === "B"){
  bNames = bNames + "" + john; 
}

console.log(bNames);






var names = ["Ben", "Bob", "John"];

var bNames = "";

for (var i = 0; i < names.length; i+=1) {
  if ( names[i][0] === "B"){
    bNames = bNames + " " + names[i]
  }
}

console.log(bNames.trim());







































