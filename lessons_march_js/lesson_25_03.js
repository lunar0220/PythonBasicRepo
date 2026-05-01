// let str = "hello";
// let newStr =  str.toUpperCase();
// console.log(newStr);




// let string = 'Пример строки';
// let string2 = 'Это тоже строка';
// let nameA = 'Мир';
// let string3 = `Привет, ${nameA}`;

// console.log(string);
// console.log(string2);
// console.log(string3);


// let text = 'I have 2 apples and 10 bananas.';
// let numbers = text.match(/\d+/g);
// // console.log(numbers);
// let sum = numbers.reduce((acc, val) => acc + Number(val), 0);
// console.log(sum);


// function eurDate(amDate){
//     let splDate = amDate.split("/");

//     let month = splDate[0];
//     let day = splDate[1];
//     let year = splDate[2];

//     return `${day}/${month}/${year}`;
// }


// console.log(eurDate("12/25/2025"));


// let text = 'Apple and Cherry is amazing Fruits';
// let wordsStarWithA = text.match(/\b[Aa][a-z]+\b/g);
// console.log(wordsStarWithA)

// let text = '+7 (800) 401-54-73';
// let onlyLetters = text.replace(/\d+/g, "")
// console.log(onlyLetters)


// let human ={
//     name:"Bob"
// }

// // Object.freeze(human);
// human.name = "alice";
// human.lastName = "Ivanova";
// human.work = "True";
// delete human.work;

// console.log(human);

// let car ={
//     brande:"Mercedec"
// }

// let local_car = Object.assign({}, car);
// local_car.brande = "Lada";
// console.log(car, local_car);

// const students = [
//     {
//         name: 'Alice'
//     },
//     {
//         name: 'Not Alice' 
//     }
// ]

// console.log(students[1].name)


// const carNew = {
//     name:'Mercedec',
//     coordinates: {
//         lat: 55,
//         lon: 50
//     }
// };
// console.log(carNew.coordinates.lon);

let human = {
    name: 'Коля',
    welcome: function(){console.log('Привет')},
    goodbye: () => console.log('Пока')
};
human.welcome();
human.goodbye();

