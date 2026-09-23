let nota = parseFloat(prompt("Digite uma nota: "))

if (nota < 5){
    window.alert("Reprovado")
}
else if (nota >= 5 && nota < 7){
    window.alert("Recuperação")
}
else{
    window.alert("Aprovado")
}