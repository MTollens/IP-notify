
import requests
import json
import subprocess
from time import sleep

# retreive token from tokenfile
with open('tokenfile', 'r') as f:
    token = json.load(f)

url = 'https://api.telegram.org/bot{}/'.format(token)

def get_updates(offset=None):
    print("getting updates")
    while True:
        try:
            URL = url + 'getUpdates'
            if offset:
                URL += '?offset={}'.format(offset)

            res = requests.get(URL)
            while res.status_code != 200 or len(res.json()['result']) == 0:
                sleep(2)
                res = requests.get(URL)
            # print(res.url)
            # print("got request")
            return res.json()

        except:
            pass;

def get_last(data):
    print("getting last")
    results = data['result']
    count = len(results)
    last = count - 1
    last_update = results[last]
    return last_update

def get_last_id_text(updates):
    print("getting last ID text")
    last_update = get_last(updates)
    chat_id = last_update['message']['chat']['id']
    update_id = last_update['update_id']
    try:
        text = last_update['message']['text']
    except:
        text = ''
    return chat_id, text, update_id

def send_message(chat_id, text, reply_markup=None):
    # print("sending message {}".format(text))
    URL = url + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    print(chat_id)
    # print("chat ^")
    if reply_markup:
        URL += '&reply_markup={}'.format(reply_markup)
    res = requests.get(URL)
    while res.status_code != 200:
        res = requests.get(URL)
    print(res.status_code)

def main():
    text = ''
    # we need to get the chat_id because it is required by the telegram API,
    # theoretically we could save it to disk when the program finishes, but it is better to check every time
    chat_id, text, update_id = get_last_id_text(get_updates())
    # print("starting")

    # provide whatever message you need here
    # given example on next line is to get the device IP address
    # message = subprocess.getoutput("ifconfig | grep 'inet 128*'")
    message = "your message here"
    send_message(chat_id, message)


if __name__ == '__main__':
    main()
