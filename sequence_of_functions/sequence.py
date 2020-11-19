#czego brakuje:
#zmienne i funkcje zajmujące się pieniędzmi (wraz ze stawkami aby wejść - 1. i 2. osoba)
#kolejność ludzi (i botów) zmieniająca się w kolejnych rundach
#pulę pieniędzy

from player_class.py import Players
from player_class.py import Bots

#roboczo tablicami, jeśli będziemy robić to obiektowo to się przerobi
karty[8][2]; #[liczba graczy][karty ludzi - oznczenie od 2 do 15 np][kolor karty]
stol[6][2]; #karty wylosowane na stół, [wartość 0 - nie ma tej karty jeszcze][kolor]. [6][0] jest po to, aby pętla while wiedziała kiedy się zakończyć

def if_amount_same(): #spr czy każdy ma tyle samo obstawione, wtedy przechodzi do kolejnej rundy - liczba kart na stole ++ v koniec gry i sprawdzenie kto wygrał

player = Players()

for x in range(7):
    bot.append(0)
    bot[nr] = Bots()
    nr += 1

rand_deck() #wylosowanie dla każdego gracza 2 kart i 3 kart na stół
while (stol[5][0] != 0)
    while (if_amount_same()=false)
    bot_choice() #powtorzenie dla liczby graczy -1, na razie dla testów trzeba zrobić randomowe decyzje
    player_choice() #wybór: fold, call, raise (i ile)
check_points() #kto wygrał
player_amount() #zaktualizowanie pieniędzy gracza - jeśli wygrał zgarnia wszystko
