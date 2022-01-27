import requests
def telegram_bot_sendtext(bot_message):
    bot_token = 'telegram_token'
    bot_chatID = 'telegram_chat-id'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=html&text=' + bot_message
    try:
        response = requests.get(send_text)
    except Exception as e:
        print("\n")
        print(Fore.RED+"Failed to send the message \U0001F641 ")
        print(e)
try:
    response=requests.get('https://ajax.staging.luno.com/ajax/1/display_ticker')
    bot_message='<b>BITCOIN PRICE USD \U0001F60A </b>\n'+str(response.text)
    telegram_bot_sendtext(bot_message)
except Exception as e:
    print(e)
