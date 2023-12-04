users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
total = len(users)
unique_users = set(users)  # TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
unique_visits = len(unique_users)

dict = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

dict["Общее количество"] = total
dict["Уникальные посещения"] = unique_visits

print(dict)