import os
import sys
import random

game = random.randint(1, 4)

print(game)
if (game == 1):
    os.system("python3 FlappyChoco/main.py")
elif (game == 2):
    os.system("./SHOKOBANG/MY_CHOCOBANG SHOKOBANG/map/Level_1")
elif (game == 3):
    print("pack openning soon...")
elif (game == 4):
    os.system("./'Choco Jump'/'the game'/'Super Choco Bros.x86_64'")