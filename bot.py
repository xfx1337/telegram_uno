import os, time
import telebot
import sqlite3
import SimpleQIWI
from SimpleQIWI import *
from time import sleep
from telebot import types

bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)

keyboard1.row('Поддержка', 'Меню')
keyboard1.row('Баланс', 'Пополнить', 'Новости')
keyboard1.row('Создать карту')
keyboard1.row('Снять с карты')

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = "Иди нахуй!"
    bot.send_message(message.chat.id, msg, reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'создать карту':
        conn = sqlite3.connect("cards.db") # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        user_id = message.chat.id
        holder = str(message.chat.first_name + " | " + message.chat.last_name)
        test2 = [(user_id, 0, holder)]

        cardCheck = ("SELECT * FROM list WHERE ID LIKE '") + (str(user_id)) + ("%'")
        cursor.execute(cardCheck)

        idCheck = cursor.fetchone()

        if idCheck == None:
            hasCard = 0
        else:
            idCheck = [ idCheck[-3] ]
            idCheck = str(idCheck)
            idCheck = idCheck.replace("'", "")
            idCheck = idCheck.replace("[", "")
            idCheck = idCheck.replace("]", "")
            hasCard = 1
        
        if hasCard == 1 and int(idCheck) == int(user_id):
            bot.send_message(message.chat.id, "У вас уже есть карта!")
            
        elif hasCard == 0:
            cursor.executemany("INSERT INTO list VALUES (?,?,?)", test2)
            bot.send_message(message.chat.id, "Карта успешно созданна!")
            conn.commit()
            
        conn.close()
        
    elif message.text.lower() == 'баланс':
        conn = sqlite3.connect("cards.db") # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        user_id = message.chat.id
        
        bot.send_message(message.chat.id, "Ваш ID:%i" % (user_id))
        
        sqlBalance = ("SELECT * FROM list WHERE ID LIKE '") + (str(user_id)) + ("%'")
        cursor.execute(sqlBalance)
        
        balance = cursor.fetchone()
        balance = [ balance[-2] ]
        balance = str(balance)
        balance = balance.replace("'", "")
        balance = balance.replace("[", "")
        balance = balance.replace("]", "")
        balance = ("Баланс: ") + (balance)
        
        bot.send_message(message.chat.id, balance)

    elif message.text.lower() == 'новости':
        bot.send_message(message.chat.id, "Хуй тебе, а не новости!")
        
    elif message.text.lower() == 'пополнить':
        #conn = sqlite3.connect("transfers.db") # или :memory: чтобы сохранить в RAM
        #cursor = conn.cursor()

        user_id = message.chat.id
        token = "df9febf173fa062dd10dfb199a90c0b1"         # https://qiwi.com/api
        phone = "+79194988902"
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

            if price2 == 1:
                qiwi_pay = qiwi_pay.replace("рублей", "рубль")
            elif price2 > 1 and price < 5:
                qiwi_pay = qiwi_pay.replace("рублей", "рубля")
            
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
                    balance_old = [ balance_old[-1] ]
                    balance_old = balance_old.replace("'", "")
                    balance_old = balance_old.replace("[", "")
                    balance_old = balance_old.replace("]", "")
                    balance_old = int(balance_old)
                    price3 = int(user_price_input)
                    balance = (balance_old) + (price3)
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
    
    elif message.text.lower() == "снять с карты":
        def transferback(message):
            if message.text.isnumeric() == False:
                bot.send_message(message.chat.id, "Неверный тип ввода! Попробуйте снова!")
                status = 0
            elif message.text.isnumeric():
                status = 1
            
            
            conn = sqlite3.connect("cards.db") # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()
            user_id = message.chat.id
        
        
            sqlBalance = ("SELECT * FROM list WHERE ID LIKE '") + (str(user_id)) + ("%'")
            cursor.execute(sqlBalance)
        
            balance = cursor.fetchone()
            balance = [ balance[-2] ]
            balance = str(balance)
            balance = balance.replace("'", "")
            balance = balance.replace("[", "")
            balance = balance.replace("]", "")
            global ammounttotransfer
            ammounttotransfer = message.text
            if status == 1:
                if (message.text) > balance:
                    bot.send_message(message.chat.id, "Недостаточно средств на балансе!!!")
                elif balance > message.text:
                    
                    def transfernext(message):
                        number = str("+7") + str(message.text)
                        global ammounttotransfer

                        token = "df9febf173fa062dd10dfb199a90c0b1"         # https://qiwi.com/api
                        phone = "+79194988902"

                        api = QApi(token=token, phone=phone)
                        api.pay(account=number, amount=ammounttotransfer, comment='Платёж от бота!')
                        bot.send_message(message.chat.id, "Платёж переведён!")
                    
                    
                    
                    
                    sendnumber = bot.send_message(message.chat.id, "Введите номер телефона +7:")
                    bot.register_next_step_handler(sendnumber, transfernext)
        sendask = bot.send_message(message.chat.id, "Сколько ты хочешь снять с карты?")
        bot.register_next_step_handler(sendask, transferback)
        
    else:
        bot.send_message(message.chat.id, 'Упс! Ты тупой гандон! Нажни нормально!')

#keyboard = types.InlineKeyboardMarkup();
bot.polling()
