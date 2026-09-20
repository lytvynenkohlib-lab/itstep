class ForbiddenNumberError(Exception):

    def __str__(self):
        return " number is banned"


def check(number):
    if "13" is str(number):
        raise ForbiddenNumberError()
    else:
         return ("number is ok")

try:
    num = input("Enter a number")
    res = check(num)
    print(res)
except ForbiddenNumberError as er:
    print(er)