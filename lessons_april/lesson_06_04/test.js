

// let inputs = document.querySelectorAll('input');
// for (let item of inputs) {
//     if(!item.value) {
//         console.log(item);
//     }
// }



// let createButton = document.createElement('button');

// document.body.appendChild(createButton);
// createButton.textContent = 'Удалить';

// createButton.onclick = function(){
//     let tableRemove = document.querySelectorAll('td');
//     let second = tableRemove[1]

//         if(second){
//             second.remove();
//         }
//     }




let createButton = document.createElement('button');

document.body.appendChild(createButton);
createButton.textContent = 'Добавить данные';

createButton.onclick = function(){
    let findH3 = document.querySelectorAll('h3');
    for(let h3 of findH3){
        if(h3.id){
            console.log(h3)
        }
    }

    let userName = document.getElementById('username');
    userName.textContent = "Иванов Иван Иванович";

    let yearN = document.getElementById('year');
    yearN.textContent = "2000";

    let firstStr = document.getElementById('first');
    firstStr.textContent = "Программирование";

    let secondStr = document.getElementById('second');
    secondStr.textContent = "Дизайн";
}
