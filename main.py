
import flask
import requests
import functions
from flask import Flask, Response, request, redirect, url_for, json

app = Flask(__name__)
URL_PATH = 'https://ea0d-2a02-6680-1109-2107-954c-a186-7723-57c1.ngrok.io/'
TOKEN = '5425657434:AAHu53vqfpE75iI7a0fzkYA5ibF7zq9zF5I'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}message'.format(
    TOKEN, URL_PATH)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/')
def sanity(): return "Server is running"


# @app.route('/message', methods=["POST"])
# def handle_message():
#     print("got message")
#     chat_id = request.get_json()['message']['chat']['id']
#     res = requests.get(
#         "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'".format(TOKEN, chat_id, "Got it"))
#     return Response("success")


def sendmessage(chatid, text):
    payload = {
        "text": text,
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
        try:
            msgtype = resp["message"]["entities"][0]["type"]
        except:
            sendmessage(chatid, "use bot command")
            return "NOT SUCCESS"
        if msgtype == "bot_command":
            messages = json.dumps({"chatid": chatid, "text": msgtext})
            try:
                dict_func[str(msgtext).split()[0][1:]](message=messages)
            except:
                sendmessage(chatid, "No such command")
                return "NOT SUCCESS"
        else:
            sendmessage(chatid, "use bot command")
    return "Done"


def command(message):
    message = eval(message)
    chatid = message["chatid"]

    if len(message["text"].split()) == 2:
        text = "not good"
    else:
        text = dict_func[str(message["text"]).split()[0][1:]](message=message)

    payload = {
        "text": text,
        "chat_id": chatid
    }
    resp = requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}'.format(TOKEN, chatid), params=payload)


def prime(message):
    text = message["text"].split()[1]
    return functions.is_prime(int(text))


def factorial(message):
    text = message["text"].split()[1]
    return functions.is_factorial(int(text))


def is_palindrome(message):
    text = message["text"].split()[1]
    return functions.is_palindrome(int(text))


def is_perfect_square(message):
    text = message["text"].split()[1]
    return functions.is_perfect_square(int(text))


dict_func = {"prime": prime}

@app.route("/setwebhook/")
def setwebhook():
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}message".format(TOKEN, URL_PATH))
    if s:
        return "Success"
    else:
        return "fail"


if __name__ == '__main__':
    app.run(port=5002)
