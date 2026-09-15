function maiorNumero(n1, n2){
    if (n1 > n2){
        alert(`${n1} é maior que ${n2}`)
    }
    else if (n1 < n2){
        alert(`${n2} é maior que ${n1}`)
    }
    else{
        alert("São iguais.")
    }
}

maiorNumero(3, 5)