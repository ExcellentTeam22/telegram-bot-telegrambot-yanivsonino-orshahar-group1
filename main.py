import flask
import requests
from flask import Flask, Response, request

app = Flask(__name__)
URL_PATH = 'https://d9f1-82-80-173-170.ngrok.io/'
TOKEN = '5425657434:AAHu53vqfpE75iI7a0fzkYA5ibF7zq9zF5I'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}message'.format(
    TOKEN, URL_PATH)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/sanity')
def sanity(): return "Server is running"


# @app.route('/message', methods=["POST"])
# def handle_message():
#     print("got message")
#     chat_id = request.get_json()['message']['chat']['id']
#     res = requests.get(
#         "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'".format(TOKEN, chat_id, "Got it"))
#     return Response("success")


def sendmessage(chatid):
    payload = {
        "text": "heyy",
        "chat_id": chatid
    }
    resp = requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}'.format(TOKEN, chatid), params=payload)

@app.route("/message", methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        resp = request.get_json()
        msgtext = resp["message"]["text"]
        sendername = resp["message"]["from"]["first_name"]
        chatid = resp["message"]["chat"]["id"]
        sendmessage(chatid)
    return "Done"


@app.route("/setwebhook/")
def setwebhook():
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}message".format(TOKEN, URL_PATH))
    if s:
        return "Success"
    else:
        return "fail"


if __name__ == '__main__':
    app.run(port=5002)
