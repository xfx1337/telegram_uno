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
Lobby = ([])
minPlayers = int("2")
bot = telebot.TeleBot("964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Пиши Lobby для попадания в Lobby")
@bot.message_handler(content_types=['text'])
def send_text(message):
    def main(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC):
            def classic_true():
                if (Player_now_UCard_Number == "+4") or (Player_now_UCard_Number == "change") or (Player_now_UCard_Number == "+2") or (Player_now_UCard_Number == "pass") or (Player_now_UCard_Number == "reverse"):
                    for user in Lobby:
                        bot.send_message(user, "Карта ходящего игрока:")
                        bot.send_message(user, choosed)
                    if choosed[-1] == "+4":
                        if Lobby_now == Lobby[-2]:
                            Player1_cards = int(Player1_cards) - int("1")
                            Player2_cards = int(Player2_cards) + int("4")
                            color_send = bot.send_message(Lobby[-2], "Выбери цвет(blue, red, yellow, blue):")
                            bot.register_next_step_handler(color_send, pluse4_1_color())
                            def pluse_1_color():
                                while (message.text.lower != "blue") or (message.text.lower != "red") or (message.text.lower != "yellow") or (message.text.lower != "green"):
                                    return
                                color = message.text.lower
                                Player_last_UCard_Color = color
                                for i in range(4):
                                    Player2_deck.append(choose_card())
                                Player1_deck.remove(choosed)
                                for user in Lobby:
                                    bot.send_message(user, "Игрок 1 сходил:")
                                    bot.send_message(user, choosed)
                                    bot.send_message(user, "Сменил цвет на:")
                                    bot.send_message(user, Player_last_UCard_Color)
                                ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                        if Lobby_now == Lobby[-1]:
                            Player2_cards = int(Player2_cards) - int("1")
                            Player1_cards = int(Player1_cards) + int("4")
                            color_send = bot.send_message(Lobby[-1], "Выбери цвет(blue, red, yellow, blue):")
                            bot.register_next_step_handler(color_send, pluse4_2_color())
                            def pluse_2_color():
                                while (message.text.lower != "blue") or (message.text.lower != "red") or (message.text.lower != "yellow") or (message.text.lower != "green"):
                                    return
                                color = message.text.lower
                                Player_last_UCard_Color = color
                                for i in range(4):
                                    Player1_deck.append(choose_card())
                                Player2_deck.remove(choosed)
                                for user in Lobby:
                                    bot.send_message(user, "Игрок 2 сходил:")
                                    bot.send_message(user, choosed)
                                    bot.send_message(user, "Сменил цвет на:")
                                    bot.send_message(user, Player_last_UCard_Color)
                                ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                    if choosed[-1] == "change":
                        if int(Lobby_now) == int(Lobby[-2]):
                            
                            Lobby_now == Lobby[-1]
                            Player1_cards = int(Player1_cards) - int("1")
                            color_ask = bot.send_message(Lobby[-2], "Выбери цвет(red, blue, green, yellow):")
                            bot.register_next_step_handler(color_ask, change_1())
                            def change_1():
                                while (message.text.lower != "blue") or (message.text.lower != "red") or (message.text.lower != "yellow") or (message.text.lower != "green"):
                                    return
                                color = message.text.lower
                                Player_last_UCard_Color = color
                                Player1_deck.remove(choosed)
                                for user in Lobby:
                                    bot.send_message(user, "Игрок 1 сходил:")
                                    bot.send_message(user, choosed)
                                    bot.send_message(user, "Сменил цвет на: ")
                                    bot.send_message(user, Player_last_UCard_Color)
                                ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                        if Lobby_now == Lobby[-1]:
                            
                            Lobby_now == Lobby[-2]
                            Player2_cards = int(Player2_cards) - int("1")
                            color_ask = bot.send_message(Lobby[-1], "Выбери цвет(red, blue, green, yellow):")
                            bot.register_next_step_handler(color_ask, change_2())
                            def change_2():
                                while (message.text.lower != "blue") or (message.text.lower != "red") or (message.text.lower != "yellow") or (message.text.lower != "green"):
                                    return
                                color = message.text.lower
                                Player_last_UCard_Color = color
                                Player2_deck.remove(choosed)
                                for user in Lobby:
                                    bot.send_message(user, "Игрок 2 сходил:")
                                    bot.send_message(user, choosed)
                                    bot.send_message(user, "Сменил цвет на: ")
                                    bot.send_message(user, Player_last_UCard_Color)
                                ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                    if choosed[1] == "+2":
                        if Lobby_now == Lobby[-2]:
                            Player1_cards = int(Player1_cards) - int("1")
                            Player2_cards = int(Player2_cards) + int("2")
                            for i in range(2):
                                Player2_deck.append(choose_card())
                            Player1_deck.remove(choosed)
                            ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                        if Lobby_now == Lobby[-1]:
                            Player2_cards = int(Player2_cards) - int("1")
                            Player1_cards = int(Player1_cards) + int("2")
                            for i in range(2):
                                Player1_deck.append(choose_card())
                            Player2_deck.remove(choosed)
                            ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                    if choosed[-2] == "pass":
                        if Lobby_now == Lobby[-2]:
                            Player1_cards = int(Player1_cards) - int("1")
                            for user in Lobby:
                                bot.send_message(user, "Игрок 1 ходит снова")
                                bot.send_message(user, "Сходил ")
                                bot.send_message(user, choosed)
                            ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                        if Lobby_now == Lobby[-1]:
                            Player2_cards = int(Player2_cards) - int("1")
                            for user in Lobby:
                                bot.send_message(user, "Игрок 2 ходит снова")
                                bot.send_message(user, "Сходил ")
                                bot.send_message(user, choosed)
                            ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)


            def classic(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC):
                if Lobby_now == Lobby[-2]:
                    PNC = len(Player1_deck)
                if Lobby_now == Lobby[-1]:
                    PNC = len(Player2_deck)
                if (Player_now_UCard_Color == Player_last_UCard_Color) or (Player_now_UCard_Number == Player_last_UCard_Number):
                    classic_true(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                elif (Player_last_UCard_Color == "x") or (Player_now_UCard_Number == "change") or (Player_now_UCard_Number == "+4"):
                    classic_true(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                else:
                    ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
  
            def ask2_1(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC):
                if message.text.lower == "take":
                    Player2_deck.append(choose_card())
                    Player2_cards = int(Player2_cards) + int("1")
                    ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                else:
                    print("else2")
                    choosed == Player2_deck[int(message.text)]
                    bot.send_message(Lobby[-1], choosed)
                    Player_now_UCard_Color = choosed[-1]
                    Player_now_UCard_Number = choosed[-2]
                    print("else2_2")
                    classic(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                    
            def ask2_2(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC):
                if message.text.lower == "take":
                    Player2_deck.append(choose_card())
                    Player2_cards = int(Player2_cards) + int("1")
                    ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                else:
                    print("else2")
                    choosed == Player2_deck[int(message.text)]
                    bot.send_message(Lobby[-1], choosed)
                    Player_now_UCard_Color = choosed[-1]
                    Player_now_UCard_Number = choosed[-2]
                    print("else2_2")
                    classic(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
                    







            def ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC):
                if Lobby_now == Lobby[-2]:
                    for card in range(len(Player1_deck)):
                        string = str(card) + " " + str(Player1_deck[card])
                        bot.send_message(Lobby[-2], string)
                    num_sent = bot.send_message(Lobby[-2], "Выбери карту(цифра или пропиши take что взять карту из колоды):")
                    choosed = []
                    PNC == int("7")
                    bot.register_next_step_handler(num_sent, ask2_1(Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC))
                if Lobby_now == Lobby[-1]:
                    for card in range(len(Player2_deck)):
                        string = str(card) + " " + str(Player2_deck[i])
                        bot.send_message(Lobby[-1], string)
                    num_sent = bot.send_message(Lobby[-1], "Выбери карту(цифра или ake что бы взять карту из колоды):")
                    choosed = []
                    bot.register_next_step_handler(num_sent, ask2_2(Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC))
            ask(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
    def uno_start():
            message = ""
            Player_now_UCard_Color = "x"
            Player_now_UCard_Number = "x"
            Player_last_UCard_Color = "x"
            Player_last_UCard_Number = "x"
            choosed = []
            Player1_deck = []
            Player2_deck = []
            PNC = int("7")
            for i in range(7):
                Player1_deck.append(choose_card())
            for i in range(7):
                Player2_deck.append(choose_card())
            PNC = int("7")
            Player_now_UCard_Color = "x"
            Player_now_UCard_Number = "x"
            Player_last_UCard_Color = "x"
            Player_last_UCard_Number = "x"
            choosed = []
            Lobby_now = Lobby[-2]
            for user in Lobby:
                bot.send_message(user, "Игрок 1 ходит")
            main(message, Player_now_UCard_Color, Player_now_UCard_Number, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player1_deck, Player2_deck, choosed, PNC)
    if message.text.lower() == "lobby":
        print("registered")
        Lobby.append(str(message.chat.id))
        minPlayers = int("2")
        while int(len(Lobby)) < minPlayers:
            print("not enough")
            return
        while len(Lobby) == int("2"):
            uno_start()
bot.polling()
