import mysql.connector

CONFIG = {
    "HOST": "localhost",
    "user": "root",
    "passoword": "",
    "database": "loja"
}

def conectar():
    return mysql.connector.connect(**CONFIG)