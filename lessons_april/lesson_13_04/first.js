// const parent = document.getElementById('parent');
// const child = document.getElementById('child');

// parent.addEventListener('click', () => console.log('Parent is done'));
// child.addEventListener('click', function(){console.log('Child is done')});





// const arr = ['parent', 'child', 'grandson'].map(id => document.getElementById(id));
// const output = document.getElementById('output');
// let capturing = false;
// let bubbling = true;

// function log(el, phase){
//     output.innerHTML += '^${phase}: ${el.id}<br>';
// }

// function setUp(){
//     arr.forEach(el =>{
//         el.removeElementListener('click', handler, true);
//         el.removeElementListener('click', handler, false);
//         if(capturing) el.removeElementListener('click', handler, true);
//         if(bubbling) el.removeElementListener('click', handler, false);
// });
// }

// function handler(e){
//     const p = e.evantPhase === 1 ? 'CAPTURIN' : e.evantPhase === 2 ? 'TARGET' : e.evantPhase === 3 ? 'BUBBLING':
//     log(this, p);
// }

// document.getElementById('turnOn').addEventListener('click', () =>{
//     capturing = !capturing;
//         setUp();
// })
// document.getElementById('turnOff').addEventListener('click', () =>{
//     bubbling = !bubbling;
//         setUp()
// })

// setUp();







// const user = {
//     name: 'Bob',
//     welcome() {
//         console.log(`Привет ${this.name}!`) ///this == user
//     }
// }

// user.welcome()



// const button = document.querySelector('#clicker');
// let countClicks = 0;

// button.addEventListener('click', () => {
//     countClicks++;
//     console.log('Кол-во кликов:', countClicks);
// })
