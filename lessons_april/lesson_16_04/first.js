// let selector = document.querySelector('select')

// let newOptions = document.createElement('option');
// selector.appendChild(newOptions);
// newOptions.text = "Москва";

// let secondOp = document.createElement('option');
// selector.appendChild(secondOp);
// secondOp.text = "Казань";

// let thirdOp = document.createElement('option');
// selector.appendChild(thirdOp);
// thirdOp.text = "Уфа";

let listener = document.querySelector('button');

listener.addEventListener('click', function(event){
    event.preventDefault();
    console.log('Действие отмененно');

    let inputsFind = document.querySelectorAll("input");

    for(let inputs of inputsFind){
        if(inputs.value.length < 10){
            console.log("Слишком коротко")
        }

    let resetNew = document.querySelectorAll("submit");
    resetNew.type = 'reset';
}})





////аснхронность
// console.log('1');
// setTimeout(() =>{ ///макрозадача
//     console.log('2')
// })
// console.log('3') ///выводится 132

// .then()
// queueMicrotask()
// MutationObserver ///микро задачи



console.log('1');
setTimeout(() =>{
    console.log('2')
})

Promise.resolve().then(() => (
    console.log("3")
))

console.log('4') ///1432



const myPromis = new Promise((resolve, reject) => {
    const success = true;

    if(success){
        console.log('1')
        resolve("Успех")
    } else{
        console.log('2')
        resolve("Ошибка")
    }
})


loadData().then(() => {
    ///что-то тут 
    throw new Error("ОШИБКА!!!")

}).catch(error => {
    console.error("Ошибка:", error)
});
