import time

from telebot import TeleBot
from  telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types

TOKEN = "7564364151:AAGK4Jh07TKBPWpM0uyIY9T7kiMdxrmtjWQ"


bot = TeleBot(TOKEN)
otvet = 0
vopros = 0
qestion = [
    ["В каком году был пидписан договор о ненападении между Германией и СССР", "1938", "1939", "1940", "1941"],
    ["Как назывался План нападения Германии на СССР?", "«Багратион»", "«Барбаросса»", "«Цитадель»", "«Гроза»"],
    ["Кто из официальных лиц СССР первым сообщил по радио о нападении нацистской Германии?", "Иосиф Сталин", "Георгий Жуков", "Вячеслав Молотов", "Юрий Левитан"],
    ["Когда впервые применили БМ-13 «Катюша» - реактивную систему залпового огня?", "14 июля 1941 года", "31 августа 1941 года", "30 сентября 1941 года", "5 декабря 1941 года"],
    ["Как называется знаменитая винтовка, прослужившая с 1891 года до 60-х годов XX века?", "Винтовка Симонова", "Винтовка Мосина", "Винтовка Калашникова", "Винтовка Токарева"],
    ["Утром 22 июня 1941 года нацистская Германия напала на СССР. Почему именно этот день был выбран гитлеровским командованием для начала военных действий?","День выбран случайным образом","Хороший прогноз погоды для авиации","В честь проведения первого авиашоу в Реймсе в 1909 году","Самый длинный световой день в году"],
    ["Утром 22 июня 1941 года народному комиссару иностранных дел В. Молотову от имени правительства Германии было сделано заявление, означавшее объявление войны. Кто сделал это заявление?","В. Шуленбург", "И. Риббентроп", "К. фон Нейрат", "Г. Мюллер"],
    ["Самым массовым истребителем ВВС Красной Армии на момент начала войны был…", "И-16, ишачок","У-2, кукурузник", "Як-1", "Ла-5"],

]
correct_answers_list = ["1939", "«Барбаросса»", "Георгий Жуков", "14 июля 1941 года", "Винтовка Мосина", "Самый длинный световой день в году", "В. Шуленбург","И-16, ишачок"]


markup_start =ReplyKeyboardMarkup(row_width=4)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bt1 = types.KeyboardButton('ОК')
    markup_start.row(bt1)
    bot.send_message(message.chat.id, "Здарова бездарь, пройди тест о ВОВ", reply_markup=markup_start)
    bot.register_next_step_handler(message, NextChoiceMarcup)

@bot.message_handler()
def NextChoiceMarcup(message):
    global vopros, otvet
    if message.text == 'ОК':
        markup_quest = ReplyKeyboardMarkup(row_width=4)
        markup_quest.row(f"{qestion[vopros][1]}", f"{qestion[vopros][2]}")
        markup_quest.row(f"{qestion[vopros][3]}", f"{qestion[vopros][4]}")
        bot.send_message(message.chat.id, f"{qestion[vopros][0]}",reply_markup=markup_quest)
        bot.register_next_step_handler(message, Answer)

@bot.message_handler()
def Answer(message):
    global otvet, vopros
    if message.text in correct_answers_list:
        bot.send_message(message.chat.id,"Правильно! Давай дальше.", reply_markup=markup_start)
        otvet += 1
        vopros += 1
        if vopros == 8:
            bot.send_message(message.chat.id, f"Поздравляю с окнчанием теста! Ты набрал {otvet} из 8 баллов", reply_markup=markup_start)
        else:
            bot.register_next_step_handler(message, NextChoiceMarcup)
    else:
        bot.send_message(message.chat.id, "Неправильно! Давай дальше?", reply_markup=markup_start)
        vopros += 1
        if vopros == 8:
            bot.send_message(message.chat.id, f"Поздравляю с окнчанием теста! Ты набрал {otvet} из 8 баллов", reply_markup=markup_start)
        else:
            bot.register_next_step_handler(message, NextChoiceMarcup)




bot.infinity_polling()


