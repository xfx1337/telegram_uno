import random
def choose_card():
    card1 = ["reverse", "red"]
    card2 = ["reverse", "green"]
    card3 = ["reverse", "yellow"]
    card4 = ["reverse", "blue"]

    card5 = ["pass", "red"]
    card6 = ["pass", "green"]
    card7 = ["pass", "yellow"]
    card8 = ["pass", "blue"]

    card9 = ["0", "red"]
    card10 = ["0", "green"]
    card11 = ["0", "yellow"]
    card12 = ["0", "blue"]

    card13 = ["1", "red"]
    card14 = ["1", "green"]
    card15 = ["1", "yellow"]
    card16 = ["1", "blue"]

    card17 = ["2", "red"]
    card18 = ["2", "green"]
    card19 = ["2", "yellow"]
    card20 = ["2", "blue"]

    card21 = ["3", "red"]
    card22 = ["3", "green"]
    card23 = ["3", "yellow"]
    card24 = ["3", "blue"]

    card25 = ["4", "red"]
    card26 = ["4", "green"]
    card27 = ["4", "yellow"]
    card28 = ["4", "blue"]

    card29 = ["5", "red"]
    card30 = ["5", "green"]
    card31 = ["5", "yellow"]
    card32 = ["5", "blue"]

    card33 = ["6", "red"]
    card34 = ["6", "green"]
    card35 = ["6", "yellow"]
    card36 = ["6", "blue"]

    card37 = ["7", "red"]
    card38 = ["7", "green"]
    card39 = ["7", "yellow"]
    card40 = ["7", "blue"]

    card41 = ["8", "red"]
    card42 = ["8", "green"]
    card43 = ["8", "yellow"]
    card44 = ["8", "blue"]

    card45 = ["9", "red"]
    card46 = ["9", "green"]
    card47 = ["9", "yellow"]
    card48 = ["9", "blue"]

    card49 = ["+4", "+4"]
    card50 = ["change", "change"]

    cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, card34, card35, card36, card37, card38, card39, card40, card41, card42, card43, card44, card45, card46, card47, card48, card49, card50]
    card_nw = random.choice(cards)
    return card_nw
import os
import telebot
from telebot import *
Lobby = []
bot = telebot.TeleBot("964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Пиши Lobby для попадания в Lobby")
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "lobby":
        print("registered")
        Lobby.append(str(message.chat.id))
        count = len(Lobby)
        minPlayers = int("2")
        while int(count) < minPlayers:
            print("not enough")
            count = len(Lobby)
            return
        print("enough")
bot.polling()










        
