
import flask
import requests

import Database
import functions
from flask import Flask, request, json

app = Flask(__name__)
URL_PATH = 'https://2c08-82-80-173-170.ngrok.io/'
TOKEN = '5425657434:AAHu53vqfpE75iI7a0fzkYA5ibF7zq9zF5I'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}message'.format(
    TOKEN, URL_PATH)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/')
def sanity(): return "Server is running"


def send_message(chatid, text):
    payload = {
        "text": text,
        "chat_id": chatid
    }
    resp = requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}'.format(TOKEN, chatid), params=payload)


@app.route("/message", methods=["POST", "GET"])
def handle_message():
    """
    Handle message from user.
    :return: Answer for the user.
    """
    if (request.method == "POST"):
        chatid = ''
        try:
            resp = request.get_json()
            msgtext = resp["message"]["text"]
            sendername = resp["message"]["from"]["first_name"]
            chatid = resp["message"]["chat"]["id"]
            name = '{}{}'.format(resp["message"]['chat']['first_name'], resp["message"]['chat']['last_name'])

            msgtype = resp["message"]["entities"][0]["type"]
            if msgtype == "bot_command":
                messages = json.dumps({"chatid": chatid, "text": msgtext, 'name': name})
                command(message=messages)
            else:
                send_message(chatid, "use bot command")

        except Exception as e:
            send_message(chatid, e.args)
            return "NOT SUCCESS"

    return "Done"


def command(message):
    """
    Check message data and sends information about the operation.
    :param message: User message with the operation, and the args
    :return: Information on the message.
    """
    message = eval(message)
    chat_id = message["chatid"]
    text = str(dict_func[str(message["text"]).split()[0][1:]](message))
    send_message(chatid=chat_id, text=text)


@app.route("/setwebhook/")
def setwebhook():
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}message".format(TOKEN, URL_PATH))
    if s:
        return "Success"
    else:
        return "fail"


if __name__ == '__main__':
    dict_func = {"prime": functions.is_prime, "factorial": functions.is_factorial,
                 "palindrome": functions.is_palindrome, "sqrt": functions.is_perfect_square, "help": functions.help
                 , "add": functions.add, 'check': functions.show_coins, 'delete': functions.delete,'close':functions.close}
    app.run(port=5002)



