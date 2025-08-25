fruits = ["りんご", "バナナ", "オレンジ"]
if "りんご" in fruits:
    print("りんごがリストに含まれています")

if "グレープ" in fruits:
    print("グレープがリストに含まれています")

else:
    print("グレープはリストに含まれていません")

if "りんご" not in fruits:
    print("りんごはリストに含まれていません")
else:
    print("りんごがリストに含まれています")

fruits_list = ["apple", "banana", "cherry"]

for fruit in fruits_list:
    print(fruit)
fruits_tuple = ("りんご", "バナナ", "オレンジ")
for fruit in fruits_tuple:
    print(fruit)
