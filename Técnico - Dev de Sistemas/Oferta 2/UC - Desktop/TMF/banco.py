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


MENSAGENS = {
    "AccountNotFound": "E-mail ou senha incorretos.",
    "InvalidEmailOrPassword": "E-mail ou senha incorretos.",
    "InvalidUsernameOrPassword": "E-mail ou senha incorretos.",
    "InvalidEmailAddress": "Informe um e-mail válido.",
    "EmailAddressNotAvailable": "Já existe uma conta com esse e-mail.",
    "InvalidPassword": "Senha inválida (mínimo de 6 caracteres).",
    "InvalidParams": "Dados inválidos. Confira os campos.",
    "InvalidSecretKey": "Secret Key inválida (veja config.py).",
    "InvalidAPIEndpoint": "Title ID inválido (veja config.py).",
}


def _post(caminho, corpo, secreto=False):
    if not config.TITLE_ID:
        raise ErroBanco("Title ID não configurado (veja config.py).")
    if secreto and not config.SECRET_KEY:
        raise ErroBanco("Secret Key não configurada (veja config.py).")

    cabecalhos = {"X-SecretKey": config.SECRET_KEY} if secreto else {}

    url = f"https://{config.TITLE_ID}.playfabapi.com{caminho}"

    try:
        resposta = requests.post(url, json=corpo, headers=cabecalhos, timeout=15)
        dados = resposta.json()
    except requests.RequestException:
        raise ErroBanco("Não foi possível falar com o PlayFab. Verifique a internet.")
    except ValueError:
        raise ErroBanco("Resposta inesperada do PlayFab.")

    if resposta.status_code != 200:
        codigo = dados.get("error", "")
        raise ErroBanco(
            MENSAGENS.get(codigo, dados.get("errorMessage", "Erro no PlayFab."))
        )

    return dados.get("data", {})


def _ler_saldo(playfab_id):
    dados = _post(
        "/Server/GetUserData",
        {
            "PlayFabId": playfab_id,
            "Keys": ["saldo"],
        },
        secreto=True,
    )

    registro = dados.get("Data", {}).get("saldo")
    return float(registro["Value"]) if registro else 0.0


def _gravar_saldo(playfab_id, valor):
    _post(
        "/Server/UpdateUserData",
        {
            "PlayFabId": playfab_id,
            "Data": {"saldo": f"{valor:.2f}"},
        },
        secreto=True,
    )


def _ler_nome(playfab_id):
    dados = _post(
        "/Server/GetUserAccountInfo",
        {"PlayFabId": playfab_id},
        secreto=True,
    )

    perfil = dados.get("UserInfo", {}).get("TitleInfo", {}) or {}
    return perfil.get("DisplayName") or playfab_id


def _buscar_id(email):
    try:
        dados = _post(
            "/Admin/GetUserAccountInfo",
            {"Email": email},
            secreto=True,
        )
    except ErroBanco:
        return None

    return dados.get("UserInfo", {}).get("PlayFabId")


def cadastrar(email, nome, senha):
    dados = _post(
        "/Client/RegisterPlayFabUser",
        {
            "TitleId": config.TITLE_ID,
            "Email": email,
            "Password": senha,
            "DisplayName": nome,
            "RequireBothUsernameAndEmail": False,
        },
    )

    playfab_id = dados["PlayFabId"]
    _gravar_saldo(playfab_id, config.SALDO_INICIAL)

    return Conta(email, nome, config.SALDO_INICIAL, playfab_id)


def autenticar(email, senha):
    dados = _post(
        "/Client/LoginWithEmailAddress",
        {
            "TitleId": config.TITLE_ID,
            "Email": email,
            "Password": senha,
        },
    )

    playfab_id = dados["PlayFabId"]

    return Conta(
        email,
        _ler_nome(playfab_id),
        _ler_saldo(playfab_id),
        playfab_id,
    )


def recarregar(conta):
    conta.saldo = _ler_saldo(conta.playfab_id)


def sacar(conta, valor):
    if valor <= 0:
        raise ErroBanco("Informe um valor maior que zero.")

    if valor > conta.saldo:
        raise ErroBanco("Saldo insuficiente.")

    _gravar_saldo(conta.playfab_id, conta.saldo - valor)
    conta.saldo -= valor


def transferir(conta, email_destino, valor):
    if email_destino.strip().lower() == conta.email.strip().lower():
        raise ErroBanco("Escolha uma conta diferente da sua.")

    id_destino = _buscar_id(email_destino)

    if not id_destino:
        raise ErroBanco("Conta de destino não encontrada.")

    saldo_destino = _ler_saldo(id_destino)
    nome_destino = _ler_nome(id_destino)

    sacar(conta, valor)
    _gravar_saldo(id_destino, saldo_destino + valor)

    return nome_destino