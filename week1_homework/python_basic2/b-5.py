データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
from typing import List


def calculation_total(numbers: List[int]) -> int:
    total = 0

    for num in numbers:
        total += num

    return total


def calculation_max(numbers: List[int]) -> int:
    max_number = numbers[0]

    for num in numbers[1:]:
        if num > max_number:
            max_number = num

    return max_number


def calculation_min(numbers: List[int]) -> int:
    min_number = numbers[0]

    for num in numbers[1:]:
        if num < min_number:
            min_number = num

    return min_number


def calculation_avg(numbers: List[int]) -> int:
    total = calculation_total(numbers)

    return total // len(numbers)
