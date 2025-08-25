def calculate_split_bill():
    """割り勘計算を行う関数"""
    try:
        # 合計金額の入力
        amount = int(input("合計金額は？(円) > "))
        if amount <= 0:
            print("正の金額を入力してください。")
            return
        
        # 人数の入力
        number_of_people = int(input("人数は？ > "))
        if number_of_people <= 0:
            print("正の人数を入力してください。")
            return
        
        # 割り勘計算
        pay_per_people = amount // number_of_people
        fraction = amount % number_of_people
        
        # 結果表示
        print("\n=== 割り勘結果 ===")
        print(f"合計金額: {amount:,}円")
        print(f"人数: {number_of_people}人")
        print(f"1人あたり: {pay_per_people:,}円")
        
        if fraction > 0:
            print(f"端数: {fraction:,}円")
            print("※端数は別途調整が必要です")
        else:
            print("端数なし！ピッタリ割り切れました")
            
    except ValueError:
        print("正しい数値を入力してください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    print("=== 割り勘計算プログラム ===")
    calculate_split_bill()
