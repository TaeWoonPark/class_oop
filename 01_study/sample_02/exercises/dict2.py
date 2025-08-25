# ユーザー設定情報を格納するための空の辞書を作成
user_settings = {}
# 新しいユーザー設定を追加
user_settings["username"] = "bob"
user_settings["theme"] = "dark"
user_settings["notifications"] = True
# ユーザー設定の表示
print("ユーザー設定:", user_settings)
# 既存のユーザー設定を変更
user_settings["theme"] = "light"
# 変更後のユーザー設定の表示
print("変更後のユーザー設定:", user_settings)
# ユーザー設定から特定の設定を削除
del user_settings["notifications"]
# 削除後のユーザー設定の表示
print("削除後のユーザー設定:", user_settings)
