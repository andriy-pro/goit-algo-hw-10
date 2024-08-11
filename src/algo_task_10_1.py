from pulp import LpMaximize, LpProblem, LpVariable, value

# Ініціалізація проблеми
model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)

# Змінні рішення
L = LpVariable(name="Lemonade", lowBound=0, cat="Continuous")
F = LpVariable(name="Fruit_Juice", lowBound=0, cat="Continuous")

# Функція цілі
model += L + F, "Total Production"

# Обмеження
model += (2 * L + 1 * F <= 100), "Water_Constraint"
model += (1 * L <= 50), "Sugar_Constraint"
model += (1 * L <= 30), "Lemon_Juice_Constraint"
model += (2 * F <= 40), "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
lemonade_production = value(L)
fruit_juice_production = value(F)
total_production = lemonade_production + fruit_juice_production

print(f"Кількість виробленого Лимонаду: {int(lemonade_production)}")
print(f"Кількість виробленого Фруктового соку: {int(fruit_juice_production)}")
print(f"Загальна кількість вироблених напоїв: {int(total_production)}")
