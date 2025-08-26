# 下記のような出力が得られる beautiful_kuku.py を実装してください
# きれいに整っているので見やすくなっています
# 式が表示されている
# 結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
# ※結果が3桁の場合は崩れてもOKです

# 行数と列数を入力
rows = int(input("行数を入力してください"))
cols = int(input("列数を入力してください"))

max_result = rows * cols
width = len(str(max_result))


# 掛け算表を入力
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        result = i * j

        print(f"{i} x {j} = {result:{width}} | ", end=" ")
    print()
