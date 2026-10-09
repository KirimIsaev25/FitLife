print('Добро пожаловать!')
user_name = input('Как вас зовут?')
user_name = user_name.title()
user_age = int(input('Сколько вам лет?'))
user_weight = input('Укажите свой вес "кг"')
user_weight = float(user_weight)
user_height = input('Укажите свой рост "м"')
user_height = float(user_height)
WATER_ML_PER_KG = 30
WATER_ML_PER_L = 1000
bmi = user_weight / (user_height ** 2)
result_bmi = round(bmi, 1)
water_ml = user_weight * WATER_ML_PER_KG
water_l = water_ml / WATER_ML_PER_L
result_water_l = round(water_l, 1)
print(
    f"Для веса кг {user_weight}, и роста {user_height} м,"
    f"ИМТ ≈ {result_bmi}, норма воды ≈, {result_water_l}",
)
print(f"Отчет для пользователя: {user_name}, {user_age} г")
print(f"Твой Индекс Массы Тела: {result_bmi}")
print(f"Рекомендуемая норма воды: {result_water_l} л. в день")
print('Расчет окончен. Будьте здоровы')
