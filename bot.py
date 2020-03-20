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
bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Пиши Lobby для попадания в Lobby")
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "lobby":
        user = message.chat.id
        f = open ("players.txt", "a")
        f.write(str(user))
        count = 0
        with open("players.txt", "r") as f:
            for line in f:
                count += 1
        while int(count) > int("1"):
            Player1_deck = []
            Player2_deck = []
            for i in range(7):
                Player1_deck.append(choose_card())
            for i in range(7):
                Player2_deck.append(choose_card())
            PNC = int("7")
            Player_now_UCard_Color = "x"
            Player_now_UCard_Number = "x"
            Player_last_UCard_Color = "x"
            Player_last_UCard_Number = "x"
            nw = ["start"]
            choosed = []
            Player1_cards = int("7")
            Player2_cards = int("7")
            Player_now_cards = int("7")
            f = open("players.txt", "r")
            Lobby_now = str(f.readline(1))
            def main(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                def ask2_1(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                    num = message.text
                    if num == "take":
                        Player1_deck.append(choose_card())
                        Player1_cards = int(Player1_cards) + int("1")
                        ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                    else:
                        choosed = Player1_deck[int(num)]
                        bot.send_message(str(f.readline(1)), choosed)
                        Player_now_UCard_Color = choosed[-1]
                        Player_now_UCard_Number = choosed[-2]
                        classic(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                def ask2_2(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                    num = message.text
                    if num == "take":
                        Player2_deck.append(choose_card())
                        Player2_cards = int(Player2_cards) + int("1")
                        ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                    else:
                        choosed = Player2_deck[int(num)]
                        bot.send_message(str(f.readline(2)), choosed)
                        Player_now_UCard_Color = choosed[-1]
                        Player_now_UCard_Number = choosed[-2]
                        classic(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                def ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                    if Lobby_now == f.readline(1):
                        for i in range(len(Player1_deck)):
                            string = str(i) + " " + str(Player1_deck[i])
                            bot.send_message(str(f.readline(1)), string)
                        num_sent = bot.send_message(str(f.readline(1)), "Выбери карту(цифруили если нет карты напиши take):")
                        bot.register_next_step_handler(num_sent, ask2_1(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed))
                    if Lobby_now == f.readline(2):
                        for i in range(len(Player2_deck)):
                            string = str(i) + " " + str(Player2_deck[i])
                            bot.send_message(str(f.readline(2)), string)
                        num_sent = bot.send_message(str(f.readline(2)), "Выбери карту(цифруили если нет карты напиши take):")
                        bot.register_next_step_handler(num_sent, ask2_2(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed))


                def classic_true(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                    if (Player_now_UCard_Number == "+4") or (Player_now_UCard_Number == "change") or (Player_now_UCard_Number == "+2") or (Player_now_UCard_Number == "pass") or (Player_now_UCard_Number == "reverse"):
                        f = open("players.txt", "r")
                        for line in f:
                            bot.send_message(line, "Карта Игрока:")
                            bot.send_message(line, choosed[-1])
                        if choosed[-1] == "+4":
                            if Lobby_now == f.readline(1):
                                Player1_cards = int(Player1_cards) - int("1")
                                Player2_cards = int(Player2_cards) + int("4")
                            color_send = bot.send_message(f.readline(1), "Выбери цвет(blue, red, green, yellow)")
                            bot.register_next_step_handler(color_send, pluse4_1_color(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed))
                            def pluse4_1_color(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                                color = message.text
                                Player_last_UCard_Color = color
                            for i in range(4):
                                Player2_deck.append(choose_card())
                                Player1_deck.remove(choosed)
                            ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                            if Lobby_now == f.readline(2):
                                Player2_cards = int(Player2_cards) - int("1")
                                Player1_cards = int(Player1_cards) + int("4")
                            color_send = bot.send_message(f.readline(2), "Выбери цвет(blue, red, green, yellow)")
                            bot.register_next_step_handler(color_send, pluse4_2_color(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed))
                            def pluse4_2_color(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                                color = message.text
                                Player_last_UCard_Color = color
                            for i in range(4):
                                Player2_deck.append(choose_card())
                                Player1_deck.remove(choosed)
                            ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                        if choosed[1] == "change":
                            if Lobby_now == f.readline(1):
                                Lobby_now = f.readline(2)
                                Player1_cards = int(Player1_cards) - int("1")
                                color_ask = bot.send_message(f.readline(1))
                                bot.register_next_step_handler(color_ask, change_1(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed))
                            if Lobby_now == f.readline(2):
                                Lobby_now = f.readline(1)
                                Player2_cards = int(Player2_cards) - int("1")
                                color_ask = bot.send_message(f.readline(1))
                                bot.register_next_step_handler(color_ask, change_1(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed))
                                def change_1(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                                    color = message.text
                                    Player_last_UCard_Color = color
                                    Player1_deck.remove(choosed)
                                    for line in f:
                                        bot.send_message(line, "Игрок 2 ходит")
                                    ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                                def change_2(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                                    color = message.text
                                    Player_last_UCard_Color = color
                                    Player2_deck.remove(choosed)
                                    for line in f:
                                        bot.send_message(line, "Игрок 1 ходит")
                                        ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                        if choosed[-2] == "pass":
                            if Lobby_now == f.readline(1):
                                Player1_cards = int(Player2_cards) - int("1")
                                Player1_deck.remove(choosed)
                                for line in f:
                                    bot.send_message(line, "Игрок 1 ходит")
                                ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                            if Lobby_now == f.readline(2):
                                Player2_cards = int(Player2_cards) - int("1")
                                Player2_deck.remove(choosed)
                                for line in f:
                                    bot.send_message(line, "Игрок 2 ходит")
                                ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                        if choosed[1] == "+2":
                            if Lobby_now == int("1"):
                                Player1_cards = int(Player1_cards) - int("1")
                                Player2_cards = int(Player2_cards) + int("2")
                                for i in range(2):
                                    Player2_deck.append(choose_card())
                                Player1_deck.remove(choosed)
                                ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                            if Lobby_now == f.readline(2):
                                Player2_cards = int(Player2_cards) - int("1")
                                Player2_deck.remove(choosed)
                                for line in f:
                                    Player1_deck.append(choose_card())
                                ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                        else:
                            for line in f:
                                bot.send_message(line, "Цвет карты игрока")
                                bot.send_message(line, Player_now_UCard_Color)
                                bot.send_message(line, "Номер карты игрока")
                                bot.send_message(line, Player_now_UCard_Number)
                            if Lobby_now == f.readline(1):
                                PNC = int(PNC) - int("1")
                                Player1_cards = PNC
                                try:
                                    Player1_deck.remove(choosed)
                                    if int(Player1_cards) == int("0"):
                                        for line in f:
                                            bot.send_message("Игрок 1 выйграл!!!")
                                    PNC = int(Player2_cards)
                                    Lobby_now = f.readline(2)
                                    Player_last_UCard_Number = "x"
                                    Player_last_UCard_Color = "x"
                                    Player_last_UCard_Number = Player_now_UCard_Number
                                    Player_last_UCard_Color = Player_now_UCard_Color
                                    for line in f:
                                        bot.send_message(line, "Игрок 2 ходит")
                                    ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                                except:
                                    ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                            elif Lobby_now == f.readline(2):
                                PNC = int(PNC) - int("1")
                                Player2_cards = PNC
                                try:
                                    Player2_deck.remove(choosed)
                                    if int(len(Player2_deck)) == int("0"):
                                        for line in f:
                                            bot.send_message(line, "Игрок 2 выйграл!!!")
                                        PNC = int(Player1_cards)
                                        Lobby_now = f.readline(1)
                                        Player_last_UCard_Number = "x"
                                        Player_last_UCard_Color = "x"
                                        Player_last_UCard_Number = Player_now_UCard_Number
                                        Player_last_UCard_Color = Player_now_UCard_Color
                                        for line in f:
                                            bot.send_message(line, "Игрок 1 ходит")
                                        ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                                except:
                                    ask(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)



   
                def classic(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed):
                    if Lobby_now == f.readline(1):
                        PNC = len(Player1_deck)
                    if Lobby_now == f.readline(2):
                        PNC = len(Player2_deck)
                    if (Player_now_UCard_Color == Player_last_UCard_Color) or (Player_now_UCard_Number == Player_last_UCard_Number):
                        classic_true(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                    elif (Player_last_UCard_Color == "x") or (Player_now_UCard_Number == "change") or (Player_now_UCard_Number == "+4"):
                        classic_true(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
                    else:
                        print("")
                                    
                main(Player_now_UCard_Color, Player_now_UCard_Number, Player1_cards, Player2_cards, Player_last_UCard_Number, Player_last_UCard_Color, Lobby_now, Player_now_cards, PNC, Player1_deck, Player2_deck, nw, choosed)
            




bot.polling()
