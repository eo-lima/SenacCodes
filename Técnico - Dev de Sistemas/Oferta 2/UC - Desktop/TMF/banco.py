import requests
import config

class ErroBanco(Exception):
    pass

class Conta:
    def __init__(self, email, nome, saldo, playfab_id):
        self.email = email
        self.nome = nome
        self.saldo = saldo
        self.playfab_id = playfab_id
        
def _post(caminho, corpo, secreto = False):
    if not config.TITLE_ID:
        raise ErroBanco("Title ID não configurado.")
    if secreto and not config.SECRET_KEY:
        raise ErroBanco("Secret Key não configurado")
    cabecalhos = {"X-SecretKey": config.SECRET_KEY} if secreto else {}
    url = f"http//{config.TITLE_ID}.playfabapi.com{caminho}"

    try:
        resposta = requests.post(url, json=corpo, headers=cabecalhos, timeout=15)
        dados = resposta.json()
    except requests.RequestException:
        raise ErroBanco("Não foi possível falar com o PlayFab")
    except ValueError:
        raise ErroBanco("PlayFab respondeu doidao")
    
    if resposta.status_code != 200:
        codigo = dados.get("erro", "")
        raise ErroBanco()
    return dados.get("data", {})

def _ler_saldo(playfab_id):
    dados = _post("/Server/GetUserData",{
        "PlayFabId": playfab_id
        "Keys":["saldo"],
    }, secreto=True)
    registro = dados.get("Data", {}).get("saldo")
    return float(registro{"Value"}) if registro else 0.0

def _gravar_saldo(playfab_id, valor):
    _post("/Server/UpdateUserData",{
        "PlayFabId": playfab_id,
        "Data": {"saldo": f"{valor:.2f}"}
    }, secreto = True)

def _ler_nome(playfab_id):
    dados = _post("/Server/GetUserAccountInfo",{"PlayFabId": playfab_id}, secreto=True)
    perfil = dados.get("UserInfo",{}).get("TitleInfo") or {}
    return perfil.get("DisplayName") or playfab_id