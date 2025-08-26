# 合計値を求める関数
def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += num

    return total


# 最大値を求める関数


def calculate_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number

    return max_value


# 最小値を求める関数


def calculate_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if numbers < min_value:
            min_value = num

    return min_value


# 平均値を求める関数


def calculate_mean(numbers):
    total = calculate_total(numbers)
    count = 0
    for nember in numbers:
        count += 1
        mean_value = total // count
    return mean_value


# メーン処理


def main():
    data_input = input("データーを入力してください(スペース区切り) > ")
    numbers = [int(x) for x in data_input.split()]

    print("最大値:", calculate_total(numbers))
    print("最大値:", calculate_max(numbers))
    print("最小値:", calculate_min(numbers))
    print("平均値:", calculate_mean(numbers))


if __name__ == "__main__":
    main
