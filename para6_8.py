class BuildingError(Exception):
    def __init__(self, message):
        super().__init__(message)


def checker(amount_of, limit_value):
    if "13" in str(amount_of):
        raise BuildingError("знайдено число 13!")

    if amount_of > limit_value:
        raise BuildingError("Занадто багато матеріалу")
    else:
        return "Кількість матеріалу в нормі"


material = 1100


try:
    checker(material, 300)
except BuildingError as e:
    print(e)