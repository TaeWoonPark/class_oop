class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def say_name(self):
        print(f"私の名前は {self.name} です。")

    def fly(self):
        print("ぶっとんでるぜ")

    def check_registration(self):
        print(f"{self.email}は登録済みです")
