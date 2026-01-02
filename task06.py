emails = (
    ("Ali", "ali@gmail.com"),
    ("Vali", "vali@yandex.ru"),
    ("Sami", "sami@mail.ru")
)
domins = []
for name, email in emails:
    domin = email.split('@')[1]
    domins.append(domin)
print(domins)