

import random
import time

omikuji = ["大吉", "吉", "凶", "中吉"]

# 入力値(もう一度引く)を代入する変数の初期値を"y"(引く)にする
again = "y"

# 入力値が"y"(引く)の間は処理を続ける
while again == "y":
    result = random.choice(omikuji)

    # 出力時に改行しない(end = "")
    # バッファの処理をせずに強制的に出力する(flush = True)
    print("今日の運勢は", end="", flush=True)

    count = 0
    # "..."と3つ出力するため3回ループする条件を指定する
    while count <= 2:
        # 1秒止める
        time.sleep(1)
        # "."を出力する
        print(".", end="", flush=True)
        count += 1

    time.sleep(1)
    # 運勢を出力する(ここでは改行する)
   
    print(f"{result}")
 
 # 「もう一度引く」と確認し、変数に代入する
    again = input("もう一度引く(y/n) > ")

