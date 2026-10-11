import json
import urllib.request


class CurrencyConverter:

    def __init__(self):
        self.rate = self.get_usd_rate()

    def get_usd_rate(self):
        """Отримує актуальний курс долара з сайту НБУ"""
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode("utf-8"))
            return float(data[0]["rate"])
        except Exception as e:
            print(f"Не вдалося отримати курс: {e}")
            return 41.0  # Резервний курс за замовчуванням

    def to_usd(self, uah):
        """Конвертує гривні в долари США"""
        return uah / self.rate


# Головна частина програми
if __name__ == "__main__":
    print("=== Конвертер валют НБУ (UAH -> USD) ===")

    converter = CurrencyConverter()
    print(f"Поточний курс USD: {converter.rate} грн\n")

    while True:
        user_input = input(
            "Введіть суму в гривнях (або напишіть 'вихід' для завершення): "
        )

        if user_input.lower() in ["вихід", "exit", "q"]:
            print("До побачення!")
            break

        try:
            uah_amount = float(user_input)
            if uah_amount < 0:
                print("Сума не може бути від'ємною!\n")
                continue

            usd_amount = converter.to_usd(uah_amount)
            print(f"Результат: {uah_amount:.2f} UAH = {usd_amount:.2f} USD\n")

        except ValueError:
            print("Будь ласка, введіть числове значення!\n")