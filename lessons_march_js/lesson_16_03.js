// function grett(callback){ 
//     callback();
// }
// grett(() => {
//     console.log("Всем привет!");
// })


// setTimeout(() => {
//     console.log("Ждем одну секунду")
// }, 1000);

// console.log("Этот код ждать не будет");


// function fetchDataFunc(callback){
//     setTimeout(() => {
//         console.log("Данные долго загружаются");
//         callback("Вот ваши данные");
//     }, 2000)
// }
// function display(data){
//     console.log(data);
// }

// fetchDataFunc(display);



// function calc(a, b, oper){
//     return oper(a, b);
// }

// function add(x, y){
//     return x+y;
// }

// function mult(x, y){
//     return x*y;
// }

// console.log(calc(5, 3, add));
// console.log(calc(5, 3, mult));


// let name = "Alex";

// function grett(callback){ 
//     let name = "Bob";
//     return callback(name);
// }
// grett((name) => {
//     console.log(name);
// })




// function calculate(x=0, y=0, z=0, oper){
//     return oper(x, y, z);
// }

// function add(x, y, z) {
//     return x+y+z;
// }

// function mult(x, y, z) {
//     return x*y*z;
// }

// function calc(x, y, z) {
//     return x-y-z;
// }

// console.log(calculate(5, 3, 2, add));
// console.log(calculate(5, 3, 2, mult));
// console.log(calculate(5, 3, 2, calc));



///РЕКУРСИИ

// (function(){
//     console.log("я выполнюсь сразу");
// })();


// function countdown(n){
//     if(n<=0){
//         console.log("Я скащала стартуем");
//         return;
//     }
//     console.log(n);
//     countdown(n-1);
// }
// countdown(10);

function counter(){
    let count = 0;
    return function(){
        count++;
        return count;
    }
}

const count = counter();
console.log(count());
console.log(count());
console.log(count());



////КЕШИРОВАНИЕ

function memory(fn) {
    const cash = {};
    return function(arg){
        if(cash[arg] !== underfind){
            console.log("Fetch from cash: " + cash[arg])
        }
    }
}