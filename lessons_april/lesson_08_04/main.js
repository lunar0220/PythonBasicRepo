// const btn = document.createElement('button');
// btn.textContent = 'YES';
// document.body.appendChild(btn);


// const parent = document.createElement('List');
// const newItem = document.createElement('Li'); ///=0
// /// 1 2 3 4
// parent.insertBefore(newItem, parent.firstChild);
// ///вставит в начало, а не в конец как appendChil
// ///0 1 2 3 4


// const div = document.createElement('div');
// document.body.appendChild(btn);
// div.style.color = 'red';

// const newParent = document.createElement('id');
// const child = newParent.firstChild;
// newParent.removeChild(child);






const input = document.getElementById('task-input');
const button = document.getElementById('input-btn');
const taskList = document.getElementById('task-list');


button.onclick = function(){
    const text = input.value.trim();

    const li = document.createElement('li');
    li.textContent = text;

    taskList.appendChild(li);
    input.value = '';
}


let deleteText = document.createElement('button');

document.body.appendChild(deleteText);
deleteText.textContent = 'Удалить элемент';

deleteText.onclick = function(){
let allLi = document.querySelectorAll('li');
if(allLi.length > 0){
    allLi[allLi.length-1].remove();
}}


button.onclick()

button.addEventListener('click'), function(){console.log('Клик')} /// как onclickб можно добавлять несколько и выведется два значения


/// div id='parent' => button id='child'
const parent = document.getElementById('parent');
const child = document.getElementById('child');

parent.addEventListener('clic', function(){console.log('Родитель')});
child.addEventListener('clic', function(){console.log('Ребенок')});