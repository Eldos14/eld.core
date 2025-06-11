import telebot
import requests

token = "7846667446:AAGBBNpdLsHm17WsVYha2LOonO_tgIhGL4c"
bot = telebot.TeleBot(token)

white_list = [5305489290, 1213131313, 55464546, 4546546547, 1213131313]

def get_inf(article):
    if len(article) > 7:
        return None
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "referer": "https://www.wildberries.ru/catalog/4051515/detail.aspx"
    }

    url = f"https://alm-basket-cdn-01.geobasket.ru/vol{article[0:2]}/part{article[0:4]}/{article}/info/ru/card.json"
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()
            return data  
        else:
            return None
    except :
        return None

def get_info(article):
    if len(article) > 7:
        return None
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "referer": "https://www.wildberries.ru/catalog/4051515/detail.aspx"
    }

    url = f"https://basket-13.wbbasket.ru/vol{article[0:4]}/part{article[0:6]}/{article}/info/price-history.json"
    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()
        
            if not data:
                print("Нет данных по цене.")
            else:
            
                last_price = data[-1]["price"]["RUB"] / 100
                print(f" Текущая цена: {last_price:.2f} ₽")
        else:
            print(f"Ошибка: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")



def bool_login(chat_id):
    return chat_id in white_list

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if bool_login(message.chat.id):
        bot.reply_to(message, f"Добро пожаловать! Ваш ID: {message.chat.id}")
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет доступа.")

@bot.message_handler(commands=["text"])
def analytics(message):
    if bool_login(message.chat.id):
        answer = get_inf(message.text)
        if answer is not None:
            bot.reply_to(message, f"{answer}")
        else:
            bot.send_message(message.chat.id, "Такого товара не существует")
    else:
        bot.send_message(message.chat.id, "Доступ к боту отсутствует, купите подписку")

@bot.message_handler(commands=["price"])
def analytics_price(message):
    if bool_login(message.chat.id):
        answer = get_inf(message.text)
        if answer is not None:
            bot.reply_to(message, f"{answer}")
        else:
            bot.send_message(message.chat.id, "Такого товара не существует")
    else:
        bot.send_message(message.chat.id, "Доступ к боту отсутствует, купите подписку")

bot.polling()
