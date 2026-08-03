class Cores:
    fundo = "#a4a5a8"
    cartao = "#c0c0c2"
    texto = "#000000"
    texto_secundario = "#000d42"
    placeholder = "#808080"
    borda = "#000000"
    primaria = "#001877"
    primaria_hover = "#001258"
    primaria_pressed = "#000B38"

estilo = f"""
QWidget#Janela{{
    background-color: {Cores.fundo}
     
}}
QWidget#TelaPrincipal{{
    background-color: {Cores.fundo}
}}
"""