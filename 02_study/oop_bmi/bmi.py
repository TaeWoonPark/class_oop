class Bmi:
    def __init__(self, height, weight):

        self.value = weight / (height**2)
        if not (10 <= self.value <= 40):
            raise ValueError()"BMIが正常値の範囲を超えています)
    def __str__(self):
        return f"{self.value:.2f}"
        


tanaka_bmi = Bmi(height=1.8, weight=67.0)
sasaki_bmi = Bmi(height=1.58, weight=120.0)

print(sasaki_bmi)

print(tanaka_bmi)
