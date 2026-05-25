// const myPromise = new Promise(function () {
//     console.log("Выполняется операция");
// });


// const myPromise3 = new Promise(function () {
//     console.log("{myPromise3} Асинхранная операция 3");
//     setTimeout(() => {
//         console.log('Завершение асинхранности');
//     }, 3000);
// });

// const myPromise2 = new Promise(function () {
//     console.log("{myPromise2} Асинхранная операция 2");
//     setTimeout(() => {
//         console.log('Завершение асинхранности');
//     }, 2000);
// });

// const myPromise1 = new Promise(function () {
//     console.log("{myPromise1} Асинхранная операция 1");
//     setTimeout(() => {
//         console.log('Завершение асинхранности');
//     }, 1000);
// });


// const myPromise = new Promise(function (resolve) {
//     console.log("Асинхранная операция");
//     resolve(`all ok... it's work`);
// });

// myPromise.then(function (value) {
//     console.log(`Из нашего промиса получили: ${value}`)
// });




// const num1 = 25;
// const num2 = 50;

// const myPromise = new Promise(function () {
//     console.log("Async function");
//     const result = num1 + num2;
//     console.log(`Result: ${result}`)
// })

// myPromise.then();

// function multiply(x, y, func){
//     if(func === undefined) func = function(value){
//         console.log(`function result: ${value}`)
//     };
//     return new Promise(function(resolve){
//         const result = x * y;
//         resolve(result);
//     }).then(func);
// }
// multiply(2, 8)
// multiply(25, 4, function(value){
//     console.log(`Результат функции: ${value}`)
// })



// const myPromise = new Promise(function (resolve, reject) {
//     console.log(`Async function`)
//     reject(`Value error: invalid value...`);
// })

// myPromise.catch(function (error) {
//     console.log(error);
// })


// const myPromise = new Promise(function (resolve) {
//     console.log(`Async function`)
//     getErrorWorkFunc();
//     resolve(`Hey hey, all work.`);
// })

// myPromise.catch(function (error) {
//     console.log(error);
// })


function genNumber(str){
    return new Promise((resolve, reject) => {
        const parsStr = parseInt(str);
        if (isNaN(parsStr)) reject(`Not a number...`);
        else resolve(parsStr);
        });
};

function print(str) { 
    genNumber(str)
    .then(value => {
        console.log(value);
        return "Its 'then' from 'getNumber";
    })
    .catch(error => {
        console.log(error);
        return "Its 'catch' from 'getNumber'";
    })
    .finally(() => {
        console.log('end promise');
        return "Its 'finally'";
    })
    .then(message => console.log(message));
}

print('863')