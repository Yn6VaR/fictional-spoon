money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0

while True:
    sum = spend - salary
    if sum > money_capital:
        break

    spend = spend + spend * increase
    money_capital -= sum
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
