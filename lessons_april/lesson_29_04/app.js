// let colors = ['red', 'green', 'blue', 'purpol', 'orange'];
// let [first, second, ...third] = colors;

// console.log(first);
// console.log(second);
// console.log(third);


// let colors = ['red', 'green']
// let colors2 = ['blue', 'purpol', 'orange'];

// let color = [...colors, ...colors2];
// console.log(color);


////ОБЬЕКТЫ

// let person = {
//     name: 'Bob',
//     age: 18,
//     city: 'Kazan',
//     student: true
// }

// // console.log(person.name);
// // console.log(person.age);

// // let props = 'age';
// // console.log(person[props]);

// // person.race = 'Russian';
// // console.log(person.race); ///нежелательно



// ///МЕТОДЫ ОБЬЕКТА

// let calculate = {
//     value: 0,

//     add(n){
//         this.value += n;
//         return this;
//     },

//     substract(n){
//         this.value -= n;
//         return this;
//     },

//     reset(){
//         this.value = 0;
//         return this;
//     },

//     getResult(){
//         return this.value;
//     }
// }

// let result = calculate
//                 .add(10)
//                 .add(10)
//                 .substract(12)
//                 .getResult()

// console.log(result)


///ПЕРЕБОР ОБЬЕКТоВ


// let stud = {
//     name: "Damir",
//     math: 85,
//     physics: 90,
//     english: 70,
//     history: 78
// }

// for (const key in stud) {
//     if (!Object.hasOwn(stud, key)) continue;
    
//     const element = stud[key];
//     console.log(`${key} -> ${element}`)
    
// }

// let keys = Object.keys(stud);
// let values = Object.values(stud);
// let entries = Object.entries(stud);

// console.log(keys);
// console.log(values);
// console.log(entries);

// let entries = Object.entries(stud)
//     .filter(([key]) => key !== 'name')
//     .map(([, value]) => value);

// let average = entries.reduce((s, g) => s+g, 0) / entries.length;
// console.log(average)



// let stud = {
//     name: "Rustem",
//     surname: 'Ildarovich',
//     age: 21,
//     city: 'Kazan'
// }

// let {name: firstName, surname: secondName, age: userAge, score = 0} = stud;
// console.log(firstName);
// console.log(secondName);
// console.log(userAge);
// console.log(score)




// let base = {
//     theme: 'dark',
//     language: 'ru',

// }

// let expended = {
//     ...base,
//     fontSize: 15,
//     language: 'en',
// }

// console.log(expended);




// class Animal{
//     constructor(name, sound) {
//         this.name = name;
//         this.sound = sound;
//     }

//     speak(){ console.log(`${this.name} say: ${this.sound}`) }
//     eat(food){ console.log(`${this.name} eat ${food}`) }

// }

// class Dog extends Animal{
//     constructor(name, breed){
//         super(name, "Bark")
//        this.breed = breed;
//     }

//     fetch(item){console.log(`${this.name} take ${item}`)}
//     say(){console.log(`${this.name} -> ${this.sound}`) };
// }



// let rex = new Dog('Rex', 'puggy');
// rex.say();
// rex.eat('cheese');
// rex.fetch('stick');


