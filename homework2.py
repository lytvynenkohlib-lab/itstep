class BuildingError(Exception):
    pass


code_to_check = """
print("1. Запуск тестового коду...")
x = 10
y = 0
res = x / y  # Тут виникне ZeroDivisionError
print("Цей рядок вже не виконається")
"""


def evaluate_and_check_code(target_code):
    print("=" * 40)
    print("ІНСПЕКТОР КОДУ: Початок перевірки...")
    print("=" * 40)

    try:
        exec(target_code)

    except Exception as error_msg:
        print("-" * 40)
        return f" [ВІДПОВІДЬ]: Знайдено помилку! Тип: {type(error_msg).__name__}. Повідомлення: {error_msg}"

    else:
        print("-" * 40)
        return "✔ [ВІДПОВІДЬ]: Помилок не знайдено, код виконано успішно."



final_result = evaluate_and_check_code(code_to_check)
print(final_result)

def divider(a, b):
 if a < b:
    raise ValueError
 if b > 100:
    raise IndexError
 return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
result = []

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
        print(result)
    except Exception as e:
        print(f"Помилка: {e}")

