// function MyFunc(){
//     let text = "Hello";
//     console.log(text);
// }
// console.log(text) //ошибки не будет

// function MyFunc(){
//     const text = "Hello";
//     console.log(text);
// }
// console.log(text); //ошибка


// while(true){
//     let x = 10;
//     console.log(x);
// }

// console.log(x) //ошибка



// let n = "5";
// n = Number(n);
// if(!isNaN(n) && n>=0){
//     let sum = 0;
//     for(let i = 1; i <= n; i++){
//         sum = sum + i;
//     }
//     console.log('Сумма числа от 1 до ' + n+ ':' + sum);
// }


// const hours = 24;
// const duration = 1.5;
// const travel = 1;

// let days = 5;
// let n = [3, 2, 4, 2, 1];

// let totalBusy = 0;
// let totalFree = 0;

// for (let i = 1; i <= n.length; i++) {
//     if (n[i] < 0 || n[i] > 5) {
//         console.log("Неверное кол-во пар");
//     } else {
//         let totalClassTime = n[i] * duration;
//         let totalTravelTime = travel * 2;

//         let busy = totalClassTime + totalTravelTime;

//         let availebleTimeToSleep = hours - busy;
//         console.log("Оставшееся время:", availebleTimeToSleep);
//     }
// }






// function sum(a=0, b=0) {
//     return a + b;
// }

// console.log(sum(5));

// const sum = (a, b) => a+b;
// console.log(sum(3, 4));


// function showMyName() {
//     console.log(this.name); //this - это объект, который вызывает функцию
// }

// const person = {
//     name: "Bob",
//     showName: showMyName
// };
// person.showName();


// function findMax(a, b) {
//     if (a > b) {
//         return a;
//     }
//     else if (a == b) {
//         return "Числа равны";
//     }
//     else {
//         return b;
//     }
// } 
// console.log(findMax(3, 5))



// function findChet(a){
//     if (a % 2 === 0){
//         return "Число четное";
//     }
//     else {
//         return "Число нечетное"
//     }
// }
// console.log(findChet(2819))


let first = 1;
let second = 1;
let sum = 0;
function findNum(n){
    for(let i = 3; i<=n; i++){
        sum = first + second;
        first = second;
        second = sum;
    }
            return sum;

}
console.log(findNum(5))