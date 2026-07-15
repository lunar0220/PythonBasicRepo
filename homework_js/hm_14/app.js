function check() {
    let a = Number(document.getElementById("a1").value);
    let b = Number(document.getElementById("b1").value);
    let result = Number(document.getElementById("result1").value);

    document.getElementById("result1").disabled = true;

    let message = document.getElementById("message");

    if (result === a + b) {
        message.innerHTML = "Верно!";
        message.style.color = "green";
    } else {
        message.innerHTML = "Неверно!";
        message.style.color = "red";
    }
}