from flask import Flask
import os
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1354466607052755108/5EpHOLTLbXqQW7yW8VWlK4ydsiJvJ4_PoKar0_zHnPSxLiq0ipBDHc7EwGNaqRbyph-I'
ARQUIVO_CONTADOR = "contador.txt"
emoji_amarelo = "🔶"
emoji_preto = "⚫"


def enviar_mensagem():
    if not os.path.exists(ARQUIVO_CONTADOR):
        with open(ARQUIVO_CONTADOR, "w") as f:
            f.write("2")

    with open(ARQUIVO_CONTADOR, "r") as f:
        dia_atual = int(f.read().strip()) + 1

    with open(ARQUIVO_CONTADOR, "w") as f:
        f.write(str(dia_atual))

    if dia_atual % 2 == 1:
        mensagem = f"{emoji_amarelo}{emoji_preto} Dia {dia_atual} sem Gol de Placa!"
    else:
        mensagem = f"{emoji_amarelo}{emoji_preto} Dia {dia_atual} sem Gol de Placa."

    data = {
    "content": mensagem,
    "username": "THIAGO ALMADA INFORMA",
    "avatar_url": "https://imgur.com/a/yNnRXPk"  # aqui vai o link da imagem
    }


    print("Mensagem enviada!" if response.status_code == 204 else f"Erro: {response.status_code}")

@app.route('/')
def home():
    return "Servidor do Gol de Placa está ativo!"

@app.route('/disparar')
def disparar():
    enviar_mensagem()
    return "Mensagem enviada pro Discord!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
