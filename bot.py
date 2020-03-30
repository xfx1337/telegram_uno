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
Player1_deck = []
Player2_deck = []
Lobby = []
Lobby_Status = "Empty"
PNC = int("7")
Player_now_UCard_Color = "x"
Player_now_UCard_Number = "x"
Player_last_UCard_Color = "x"
Player_last_UCard_Number = "x"
choosed = []
Lobby_now = Lobby[-2]
Player1_cards = int("7")
Player2_cards = int("7")
Player_now_cards = int("7")
import telebot
from telebot import *
bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Пиши Lobby для попадания в Lobby")
@bot.message_handler(commands=['FindLobby'])
def FindLobby(message):
    Lobby.append(message.chat.id)
    print("Registered")
    if len(Lobby) >= 2:
        pass
    else:
        return
    global Player1_deck
    global Player2_deck
    print("Len bigger then")
    for i in range(7):
        Player1_deck.append(choose_card())
    for i in range(7):
        Player2_deck.append(choose_card())
@bot.message_handler(commands=['ChooseCard'])
def ChooseCard(message):
    
    
    global PNC
    global Player_now_UCard_Color
    global Player_now_UCard_Number
    global Player_last_UCard_Color
    global Player_last_UCard_Number
    global choosed
    global Lobby_now
    global Player1_cards
    global Player2_cards
    global Player_now_cards
    
    
    if Lobby_Status is "Empty":
        bot.send_message(message.chat.id, "Лобби пустое")
    if Lobby_Status is "Full":
        pass
    if Lobby_now != message.chat.id:
        bot.send_message(message.chat.id, "Сейчас ходит другой игрок!")
    if Lobby_now == message.chat.id:
        pass
    if Lobby_now == Lobby[-2]:
        for i in range(len(Player1_deck)):
            string = str(i) + " " + str(Player1_deck[i])
            bot.send_message(Lobby[-2], string)
        bot.send_message(message.chat.id, "Напиши номер карты или take(take длч того что бы взять карту из колоды:")
        @bot.message_handler(content_types=['text'])
        def handler(message):
            global PNC
            global Player_now_UCard_Color
            global Player_now_UCard_Number
            global Player_last_UCard_Color
            global Player_last_UCard_Number
            global choosed
            global Lobby_now
            global Player1_cards
            global Player2_cards
            global Player_now_cards
            bot.send_message(message.chat.id, "Вы сходили. Проверка подходит ли ваша карта к прошлой")
            num = message.text
            if num == "take":
                global Player1_deck.append(choose_card())
                global Player1_cards = int(Player1_cards) + int("1")
            else:
                global choosed = Player1_deck[int(num)]
                bot.send_message(Lobby[-2]), choosed)
                global Player_now_UCard_Color = choosed[-1]
                global Player_now_UCard_Number = choosed[-2]
                if Player_now_UCard_Color == Player_last_UCard_Color or Player_now_UCard_Number == Player_last_UCard_Number or Player_last_UCard_Color == "x" or Player_last_UCard_Number == "x" or Player_now_UCard_Number == "change" or (Player_now_UCard_Number == "+4"):
                    pass
                else:
                    return
                bot.send_message(message.chat.id, "Карта подходит!")
                Player_last_UCard_Color == Player_now_UCard_Color
                Player_last_UCard_Number == Player_now_UCard_Number
                if Player_now_UCard_Number == "change":
                    Lobby_now == Lobby[-1]
                    Player1_cards = int(Player1_cards) - int("1")
                    bot.send_message(Lobby[-2], "Цвет для следуешего игрока:")
                    @bot.message_handler(content_types=['text'])
                    def handler(message):
                        global PNC
                        global Player_now_UCard_Color
                        global Player_now_UCard_Number
                        global Player_last_UCard_Color
                        global Player_last_UCard_Number
                        global choosed
                        global Lobby_now
                        global Player1_cards
                        global Player2_cards
                        global Player_now_cards
                        color = message.text
                        Player_last_UCard_Color = color
                        Player1_deck.remove(choosed)
                if Player_now_UCard_Number == "+4":
                    Player1_cards = int(Player1_cards) - int("1")
                    Player2_cards = int(Player2_cards) + int("4")
                    bot.send_message(Lobby[-2], "Выбери цвет для следуешего игрока:")
                    @bot.message_handler(content_types=['text'])
                    def handler(message):
                        global PNC
                        global Player_now_UCard_Color
                        global Player_now_UCard_Number
                        global Player_last_UCard_Color
                        global Player_last_UCard_Number
                        global choosed
                        global Lobby_now
                        global Player1_cards
                        global Player2_cards
                        global Player_now_cards
                        color = message.text
                        global Player_last_UCard_Color = color
                        global Player1_deck.remove(choosed)
                        for i in range(4):
                            global Player2_deck.append(choose_card())
                    
                














