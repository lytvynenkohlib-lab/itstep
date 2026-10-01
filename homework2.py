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
        return f" ВІДПОВІДЬ: Знайдено помилку! Тип: {type(error_msg).__name__}. Повідомлення: {error_msg}"
    else:
        print("-" * 40)
        return "ВІДПОВІДЬ: Помилок не знайдено, код виконано успішно."

final_result = evaluate_and_check_code(code_to_check)
print(final_result)

print("=" * 40)
print("РОБОТА ФУНКЦІЇ DIVIDER:")
print("=" * 40)

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b завелике")
    return a / b

result = []

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
except Exception as e:
    print(f"Помилка створення словника: {type(e).__name__} -> {e}")
    data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

print("-" * 40)

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
        print(f"Успішно: {res}")
    except Exception as e:
        print(f"Помилка для ключа {repr(key)}: {type(e).__name__} -> {e}")

print("-" * 40)
print("Фінальний результат result:", result)