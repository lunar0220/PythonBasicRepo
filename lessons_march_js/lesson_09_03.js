// let a = 10; //поменять можно
// let b = 5;
// let sum = a*b;
// const c = 4; //поменять нельзя

// console.log(c); //underfind
// console.log(sum);

// let str = "3.14";
// let str2 = "3.14px";
// let num = parseInt(str);
// let num2 = parseInt;

// console.error(sum); //ошибку напишет
// console.warn(sum); //предупреждение
// console.table(sum); //вывод в виде таблицы


// console.log(x);
// let x = 5; //если запустить выведится ошибка


// let str = "123";
// let num = +str;
// if(isNaN(num)){
//     console.log("Это ошибка!");
// } else{
//     console.log("Успешно:", num);
// }

// let num = 5 + Number("5");
// console.log(num);



// let input = prompt("Введите строку:");

// let convertedNumber = Number(input);

// if(isNaN(convertedNumber)){
//     console.warn("Не число");
// } else{
//     console.log("Число:" + convertedNumber);
// }


// ++a инкремент
// --а дискремент

// console.log(++a);
// console.log(--a);
// console.log(a);


// let day = 5;
// switch(day){
//     case 1:
//     case 2:
//     case 5:
//         console.log("Значение найдено");
//         break;
//     default:
//         console.log("Не найдено");

// }





// let num = "100";
// let number = Number(num);

// if(isNaN(number)){
//     console.warn("Это не число");
// } else if(number % 2 === 0){
//     console.log("Число четное");
// } else{
//     console.log("Число нечетное");
// }  


let day = 21;
let month = 1;

let sign = ""

if ((month == 1 && day >= 20) || (month == 2 && day <= 18)) {
    sign = "Водолей";
} else if ((month == 2 && day >= 19) || (month == 3 && day <= 20)) {
    sign = "Рыбы";
} else if ((month == 3 && day >= 21) || (month == 4 && day <= 19)) {
    sign = "Овен";
} else if ((month == 4 && day >= 20) || (month == 5 && day <= 20)) {
    sign = "Телец";
} else if ((month == 5 && day >= 21) || (month == 6 && day <= 20)) {
    sign = "Близнецы";
} else if ((month == 6 && day >= 21) || (month == 7 && day <= 22)) {
    sign = "Рак";
} else if ((month == 7 && day >= 23) || (month == 8 && day <= 22)) {
    sign = "Лев";
} else if ((month == 8 && day >= 23) || (month == 9 && day <= 22)) {
    sign = "Дева";
} else if ((month == 9 && day >= 23) || (month == 10 && day <= 21)) {
    sign = "Весы";
} else if ((month == 10 && day >= 22) || (month == 11 && day <= 21)) {
    sign = "Скорпион";
} else if ((month == 11 && day >= 23) || (month == 12 && day <= 21)) {
    sign = "Стрелец";
} else if ((month == 12 && day >= 22) || (month == 1 && day <= 19)) {
    sign = "Козерог";
} else {
    sign = "Не верная дата"
}

console.log("Ваш знак зодиака: " + sign);
