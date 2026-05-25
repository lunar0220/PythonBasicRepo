import React from "react";
import ReactDOM, { createRoot } from 'react-dom/client';

// const rootNode = ReactDOM.createRoot(document.getElementById('app'));

// const element = <h1>hello</h1>
// rootNode.render(element);

// const stud = {
//     id: 1,
//     age: 21,
//     firstName: "Anastasia",
//     lastName: "Vlasova",
//     getFullName: function () {
//         return `${this.firstName} ${this.lastName}`;
//     }
// };

// createRoot(document.getElementById('app')).render(
//     // <h2>15 + 8 = {15 + 8}</h2>
//     <div id={stud.id}>
//         <p>Полное имя: {stud.getFullName()}</p> 
//         <p>Возраст: {stud.age}</p>
//         <p>Индефикатор: {stud.id}</p>
//         <p>Дата формирование: {new Data().toLocalTimeString()}</p>
//     </div>
// );

const langs = ["Python", "Goland", "C#", "1C"];

const styleObj = {
    color: "red",
    fontSize: "24px",
    "background-color": "black",
    "border-radius": "10px",
    margin: "3px",
    "border-radius": "8px",
    padding: "10px",
    "box-shadow": "0 0 10px rgba(0, 0, 0, 0.5)"
}

createRoot(document.getElementById('app')).render(
    <div>
    <h1 style={styleObj}>Hello, world!</h1>
        <ul>
            {langs.map((lang, index) => (<li key={index}>{lang}</li>))};
        </ul>
    </div>
)




