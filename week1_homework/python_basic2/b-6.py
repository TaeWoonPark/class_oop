サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
import random
from typing import List


def roll_dice_sided_n(side: int, times: int) -> List[int]:
    """N面サイコロをM回振った結果を返す"""
    results = []

    for _ in range(times):
        dice = random.randint(1, side)
        results.append(dice)

    return results


if __name__ == "__main__":
    n = int(input("8: "))
    m = int(input("20: "))

    print(roll_dice_sided_n(side=n, times=m))
