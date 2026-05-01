// const color = {
//     blue: color,
// }
// ///проверяем есть ли ключ в объекте
// console.log("blue" in color);

// let arr = [1, 2, 3];
// console.log(arr.includes(2));

// let obj = {'3':4};
// let arr2 = [1, 2, obj];
// console.log(arr2.includes(obj));

// arr.push(arr);
// console.log(arr);




// 'use strict';
// let cabinet = {
//     topbox: 'Паспорт',
// }

// Object.defineProperty(cabinet, 'topbox', {
//     writable: true,
// })

// cabinet.topbox = ['Диплом']; ///в данном случае мы перезаписываем строку на массив
// cabinet.topbox.push('СНИЛС'); ///в данном случае мы добавляем элемент в массив, который уже есть в объекте
// console.log(cabinet);

// Object.defineProperty(cabinet, 'topbox', {
//     writable: false,
// })

// cabinet.topbox.push('Сведетельство');
// console.log(cabinet);


// Object.freeze(cabinet);
// cabinet.topbox.push('Сведетельство');
// console.log(cabinet);


// let numbers = [1, 2, 3];
// let numbers2 = [4, 5, 6];

// console.log(numbers+numbers2);
// let res = [...numbers, ...numbers2];
// console.log(res);





// const paketMom = {
//     fruit: "apple",
//     milk: true,
// }

// const paketDad = {
//     fruit: "orange",
//     candy: true,
// }

// allPaket = {...paketMom, ...paketDad}; ///второй обьект имеет приоритет и перезаписывает значение ключа fruit, который есть в обоих обьектах
// console.log(allPaket);






// function sumNumbers(first, second){
//     let result = 0;

//     for(let arg of arguments){
//         result += arg;
//     }

//     return result;
// }

// console.log(sumNumbers(1, 2, 3, 4));

// function mySum(...arg){
//     return arg.reduce((sum, val) => sum + val, 0)
// }

// console.log(mySum(1, 2, 3, 10))



// const market = {
//     type: ['food', 'drinks'],
//     product: {
//         price: 100,
//         wieght: 'lite'
//     }
// }

// Object.freeze(market);
// delete market.type[1];
// delete market.type[0];
// market.type = "arr";
// market.product.price = 200;
// console.log(market);



const grades = {
    Anna: 85,
    Boris: 70,
    Clara: 90,
    Bob: 1
};

function allGreatStud() {
    for (let grade in grades){
        if (grades[grade] > 75){
            console.log(grade + ': ' + grades[grade]);
}}}

allGreatStud();


const test = {a:1, b:undefined, c:null};
function hasKey(obj, key){
    return key in obj;
}

console.log(hasKey(test, "d"));


function hasVal(obj, val){
    for (let key in obj){
        if(obj[key] == val){
            return true;
        }
    }
    return false;
}

console.log(hasVal(test, "2"));