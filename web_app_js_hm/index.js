function register(){
  const login = document.getElementById('login').value;
  const password = document.getElementById('password').value;

    if(!login || !password){
      alert('Введены не все данные');
      return;
    }
  alert("Вход выполнен");
  window.location.href = 'login.html';
}

function loginUser(){
  const login = document.getElementById('login').value;
  const password = document.getElementById('password').value;

    if(!login || !password){
      alert('Введены не все данные');
      return;
    }
  alert("Вход выполнен");
  window.location.href = 'portfolio.html';
};


function generatePortfolio() {
  const name = document.getElementById('name').value;
  const about = document.getElementById('about').value;
  const skills = document.getElementById('skills').value;
  const projects = document.getElementById('projects').value;

  const card = `
    <div class="portfolio-card">
      <h2>${name}</h2>
      <p>${about}</p>
      <div>${skills}</div>
      <div>${projects}</div>
    </div>
  `;

    document.getElementById('result').innerHTML = card;
}


console.log("JS работает");