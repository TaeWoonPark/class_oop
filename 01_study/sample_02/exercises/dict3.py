person = {
     "name": "Alice",
     "age": 30,
     "city": "New York"
}

# キー "name"に関連付けられた値を取得
name = person.get("name")

# キー "country" は存在しないのでデフォルト値 "USA" を返す
country = person.get("country", "USA")
age = person.get("age")
print(name)
print(country)
print(age)
city = person.pop("city")
print(city)

