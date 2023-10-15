import telebot
import random
from telebot import types

token='6543780776:AAFdZcoOLYImo9O5QA-NsYhDH0CZrMhc3X0'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Я помогу придумать отмазку\n\n Чтобы оправдать своё опаздание, введите: /late\n")
        
@bot.message_handler(commands=['late'])
def excuse_handler(message):
    list1 = ["Я задерживаюсь", "Опаздываю", "Приду позже запланированного", "Мне неловко, но я не успеваю к сроку", "Буду позже, чем обычно"]
    list2 = ["потому, что", "в связи с тем, что", ", так как", "по причине того, что"]
    list3 = ["сосед", "автобус", "ветер", "живот", "холодильник"]
    list4 = ["при попытке выдвинуться из дома засвистел как ненормальный", "выглядел подозрительно", "заставил задуматься о вечном", "чуть не столкнул с дороги", "показал свою несостоятельность", "решил надо мной подшутить"]
    list6 = [" и", ", затем", ", что вскоре"]
    list7 = ["стало невыносимо грусно", "закружилась голова", "пошли дурные мысли", "поднялась температура", "перехотелось ехать", "возникло стойкое ощущение тоски"]
    excuse = random.choice(list1) + " " + random.choice(list2) + " " + random.choice(list3) + " " + random.choice(list4) + random.choice(list6) + " " + random.choice(list7) + "!"
    bot.send_message(message.chat.id, excuse)
        
bot.infinity_polling()