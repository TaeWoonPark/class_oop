rows = int(input("行数を入力してください:"))

cols = int(input("列数を入力してください"))

max_width = len(str(rows * cols))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"{i * j:{max_width}}", end=" ")
    print()
