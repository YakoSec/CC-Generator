# Coder = Mr. Yako
# Instagram: @YakoSec
# GitHub: @YakoSec
# Telegram: @YakoSec

import random

import colorama
from colorama import Fore,Back, Style
colorama.init()

print(Fore.YELLOW)
print("Coder: Mr. Yako \nInstagram: @YakoSec \nTelegram: @YakoSec \nGitHub: @YakoSec")

number = random.randint(1000000000000000, 100000000000000000)
date = random.randint(1, 12)
date1 = random.randint(23, 30)
cvv = random.randint(100, 1000)

print(Fore.RED)
print("Your credit card has been created! ")

print(Fore.GREEN)
print("Num: ", number)
print("Date: ", date, - date1)
print("CVV: ", cvv)
