import random


class Student1:
    pass


print("Hi")


class Student2:
    print("Hi")


first_student2 = Student2()

class Student3:
    print("Hi")

    def __init__(self):
        self.height = 160
        print("I am alive!")

first_student3 = Student3()

class Student4:
    def __init__(self):
        self.height = 160

nick4 = Student4()
print(nick4.height)


class Student5:
    def __init__(self, height=160):
        self.height = height

nick5 = Student5()
kate5 = Student5(height=170)
print(nick5.height)
print(kate5.height)


class Student6:
    amount_of_students = 0

    def __init__(self, height=160):
        self.height = height
        Student6.amount_of_students += 1

nick6 = Student6()
kate6 = Student6(height=170)
print(nick6.amount_of_students)
print(Student6.amount_of_students)


class Student7:
    height = 160

    def __init__(self):
        print(self.height)

nick7 = Student7()


class Student8:
    height = 160

    def __init__(self):
        print(self.height)
        self.height += 10


nick8 = Student8()
kate8 = Student8()

class Student9:
    def __init__(self):
        self.height = 170

    def printer(self):
        print(self.height)

nick9 = Student9()
nick9.printer()

class Student10:
    amount_of_students = 0

    def __init__(self, height=160):
        self.height = height
        Student10.amount_of_students += 1

    def grow(self, height=1):
        self.height += height


nick10 = Student10()
kate10 = Student10(height=170)
nick10.grow(height=15)
print(kate10.height)
print(nick10.height)

class Student11:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f"I am a student. My name is {self.name}."

nick11 = Student11(name="Nick")
print(nick11)

class Student12:
    def __init__(self, name=None):
        self.name = name

    def __del__(self):
        print("Training is over. I am now an expert!")


nick12 = Student12()

class StudentSimulator:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.money -= 2

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 4
        self.progress -= 0.02

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.money < 0:
            print("Bankrupt…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money    = {self.money}")

    def live(self, day):
        day_str = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day_str:=^50}")

        if self.money < 15:
            self.to_work()
        elif self.progress < 0.2:
            self.to_study()
        else:
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()

        self.end_of_day()
        self.is_alive()

nick = StudentSimulator(name="Nick")
for day in range(1, 366):
    if nick.alive == False:
        break
    nick.live(day)