// Validar data

// var data = /^[0[1-9]|1[0-9]|2[0-9]|3[0-1]]+/[0[1-9]|1[0-2]]+/{4}$/

// Validar cpf

// var email = /^[a-zA-Z0-9._]+@[a-zA-z0-9]+\.[a-zA-Z]{2,}$/

const inputs = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.span-required');
const email = /^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
function emailValidate(){
    if (email.test(inputs[0].value)){
        removeError(0)
    }
    else{
        setError(0);
    }
}
function setError(index){
    spans[index].style.display = 'block';
    spans[index].style.color = 'red';
}

function removeError(index){
    spans[index].style.display = 'none';
}

var modal = document.getElementById("modal");
var abrir = document.getElementById("abrir");
var fechar = document.getElementById("fechar");

abrir.addEventListener("click", function(){
    modal.style.display = "block";
});

fechar.addEventListener("click", function(){
    modal.style.display = "none";
});