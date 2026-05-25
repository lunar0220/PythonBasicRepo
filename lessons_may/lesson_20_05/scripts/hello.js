let name = 'Nastya'

function sayHello() {
    console.log(`Hello, ${name}`)
};

function sayGoodbye() {
    console.log(`Goodbye, ${name}`)
}


export {name, sayGoodbye, sayHello as default};