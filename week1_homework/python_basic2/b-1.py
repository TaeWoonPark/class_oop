# 下記のような出力が得られる kuku_1.py を実装してください。


def main():
    # 外側 1~9までの行
    for i in range(1, 10):
        # 内側の 1~9までの列
        for j in range(1, 10):

            product = i * j

            print(f"{product}", end="")

            print("\n", end="")


if __name__ == "__main__":
    main()
