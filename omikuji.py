# importing 

import random

# function to receive a random option from a tuple 

def omikuji():
    luck = (
        '大吉 (Daikichi) - Great fortune',
        '中吉 (Chuukichi) - Middle fortune',
        '小吉 (Shoukichi) - Small fortune',
        '吉 (Kichi) - Fortune',
        '凶 (Kyou) - Bad luck',
        '大凶 (Daikyou) - Great bad luck',
        '末吉 (Suekichi) - Future fortune',
        '幸運 (Kouun) - Good luck',
        '平安 (Heian) - Peace and safety',
        '成功 (Seikou) - Success'
    )

    # Randomly select an option
    options_random = random.randint(0, 9)
    print(luck[options_random])

# terminal input 

terminal = int(input('Look! You\'ve just found an omikuji! What do you want to do with it?\n'
                     '0. Try your luck!\n'
                     '1. Do nothing\n'))

if terminal == 0:
    omikuji()
else:
    pass