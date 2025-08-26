# サイコロの面の数は?: 8
# 何回振りますか?: 20
# [6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]


import random


def main():

    # ユーザーから入力を受け取る
    n = int(input("サイコロの面の数は？: "))
    m = int(input("何回ふりますか？: "))

    # M回サイコロを振った結果をリストに格納
    results = []
    for _ in range(m):
        roll = random.randint(1, n)
        results.append(roll)

        print(results)


if __name__ == "__main__":
    main
