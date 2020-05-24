import os, time
import telebot
import sqlite3
from SimpleQIWI import *
from time import sleep
from telebot import types
bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')
newspath = input('Enter path to message to send to user as News!:')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('Поддержка', 'Меню')
keyboard1.row('Баланс', 'Пополнить', 'Новости')
keyboard1.row('Создать карту')
keyboard1.row('Снять с карты')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, msg, reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'создать карту':
        conn = sqlite3.connect("cards.db") # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        user_id = message.chat.id
        zero_str = ("0")
        holder = [((message.first_name), (message.last_name))]
        zero = int(zero_str)
        test2 = [((user_id), (zero), (holder))]
        cursor.executemany("INSERT INTO list VALUES (?,?,?)", test2)
        conn.commit()
        conn.close()
    elif message.text.lower() == 'баланс':
        conn = sqlite3.connect("cards.db") # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        user_id = message.chat.id
        bot.send_message(message.chat.id, "Ваш ID:%i" % (user_id))
        user_id2 = str(user_id)
        sqlBalance = ("SELECT * FROM list WHERE ID LIKE '") + (user_id2) + ("%'")
        cursor.execute(sqlBalance)
        balance = cursor.fetchone()
       	balance2 = [ balance[-1] ]
       	balance3 = str(balance2)
       	balance4 = balance3.replace("'", "")
       	balance5 = balance4.replace("[", "")
       	balance5 = balance5.replace("]", "")
        balance_send = ("Баланс: ") + (balance5)
        bot.send_message(message.chat.id, balance_send) 
    elif message.text.lower() == 'пополнить':
        #conn = sqlite3.connect("transfers.db") # или :memory: чтобы сохранить в RAM
        #cursor = conn.cursor()

        user_id = message.chat.id
        token = "102bdafd326e59af4a61826098f5311e"         # https://qiwi.com/api
        phone = "+79124862813"
        def transfer(message):
            conn = sqlite3.connect("transfers.db") # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()
            user_price_input = (message.text)

            #user_price_input = ("1") # Здесь нужно получать значение суммы платежа от пользователя(А пока-что выставлено просто 1)
            api = QApi(token=token, phone=phone)
            price2 = int(user_price_input)
            price = price2             # Минимальное значение при котором счет будет считаться закрытым
            comment = api.bill(price)   # Создаем счет. Комментарий с которым должен быть платеж генерируе$

            bot.send_message(message.chat.id, "Ваш ID:%i" % (user_id))
            qiwi_pay= ('''
Отправьте %i рублей на QIWI кошелёк "+79124862813" с комментарием:
%s        
            ''' % (price2, comment))
            #bot.send_message(message.chat.id, "Отправьте сумму которую хотите получить на свой баланс на QIWI кошелёк: +79124862813 с комментарием(ПОКА-ЧТО МОЖНО ОТПРАВИТЬ ТОЛЬКО 1РУБЛЬ, ЗАВТРА ПОФИКШУ): %s" % (comment))
            bot.send_message(message.chat.id, qiwi_pay)
            api.start()                 # Начинаем прием платежей

            while True:
                if api.check(comment):  # Проверяем статус
                    test = [((user_id), (user_price_input), (comment))]

                    cursor.executemany("INSERT INTO list VALUES (?,?,?)", test)
                    conn.commit()
                    conn.close()
                    conn = sqlite3.connect("balances.db") # или :memory: чтобы сохранить в RAM
                    cursor = conn.cursor()
#user_id = input("Enter test User ID(Telegram ID)!:")
                    user_id2 = str(user_id)
                    sql0 = "SELECT * FROM list WHERE ID LIKE '" + (user_id2) + ("'")
                    cursor.execute(sql0)
                    balance_old = (cursor.fetchone())
                    balance_old2 = [ balance_old[-1] ]
                    balance_old3 = str(balance_old2)
                    balance_old4 = balance_old3.replace("'", "")
                    balance_old5 = balance_old4.replace("[", "")
                    balance_old6 = balance_old5.replace("]", "")
                    balance_old7 = int(balance_old6)
                    price3 = int(user_price_input)
                    balance = (balance_old7) + (price3)
                    sql = ('''
UPDATE list
SET BALANCE = '%i'
WHERE ID = '%s'
''' % (balance, user_id))
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    break
        sent = bot.send_message(message.chat.id, "Введите сумму для перевода на ваш баланс!")

        bot.register_next_step_handler(sent, transfer)
        sleep(1)
    else:
        bot.send_message(message.chat.id, 'Упс! Ты ввёл не правельную комманду! Пиши "Меню" что получить подсказку!')

#keyboard = types.InlineKeyboardMarkup();
bot.polling()
