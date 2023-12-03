import os
import sys
import random

game = random.randint(1, 3)

print(game)
if (game == 1 or sys.argv[1] == "flappy"):
    os.system("python3 FlappyChoco/main.py")
elif (game == 2):
    os.system("./SHOKOBANG/MY_CHOCOBANG SHOKOBANG/map/Level_1")
elif (game == 3):
    print("pack openning soon...")