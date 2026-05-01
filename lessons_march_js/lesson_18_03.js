///рекурсия

// function countdown(n){
//     if(n<=0){
//         console.log("End");
//         return;
//     }
//     console.log(n);
//     countdown(n-1);
// }

// countdown(5);



// function pow(base, exp){
//     if(exp === 0 ) return 1;
//     return base * pow(base, exp-1);
// }
// console.log(pow(2, 16));



// function fac2(n){
//     if(n === 0) return 1;
//     return n * fac2(n-1);
// }

// console.log(fac2(5));



// function fib(n){
//     if(n <= 1) return 1;
//     if(n === 2) return 1;
//     return fib(n-1) + fib(n-2);
// }

// console.log(fib(5));




// function createUser(name){
//     let password = "qwerty";
//     return {
//         getName: function(){
//             return name;
//         }, 
//         checkPassword: function(input){
//             return input === password;
//         }
//     };
// }

// const user = createUser("Bob");
// console.log(user.getName());
// console.log(user.checkPassword("123"));
// console.log(user.password);



///задачки

// function multiply(a){
//     return function(x){
//         return a * x;
//     }
// } 

// const result = multiply(5);
// console.log(result(3));



// function memory(fn){
//     const cash = {};

//     return function(arg){
//         if(cash[arg] !== undefined){
//             console.log("Fetch from cash: " + arg);
//             return cash[arg];
//         }

//         const result = fn(arg);
//         cash[arg] = result;
//         console.log("computing process result: " + arg);
//         return arg;
//     }
// }

// function fac(n){
//     if(n === 0) return 1;
//     return n * fac(n-1);
// }

// const memroraized = memory(fac);
// console.log(memroraized(5));
// console.log(memroraized(5));



// function sumDigits(n){
//     if(n<10) return n;
//     let x = n%10;
//     if(x  == 1 || x == 2 || x == 3 || x == 5 || x == 7) return x = x;
//     else{
//         x = 0;
//     }
//     return x + sumDigits(Math.floor(x / 10));
// }

function sumDigits(n){
    if (n < 10) {
        return (n === 2 || n === 3 || n === 5 || n === 7) ? n : 0;
    }

    let x = n % 10;

    if (x !== 2 && x !== 3 && x !== 5 && x !== 7) {
        x = 0;
    }

}

function cashedsumDigits(){
    const cash = {};
        return function(arg){
        if(cash[arg] !== undefined){
            console.log("Fetch from cash: " + arg);
            return cash[arg];
        }

        console.log("computing process result: " + arg);
        const result = sumDigits(arg);
        cash[arg] = result;

        return result;
    }
}

const cashed = cashedsumDigits();

console.log(cashed(2893));
console.log(cashed(2893));


///431 = 4