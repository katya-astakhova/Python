income = int(input("Введите выручку фирмы"))
cost = int(input("Введите издержки фирмы"))
if income > cost:
    print("Прибыль больше издержек")
    profit = (income-cost)/income
    print("Рентабельность равна ", profit)
    num_emp = int(input("Введите численность сотрудников"))
    profit_emp = (income-cost)/num_emp
    print("Прибыль фирмы на одного работника", "%.2f" % profit_emp)
else:
    print("Издержки больше прибыли!")
