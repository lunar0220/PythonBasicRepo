'use strict';
// let name = "Amina";
// console.log(name)


// const NAME = "Amina";
// console.log(name)

// if(true){
//     var n = 3;
// }
// console.log(n); ///лучше использовать let

// let userName = "Bob";
// let _userName = "Bob";
// let $userName = "Bob"; ///не желательно вообще 

// let bigNumber = 15_000_000;
// console.log(bigNumber)

// let number = -1/0;
// console.log(typeof number)

// console.log(10%3);

//СТРОКИ
// let student = "Дамир" + "Азатович";
// let greeting = `Hello to Academy TOP -> ${student}!`;
// console.log(greeting);
// console.log(greeting.length);
// console.log(greeting.toLocaleUpperCase());
// console.log(greeting.toLocaleLowerCase());
// console.log(greeting.includes("TOP"));
// console.log(greeting[1]);
// console.log(greeting.at(-10));
// console.log(greeting.slice(9, 16));
// console.log(greeting.replace("->", ":"));
// console.log(greeting.replaceAll("e", "!"));




// //BOOL
// if ("5" === 5){
//     console.log("equal");
// } ///строгое значение


// let num1 = prompt('Enter first number');
// if (num1 == 5){
//     console.log("equal to 5");
// }


// let n;
// console.log(n);
// console.log(typeof n);

// console.log("B" + "a"+ +"a" +"a"); //BaNaNa


// let result = +"42" + 18;
// console.log(result);

// let result2 = Number("2.5") + 18;
// console.log(result2);

// let result3 = Number("") + 18;
// console.log(result3);

// let result4 = Number(true) + 18;
// console.log(result4);

// let result5 = Boolean(0);
// console.log(result5);




// let userName = null;
// let displayName = userName ?? "Guest";
// console.log(displayName);


///ЦИКЛЫ

// for(let i = 1; i <= 5; i++){
//     console.log(`Step: ${i}`);

// }

// let i = 1;
// for(;;){
//     if (i <= 5){
//     console.log(`Step: ${i};`)
// } else {break};
// i++}


// let secret = 52;
// let guess = 0;
// let attempts = 0;

// while(guess !== secret){
//     attempts++;
//     guess = Math.floor(Math.random() * 100 ) + 1;
//     console.log(guess);
// }
// console.log(`You are win. All attempts => ${attempts}`)




// function sayHello(){
//     console.log("Hello, stud!"); 
// } ///function declaration -- отличается тем что имеет свойство хостинга

// sayHello()


// function sayHello(name){
//     return `Hello ${name}`; 
// }

// console.log(sayHello("Alic"))


// let sayHi = name => {
//     return `Hello ${name}`; 
// }
// console.log(sayHi("Nastya"));



// function User(name, age){
//     this.age = age;
//     this.name = name;
// }

// let user = new User("alina", 19);

// console.log(user);
// console.log(user.name);
// console.log(user.age);



// function appOperation(a, b, operation){
//     return operation(a, b);
// }


// const add = (a, b) => a + b;
// const substruct = (a, b) => a - b;
// const multipal = (a, b) => a * b;

// console.log(appOperation(10, 5, add));
// console.log(appOperation(10, 5, substruct));
// console.log(appOperation(10, 5, multipal));



// ///МАССИВЫ
// let fruits = ['apple', 'banana', 'orange', 'pear'];
// console.log(fruits.at(-3));
// console.log(fruits.length);

// console.log(fruits[fruits.length - 3]);

// ///МЕТОДЫ МАССИВОВ
// let fruits = ['apple', 'banana', 'orange', 'pear'];
// fruits.push("pinapple");
// fruits.unshift("straberry");
// fruits.pop();
// fruits.shift();
// console.log(fruits.indexOf("orange"));
// fruits.splice(2, 2, "juice")
// console.log(fruits);


///СОРТИРОВКА
let num = [1, 2, 5, 3, -4, -10, 9];
// num.sort((a, b) => a - b);
// console.log(num)


///Map

let newNums = num.map(n => n ** 2);
console.log(newNums);

let nEwNum = num.filter( n => n < 0);
console.log(nEwNum);

let neewNum = num.reduce((acc, n) => acc * n, 1);
console.log(neewNum);

let neewNums = num.some(n => n > 0);
console.log(neewNums);



